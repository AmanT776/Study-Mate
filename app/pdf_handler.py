import streamlit as st
import tempfile



def pdf_handler(uploaded_file):
    submit = st.sidebar.button("submit to db", key="submit_pdf") 
    file = None
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            file = tmp.name
    return file, submit
