import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/personal_image.png", width=350)

with col2:
    st.title("Anis Al-khatib")
    content = """
    A passionate and dedicated software developer with a strong foundation in creating innovative and efficient solutions. Over the course of my programming journey, I've successfully developed 20 robust applications using Python, demonstrating my expertise in this versatile and powerful language.

    In addition to my Python proficiency, I have an intermediate skill level in JavaScript, which allows me to create dynamic and interactive web applications. My understanding of HTML and CSS further complements my front-end development skills, enabling me to design visually appealing and user-friendly interfaces.
    """
    st.info(content)

explore = "Feel free to explore my portfolio and see how my passion for coding translates into practical and impactful projects. I’m always excited to take on new challenges and contribute to meaningful projects. Let's connect and create something amazing together!"
st.write(explore)

col3, margin, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
break_point = int(len(df) / 2)

def centered_header(title):
    return f'<h2 style="text-align: center;">{title}</h2>'

def centered_link(url):
    return f'<p style="text-align: center;"><a href="{url}">Source Code</a></p>'

def centered_description(description):
    return f'<p style="text-align: center;">{description}</p>'

with col3:
    for index, row in df[:break_point].iterrows():
        st.markdown(centered_header(row["title"]), unsafe_allow_html=True)
        st.image("images/" + row["image"])
        st.markdown(centered_link(row["url"]), unsafe_allow_html=True)
        st.markdown(centered_description(row["description"]), unsafe_allow_html=True)

with col4:
    for index, row in df[break_point:].iterrows():
        st.markdown(centered_header(row["title"]), unsafe_allow_html=True)
        st.image("images/" + row["image"])
        st.markdown(centered_link(row["url"]), unsafe_allow_html=True)
        st.markdown(centered_description(row["description"]), unsafe_allow_html=True)
