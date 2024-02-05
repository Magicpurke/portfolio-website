import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("pages/topics.csv")

st.header("Contact Me")
topics = df["topic"].unique().tolist()

with st.form(key="email"):
    user_email = st.text_input("Your email address")
    selected_option = st.selectbox("What topic do you want to discuss", topics)
    raw_message = st.text_area("Your message here")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}    
"""

    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent")



