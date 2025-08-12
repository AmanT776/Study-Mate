import os
import tempfile
import streamlit as st
from app.loaders import pdf_loader
import cryptography

st.markdown("<h1 style='text-align: center;'>Study Mate</h1>", unsafe_allow_html=True)


user_input = st.chat_input("user")
with st.chat_message("user"):
    st.write(user_input)
with st.chat_message("bot"):
    st.write("how are you")


uploaded_file = st.sidebar.file_uploader("file",type="pdf")
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name
        pdf_loader(tmp_path)

