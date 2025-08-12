import streamlit as st
from app.load_and_chunk_file import load_and_chunk_file
from app.pdf_handler import pdf_handler
import cryptography


st.markdown("<h1 style='text-align: center;'>Study Mate</h1>", unsafe_allow_html=True)


user_input = st.chat_input("user")
with st.chat_message("user"):
    st.write(user_input)
with st.chat_message("bot"):
    st.write("how are you")


uploaded_file = st.sidebar.file_uploader("file",type="pdf")

if uploaded_file:
    st.sidebar.success(f"Uploaded {uploaded_file.name}")
file,submit = pdf_handler(uploaded_file)

if file and submit:
    with st.spinner("Indexing PDF..."):
        chunk = load_and_chunk_file(file)
        st.success("PDF indexed successfully")



