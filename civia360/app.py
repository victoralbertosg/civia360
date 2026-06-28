import streamlit as st
from pathlib import Path
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

st.set_page_config(page_title="CIVIA 360", page_icon="🏛️", layout="centered")

# ── Modelos (cacheados para no recargar en cada rerun) ──────────────────────
@st.cache_resource
def load_models():
    embed = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    gen_name = 'google/flan-t5-small'
    tok = AutoTokenizer.from_pretrained(gen_name)
    gen = AutoModelForSeq2SeqLM.from_pretrained(gen_name)
    dim = embed.get_sentence_embedding_dimension()
    idx = faiss.IndexFlatL2(dim)
    return embed, tok, gen, idx

embed_model, tokenizer, generator, index = load_models()

# ── Estado persistente de Streamlit ─────────────────────────────────────────
if "texts" not in st.session_state:
    st.session_state.texts = []

# ── Funciones ────────────────────────────────────────────────────────────────
def index_chunks(content: str):
    """Divide el texto en fragmentos y los indexa en FAISS."""
    chunks = [content[i:i+1000] for i in range(0, len(content), 1000)]
    for chunk in chunks:
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
    q_emb = embed_model.encode(query)
    n = len(st.session_state.texts)
    k = min(k, n)
    D, I = index.search(np.array([q_emb], dtype='float32'), k)
    return [(st.session_state.texts[i], D[0][j]) for j, i in enumerate(I[0]) if i < n]

def generate_answer(context: str, query: str) -> str:
    prompt = (
        f"Read the context and answer the question in Spanish.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}\n\n"
        f"Answer:"
    )
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    output_ids = generator.generate(
        **inputs,
        max_new_tokens=200,
        num_beams=4,
        early_stopping=True,
    )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

# ── Interfaz ─────────────────────────────────────────────────────────────────
st.title("🏛️ CIVIA 360 – Consulta Ciudadana con IA")
st.caption("Sistema de Recuperación y Generación Aumentada para Servicios Municipales")

st.divider()

# — Panel de carga —
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
    if st.button("📋 Cargar datos de ejemplo", use_container_width=True):
        n = load_sample_data()
        st.success(f"✅ {n} archivos de ejemplo cargados ({len(st.session_state.texts)} fragmentos indexados)")

if uploaded:
    add_uploaded_files(uploaded)
    st.success(f"✅ Documentos indexados — {len(st.session_state.texts)} fragmentos en memoria")

# — Estado del índice —
n_docs = len(st.session_state.texts)
if n_docs > 0:
    st.info(f"📚 Base de conocimiento activa: **{n_docs} fragmentos** indexados")
else:
    st.warning("⚠️ No hay documentos cargados. Sube archivos o usa los datos de ejemplo.")

st.divider()

# — Consulta —
query = st.text_input("🔍 Escribe tu pregunta:", placeholder="¿Cuál es el procedimiento para solicitar una licencia de construcción?")

if query:
    if n_docs == 0:
        st.error("❌ Primero carga documentos antes de realizar consultas.")
    else:
        topk = st.slider("Número de fragmentos de contexto", 1, min(10, n_docs), min(5, n_docs))
        with st.spinner("Buscando y generando respuesta..."):
            results = retrieve(query, k=topk)
            context = "\n\n".join([r[0] for r in results])
            answer = generate_answer(context, query)

        st.subheader("💬 Respuesta")
        st.success(answer)

        with st.expander("📄 Ver fuentes utilizadas"):
            for i, (frag, dist) in enumerate(results, 1):
                st.markdown(f"**Fuente {i}** *(dist={dist:.2f})*")
                st.text(frag[:300] + ("…" if len(frag) > 300 else ""))
                st.divider()
