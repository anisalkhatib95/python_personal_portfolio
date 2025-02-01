import streamlit as st
from send_email import send_email


st.header("Contact Me")

with st.form(key="email_form"):
    user_mail = st.text_input("Your email address...")
    raw_message = st.text_area("Your messaage...")
    subject = st.selectbox(label="What is the topic of this message?", 
                           options=[
                               "Question", 
                               "Request", 
                               "Appointment"
                           ])
    message = f"""\
Subject: Python Portfolio Website: {subject}

From: {user_mail}

{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Message was sent successfully.")