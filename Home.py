import streamlit as st
import pandas
from PIL import Image

st.set_page_config(layout="wide")
col1, col2, = st.columns(2)

with col1:
    original_image_path = "images/photo.png"
    original_image = Image.open(original_image_path)

    rotated_image = original_image.rotate(-90)

    st.image(rotated_image, width=600)

with col2:
    st.title("Miodrag 'Miki' Lovrenovic")

    content = """
    Als aufstrebender Python-Programmierer präsentiere ich hier meine Projekte. Auf der Suche nach beruflichen Möglichkeiten
vertiefe ich meine Python-Kenntnisse und erkunde die Welt der Programmierung. Begleite mich auf meinem Weg und entdecke
 die spannenden Projekte, an denen ich arbeite. Ich freue mich darauf, meine Fähigkeiten weiter zu entwickeln
 und in der Programmierwelt Fuß zu fassen.
    """
    st.info(content)

text_content = """
Hier findest du einige der Anwendungen, die ich in Python entwickelt habe. Kontaktiere mich gerne!
"""
st.text(text_content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("06 data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']}])")
