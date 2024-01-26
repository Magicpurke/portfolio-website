import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Miki Lovrenovic")
    content = """
    Hi, I am Miki! I am a beginner Python programmer trying to make his way into the world of IT
    """
    st.info(content)
