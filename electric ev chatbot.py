import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model
@st.cache_resource
def load_model():
    return SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

@st.cache_data
def prepare_knowledge_base(df):
    """Create searchable knowledge base from dataset"""
    knowledge_entries = []
    
    for idx, row in df.iterrows():
        # Create natural language entries
        entry = f"The {row['Make']} {row['Model']} has an electric range of {row['Electric Range']} miles"
        knowledge_entries.append({
            'text': entry,
            'data': row.to_dict()
        })
    
    return knowledge_entries

@st.cache_resource
def create_faiss_index(_model, knowledge_base):
    """Create FAISS index for semantic search"""
    texts = [entry['text'] for entry in knowledge_base]
    embeddings = _model.encode(texts)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings.astype('float32'))
    
    return index, embeddings

def get_answer(question, model, knowledge_base, index):
    """Find relevant answer using semantic search"""
    question_embedding = model.encode([question])
    
    D, I = index.search(question_embedding.astype('float32'), k=3)
    
    # Get top matches
    answers = []
    for idx in I[0]:
        answers.append(knowledge_base[idx])
    
    return answers

# Streamlit app
st.title("🔋 EV Range Assistant (RAG)")

model = load_model()
df = pd.read_csv('cleaned_ev_dataset.csv')
knowledge_base = prepare_knowledge_base(df)
index, embeddings = create_faiss_index(model, knowledge_base)

# Chat interface
if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about EVs..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        results = get_answer(prompt, model, knowledge_base, index)
        
        response = "Based on our database:\n\n"
        for i, result in enumerate(results, 1):
            response += f"{i}. {result['text']}\n"
        
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
