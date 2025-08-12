import streamlit as st

st.markdown("<h1 style='text-align: center;'>Study Mate</h1>", unsafe_allow_html=True)


user_input = st.chat_input("user")
with st.chat_message("user"):
    st.write(user_input)


file = st.sidebar.file_uploader("file")
