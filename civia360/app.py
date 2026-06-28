import streamlit as st
from pathlib import Path
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import torch

st.set_page_config(page_title="CIVIA 360", page_icon="🏛️", layout="centered")

# ── Modelos cacheados ────────────────────────────────────────────────────────
@st.cache_resource(show_spinner="⏳ Cargando modelos de IA (primera vez puede tardar 1-2 min)…")
def load_models():
    # Embeddings multilingüe para búsqueda semántica en español
    embed = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    dim = embed.get_sentence_embedding_dimension()
    idx = faiss.IndexFlatL2(dim)

    # QA extractivo multilingüe — SIN usar pipeline()
    model_name = "deepset/xlm-roberta-base-squad2"
    tok = AutoTokenizer.from_pretrained(model_name)
    qa_model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    qa_model.eval()

    return embed, idx, tok, qa_model

embed_model, index, qa_tokenizer, qa_model = load_models()

# ── Estado persistente ───────────────────────────────────────────────────────
if "texts" not in st.session_state:
    st.session_state.texts = []

# ── Funciones ────────────────────────────────────────────────────────────────
def index_chunks(content: str):
    """Divide texto en fragmentos solapados y los indexa en FAISS."""
    size, overlap = 500, 100
    start = 0
    while start < len(content):
        chunk = content[start:start + size]
        if chunk.strip():
            emb = embed_model.encode(chunk)
            index.add(np.array([emb], dtype='float32'))
            st.session_state.texts.append(chunk)
        start += size - overlap

def add_uploaded_files(files):
    for f in files:
        content = f.read().decode('utf-8')
        index_chunks(content)

def load_sample_data():
    example_dir = Path(__file__).parent / 'sample_data'
    loaded = 0
    for f in sorted(example_dir.iterdir()):
        if f.suffix in ['.txt', '.md']:
            content = f.read_text(encoding='utf-8')
            index_chunks(content)
            loaded += 1
    return loaded

def retrieve(query: str, k: int = 5):
    """Recupera los k fragmentos más similares semánticamente."""
    q_emb = embed_model.encode(query)
    n = len(st.session_state.texts)
    if n == 0:
        return []
    k = min(k, n)
    D, I = index.search(np.array([q_emb], dtype='float32'), k)
    return [(st.session_state.texts[i], float(D[0][j])) for j, i in enumerate(I[0]) if i < n]

def answer_question(context: str, question: str) -> dict:
    """
    QA extractivo manual sin pipeline().
    Devuelve {'answer': str, 'score': float}.
    """
    try:
        inputs = qa_tokenizer(
            question,
            context,
            return_tensors="pt",
            truncation=True,
            max_length=512,
            stride=128,
            return_overflowing_tokens=False,
            padding=True,
        )
        with torch.no_grad():
            outputs = qa_model(**inputs)

        start_logits = outputs.start_logits[0]
        end_logits   = outputs.end_logits[0]

        # Obtener los índices con mayor puntuación
        start_idx = int(torch.argmax(start_logits))
        end_idx   = int(torch.argmax(end_logits)) + 1

        # Asegurar orden correcto
        if end_idx <= start_idx:
            end_idx = start_idx + 1

        input_ids = inputs["input_ids"][0]
        answer_tokens = input_ids[start_idx:end_idx]
        answer = qa_tokenizer.decode(answer_tokens, skip_special_tokens=True).strip()

        # Score combinado normalizado
        s_score = float(torch.softmax(start_logits, dim=-1)[start_idx])
        e_score = float(torch.softmax(end_logits,   dim=-1)[end_idx - 1])
        score   = (s_score + e_score) / 2.0

        return {"answer": answer, "score": score}
    except Exception as e:
        return {"answer": "", "score": 0.0}

# ── Interfaz ─────────────────────────────────────────────────────────────────
st.title("🏛️ CIVIA 360 – Consulta Ciudadana con IA")
st.caption("Asistente virtual multilingüe para trámites y servicios municipales")

st.divider()

# — Carga de documentos —
col1, col2 = st.columns([3, 1])
with col1:
    uploaded = st.file_uploader(
        "📂 Sube documentos municipales (.txt, .md)",
        accept_multiple_files=True,
        type=['txt', 'md'],
    )
with col2:
    st.write("")
    st.write("")
    if st.button("📋 Datos de ejemplo", use_container_width=True):
        with st.spinner("Indexando documentos de ejemplo…"):
            n = load_sample_data()
        st.success(f"✅ {n} archivos cargados — {len(st.session_state.texts)} fragmentos indexados")

if uploaded:
    with st.spinner("Indexando archivos subidos…"):
        add_uploaded_files(uploaded)
    st.success(f"✅ {len(uploaded)} archivo(s) indexados — {len(st.session_state.texts)} fragmentos en total")

# — Estado del índice —
n_docs = len(st.session_state.texts)
if n_docs > 0:
    st.info(f"📚 Base de conocimiento activa: **{n_docs} fragmentos** indexados")
else:
    st.warning("⚠️ Sin documentos. Usa **Datos de ejemplo** o sube archivos .txt / .md")

st.divider()

# — Consulta en español —
query = st.text_input(
    "🔍 Escribe tu pregunta en español:",
    placeholder="¿Cuál es el procedimiento para solicitar una licencia de construcción?"
)

if query:
    if n_docs == 0:
        st.error("❌ Primero carga documentos antes de realizar consultas.")
    else:
        topk = st.slider("Fragmentos de contexto a revisar", 1, min(10, n_docs), min(5, n_docs))

        with st.spinner("🔎 Buscando y extrayendo respuesta…"):
            results  = retrieve(query, k=topk)
            if not results:
                st.error("No se encontraron fragmentos relevantes.")
                st.stop()
            context  = "\n\n".join([r[0] for r in results])
            result   = answer_question(context, query)
            answer   = result.get("answer", "").strip()
            score    = result.get("score", 0.0)

        # — Mostrar respuesta —
        st.subheader("💬 Respuesta")
        if answer and score > 0.05 and len(answer) > 3:
            st.success(answer)
            st.caption(f"Confianza del modelo: {score:.0%}")
        else:
            st.warning("⚠️ No se encontró respuesta precisa. Mostrando fragmento más relevante:")
            st.info(results[0][0][:600])

        # — Fuentes —
        with st.expander("📄 Ver fragmentos fuente utilizados"):
            for i, (frag, dist) in enumerate(results, 1):
                relevancia = max(0.0, 1.0 - dist / 5.0)
                st.markdown(f"**Fragmento {i}** — relevancia: `{relevancia:.0%}`")
                st.text(frag[:400] + ("…" if len(frag) > 400 else ""))
                st.divider()
