import streamlit as st
from pathlib import Path
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# ---- Configuración de modelos pequeños ----
embed_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
gen_model_name = 'google/flan-t5-small'
tokenizer = AutoTokenizer.from_pretrained(gen_model_name)
generator = AutoModelForSeq2SeqLM.from_pretrained(gen_model_name)
gen_pipe = pipeline('text2text-generation', model=generator, tokenizer=tokenizer, max_length=200)

# ---- Funciones de indexado ----
INDEX_DIR = Path('faiss_index')
INDEX_DIR.mkdir(exist_ok=True)
DIM = embed_model.get_sentence_embedding_dimension()
index = faiss.IndexFlatL2(DIM)
texts = []  # lista de textos completos

def add_documents(files):
    for f in files:
        content = f.read().decode('utf-8')
        # dividir en fragmentos simples de 200 palabras
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
    output = gen_pipe(prompt)[0]['generated_text']
    return output

st.title('Demo CIVIA 360 – RAG con modelos pequeños')
uploaded = st.file_uploader('Sube documentos (.txt, .md)', accept_multiple_files=True, type=['txt','md'])
if uploaded:
    add_documents(uploaded)
    st.success('Documentos indexados')

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
