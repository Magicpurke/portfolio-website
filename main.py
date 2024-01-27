import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2, = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Miki Lovrenovic")
    content = """
    Hi, I am Miki! I am a beginner Python programmer trying to make his way into the world of IT
    """
    st.info(content)

text_content = """
Below you can find some of the apps i have built in Python. Feel free to contact me!
"""
st.text(text_content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("06 data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']}])")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']}])")
