import streamlit as st
from pathlib import Path
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

st.set_page_config(page_title="CIVIA 360", page_icon="🏛️", layout="centered")

# ── Traducción manual de preguntas frecuentes ES→EN ─────────────────────────
QUESTION_MAP = {
    "licencia de construcción": "construction license procedure documents required steps",
    "licencia de obra":         "construction license procedure documents required steps",
    "construir":                "construction permit building license procedure",
    "registrar un negocio":     "business registration documents required municipality",
    "negocio":                  "business registration documents required",
    "predial":                  "property tax payment deadlines discounts",
    "impuesto predial":         "property tax payment deadlines discounts",
    "acta de nacimiento":       "birth certificate request civil registry",
    "nacimiento":               "birth certificate civil registry documents",
    "uso de suelo":             "land use regulations residential commercial restrictions",
    "suelo":                    "land use zoning regulations restrictions",
    "descuento":                "discounts exemptions property tax",
    "documentos":               "documents required registration license",
    "plazo":                    "payment deadlines schedule fees",
    "multa":                    "penalty fine construction without license",
}

def translate_query(query: str) -> str:
    """Convierte una pregunta en español a términos clave en inglés."""
    q_lower = query.lower()
    for es_key, en_terms in QUESTION_MAP.items():
        if es_key in q_lower:
            return en_terms
    # Si no hay match, devuelve la pregunta original
    return query

# ── Modelos (cacheados para no recargar en cada rerun) ──────────────────────
@st.cache_resource(show_spinner="⏳ Cargando modelos de IA (primera vez puede tardar 1-2 min)…")
def load_models():
    embed = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    gen_name = 'google/flan-t5-small'
    tok = AutoTokenizer.from_pretrained(gen_name)
    gen = AutoModelForSeq2SeqLM.from_pretrained(gen_name)
    dim = embed.get_sentence_embedding_dimension()
    idx = faiss.IndexFlatL2(dim)
    return embed, tok, gen, idx

embed_model, tokenizer, generator, index = load_models()

# ── Estado persistente ───────────────────────────────────────────────────────
if "texts" not in st.session_state:
    st.session_state.texts = []
if "index_count" not in st.session_state:
    st.session_state.index_count = 0

# ── Funciones ────────────────────────────────────────────────────────────────
def index_chunks(content: str):
    chunks = [content[i:i+800] for i in range(0, len(content), 800)]
    for chunk in chunks:
        if chunk.strip():
            emb = embed_model.encode(chunk)
            index.add(np.array([emb], dtype='float32'))
            st.session_state.texts.append(chunk)
            st.session_state.index_count += 1

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

def retrieve(query_en: str, k: int = 5):
    q_emb = embed_model.encode(query_en)
    n = len(st.session_state.texts)
    if n == 0:
        return []
    k = min(k, n)
    D, I = index.search(np.array([q_emb], dtype='float32'), k)
    return [(st.session_state.texts[i], float(D[0][j])) for j, i in enumerate(I[0]) if i < n]

def generate_answer(context: str, query_original: str, query_en: str) -> str:
    prompt = (
        f"Based on the following context, answer the question concisely.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {query_en}\n\n"
        f"Answer:"
    )
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    output_ids = generator.generate(
        **inputs,
        max_new_tokens=200,
        num_beams=4,
        early_stopping=True,
        no_repeat_ngram_size=3,
    )
    answer = tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()

    # Fallback: si el modelo no produce texto útil, devolver el mejor fragmento
    if not answer or len(answer) < 5:
        return None
    return answer

# ── Interfaz ─────────────────────────────────────────────────────────────────
st.title("🏛️ CIVIA 360 – Consulta Ciudadana con IA")
st.caption("Asistente virtual para trámites y servicios municipales")

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
        st.success(f"✅ {n} archivos cargados — {st.session_state.index_count} fragmentos indexados")

if uploaded:
    with st.spinner("Indexando archivos subidos…"):
        add_uploaded_files(uploaded)
    st.success(f"✅ {len(uploaded)} archivo(s) indexados — {st.session_state.index_count} fragmentos en total")

# — Estado del índice —
n_docs = len(st.session_state.texts)
if n_docs > 0:
    st.info(f"📚 Base de conocimiento activa: **{n_docs} fragmentos** indexados")
else:
    st.warning("⚠️ Sin documentos. Usa el botón **Datos de ejemplo** o sube archivos .txt")

st.divider()

# — Consulta —
query = st.text_input(
    "🔍 Escribe tu pregunta en español:",
    placeholder="¿Cuál es el procedimiento para solicitar una licencia de construcción?"
)

if query:
    if n_docs == 0:
        st.error("❌ Primero carga documentos antes de realizar consultas.")
    else:
        topk = st.slider("Fragmentos de contexto", 1, min(10, n_docs), min(5, n_docs))
        with st.spinner("Buscando y generando respuesta…"):
            # Traducir la pregunta al inglés para mejor recuperación
            query_en = translate_query(query)
            results = retrieve(query_en, k=topk)

            if not results:
                st.error("No se encontraron fragmentos relevantes.")
            else:
                context = "\n\n".join([r[0] for r in results])
                answer = generate_answer(context, query, query_en)

        st.subheader("💬 Respuesta")
        if answer:
            st.success(answer)
        else:
            # Fallback: mostrar el fragmento más relevante directamente
            st.info("ℹ️ El modelo no generó una respuesta directa. Fragmento más relevante encontrado:")
            st.markdown(f"> {results[0][0][:600]}")

        with st.expander("📄 Ver todos los fragmentos fuente"):
            for i, (frag, dist) in enumerate(results, 1):
                st.markdown(f"**Fuente {i}** — similitud: `{1/(1+dist):.2%}`")
                st.text(frag[:400] + ("…" if len(frag) > 400 else ""))
                st.divider()
