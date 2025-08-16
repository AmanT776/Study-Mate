import streamlit as st
from app.load_and_chunk_file import load_and_chunk_file
from app.pdf_handler import pdf_handler
from app.vector_store import vector_store
from app.chain import create_rag_chain
from app.retriever import create_retriever
import cryptography

st.markdown("<h1 style='text-align: center;'>Study Mate</h1>", unsafe_allow_html=True)

if "retriever" not in st.session_state:
    st.session_state.retriever = None
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

uploaded_file = st.sidebar.file_uploader("file", type="pdf")

if uploaded_file:
    st.sidebar.success(f"Uploaded {uploaded_file.name}")

file, submit = pdf_handler(uploaded_file)

if file and submit:
    with st.spinner("Indexing PDF..."):
        chunked_docs = load_and_chunk_file(file)
        vectordb = vector_store(chunked_docs)
        st.session_state.retriever = create_retriever(vectordb)
        st.session_state.rag_chain = create_rag_chain(st.session_state.retriever)
        st.success("PDF indexed successfully")

if st.session_state.rag_chain:
    st.info("Ready to answer questions")
    question = st.text_input("Ask a question about the PDF: ")
    if question:
        with st.spinner("Generating answer..."):
            answer = st.session_state.rag_chain.invoke(question)
            st.write(answer)
