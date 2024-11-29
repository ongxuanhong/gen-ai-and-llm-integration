"""
Streamlit App
"""

import io

import streamlit as st
from docx import Document
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv()

st.set_page_config(page_title="LLM App Example Loc and Hong", page_icon="🦜")
st.title("LLM App Example Loc and Hong")


def generate_response(input_text):
    llm = AzureChatOpenAI(temperature=0.7, azure_deployment="gpt-4-0613")
    print(llm)
    st.info(llm.invoke(input_text).content)


uploaded_file = st.file_uploader("Choose a file", type=("docx"))
if uploaded_file is not None:
    # Read the uploaded file into a buffer
    bytes_data = uploaded_file.read()

    # Load the docx file into a Document object
    with io.BytesIO(bytes_data) as buffer:
        document = Document(buffer)

    # Extract paragraphs from the document
    paragraphs = [para.text for para in document.paragraphs]

    # Display the content of the docx file on the Streamlit app
    st.write("Content of the uploaded file:")
    for paragraph in paragraphs:
        st.write(paragraph)

    # Additional processing or visualization can be added here
else:
    st.write("Please upload a .docx file to display its contents.")

with st.form("my_form"):
    text = st.text_area("Enter text:")
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)
