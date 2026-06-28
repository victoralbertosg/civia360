import streamlit as st
from pathlib import Path
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline

st.set_page_config(page_title="CIVIA 360", page_icon="🏛️", layout="centered")

# ── Modelos cacheados ────────────────────────────────────────────────────────
@st.cache_resource(show_spinner="⏳ Cargando modelos de IA (primera vez puede tardar 1-2 min)…")
def load_models():
    # Embeddings multilingüe (soporta español e inglés)
    embed = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    dim = embed.get_sentence_embedding_dimension()
    idx = faiss.IndexFlatL2(dim)

    # QA extractivo multilingüe — extrae respuestas directas del contexto en español
    qa = pipeline(
        "question-answering",
        model="deepset/xlm-roberta-base-squad2",
        tokenizer="deepset/xlm-roberta-base-squad2",
    )
    return embed, idx, qa

embed_model, index, qa_pipeline = load_models()

# ── Estado persistente ───────────────────────────────────────────────────────
if "texts" not in st.session_state:
    st.session_state.texts = []

# ── Funciones ────────────────────────────────────────────────────────────────
def index_chunks(content: str):
    """Divide el texto en fragmentos y los indexa en FAISS."""
    chunks = [content[i:i+600] for i in range(0, len(content), 500)]
    for chunk in chunks:
        if chunk.strip():
            emb = embed_model.encode(chunk)
            index.add(np.array([emb], dtype='float32'))
            st.session_state.texts.append(chunk)

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
    """Recupera los k fragmentos más similares a la pregunta."""
    q_emb = embed_model.encode(query)
    n = len(st.session_state.texts)
    if n == 0:
        return []
    k = min(k, n)
    D, I = index.search(np.array([q_emb], dtype='float32'), k)
    return [(st.session_state.texts[i], float(D[0][j])) for j, i in enumerate(I[0]) if i < n]

def answer_question(context: str, question: str):
    """
    Usa el modelo extractivo para encontrar la respuesta exacta en el contexto.
    Devuelve dict con 'answer', 'score', 'start', 'end'.
    """
    try:
        result = qa_pipeline(question=question, context=context, max_answer_len=300)
        return result
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
    st.warning("⚠️ Sin documentos. Usa el botón **Datos de ejemplo** o sube archivos .txt / .md")

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
            # 1. Recuperar fragmentos relevantes
            results = retrieve(query, k=topk)
            if not results:
                st.error("No se encontraron fragmentos relevantes.")
            else:
                # 2. Concatenar contexto y buscar la respuesta
                context = "\n\n".join([r[0] for r in results])
                result = answer_question(context, query)
                answer = result.get("answer", "").strip()
                score  = result.get("score", 0.0)

        # — Mostrar respuesta —
        st.subheader("💬 Respuesta")
        if answer and score > 0.05:
            st.success(answer)
            st.caption(f"Confianza del modelo: {score:.0%}")
        else:
            st.warning(
                "⚠️ No se encontró una respuesta precisa con la confianza suficiente. "
                "Intenta reformular la pregunta o añadir más documentos."
            )
            # Mostrar fragmento más relevante como referencia
            st.markdown("**Fragmento más relevante encontrado:**")
            st.info(results[0][0][:500])

        # — Fuentes —
        with st.expander("📄 Ver fragmentos fuente utilizados"):
            for i, (frag, dist) in enumerate(results, 1):
                relevancia = max(0.0, 1.0 - dist / 5.0)
                st.markdown(f"**Fragmento {i}** — relevancia: `{relevancia:.0%}`")
                st.text(frag[:400] + ("…" if len(frag) > 400 else ""))
                st.divider()
