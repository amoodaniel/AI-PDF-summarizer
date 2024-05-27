import streamlit as st
import os
from dotenv import load_dotenv
from utils import *


def main():
    st.set_page_config(page_title = 'PDF Sumarizer')

    st.title("PDF Summarizing")
    st.write("Summarize your PDF files in just a few seconds")
    st.write('Developed by Daniel Amoo')
    st.divider()

    pdf = st.file_uploader('Upload your PDF Document', type = 'pdf')

    #Creating a button for users to submit their PDF
    submit = st.button('Generate Summary')

    load_dotenv()
    #Setting the OpenAI API key as an environment variable
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


    if submit:
        response = summarizer(pdf)

        st.subheader('Summary of the file')
        st.write(response)
if __name__ == '__main__':
    main()