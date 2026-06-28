import streamlit as st
from pathlib import Path
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# ---- Configuración de modelos pequeños ----
embed_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
gen_model_name = 'google/flan-t5-small'
tokenizer = AutoTokenizer.from_pretrained(gen_model_name)
generator = AutoModelForSeq2SeqLM.from_pretrained(gen_model_name)




# ---- Funciones de indexado ----
INDEX_DIR = Path('faiss_index')
INDEX_DIR.mkdir(exist_ok=True)
DIM = embed_model.get_sentence_embedding_dimension()
index = faiss.IndexFlatL2(DIM)
texts = []  # lista de textos completos

def add_documents(files):
    for f in files:
        # Support both Streamlit uploaded files (have .read) and local Path objects
        if hasattr(f, "read"):
            content = f.read().decode('utf-8')
        else:
            content = Path(f).read_text(encoding='utf-8')
        # dividir en fragmentos simples de ~1000 caracteres
        chunks = [content[i:i+1000] for i in range(0, len(content), 1000)]
        for chunk in chunks:
            emb = embed_model.encode(chunk)
            index.add(np.array([emb]).astype('float32'))
            texts.append(chunk)

def retrieve(query, k=5):
    q_emb = embed_model.encode(query)
    D, I = index.search(np.array([q_emb]).astype('float32'), k)
    results = [(texts[i], D[0][j]) for j, i in enumerate(I[0])]
    return results

def generate_answer(context, query):
    prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    output_ids = generator.generate(**inputs, max_length=200)
    output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output

st.title('Demo CIVIA 360 – RAG con modelos pequeños')
uploaded = st.file_uploader('Sube documentos (.txt, .md)', accept_multiple_files=True, type=['txt','md'])
if uploaded:
    add_documents(uploaded)
    st.success('Documentos indexados')

if st.button('Cargar datos de ejemplo'):
    # Load the sample files that live in the same directory as this script
    example_dir = Path(__file__).parent / 'sample_data'
    for f in example_dir.iterdir():
        if f.suffix in ['.txt', '.md']:
            content = f.read_text(encoding='utf-8')
            # Reuse the same processing logic as uploaded files
            chunks = [content[i:i+1000] for i in range(0, len(content), 1000)]
            for chunk in chunks:
                emb = embed_model.encode(chunk)
                index.add(np.array([emb]).astype('float32'))
                texts.append(chunk)
    st.success('Datos de ejemplo cargados')
query = st.text_input('Pregunta')
if query and len(texts) > 0:
    topk = st.slider('Número de fragmentos', 1, 10, 5)
    results = retrieve(query, k=topk)
    context = "\n\n".join([r[0] for r in results])
    answer = generate_answer(context, query)
    st.subheader('Respuesta')
    st.write(answer)
    st.subheader('Fuentes usadas')
    for i, (frag, dist) in enumerate(results, 1):
        st.write(f"**Fuente {i}:** {frag[:200]}… (dist={dist:.2f})")
