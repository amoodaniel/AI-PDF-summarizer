#Needed Libraries
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms.openai import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain_community.callbacks.manager import get_openai_callback
from pypdf import PdfReader

def process_text(text):
    #process the given text by splitting it into chunks and converting them into embeddings to form a knowledge base
    text_splitter = CharacterTextSplitter(
        separator= '\n',
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    chunks = text_splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
    #Create a FAISS index from the text chunks using the embeddings
    knowledgeBase = FAISS.from_texts(chunks, embeddings)

    return knowledgeBase

def summarizer(pdf):
    #To sumarize the content of the pDF file

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        #Extract text from each page of the PDF
        for page in pdf_reader.pages:
            text += page.extract_text() or ""

        #Process the extracted text to create a knowledge base
        knowledgeBase = process_text(text)

        #Define a query for summarziation
        query = 'Sumarize the content of the uploaded PDF file in approximately 3-5 sentences'
        if query:
            #Perform the simililarity search in the knowledge bade using the query
            docs = knowledgeBase.similarity_search(query)
            #Specifify the model use for generating the Summary
            OpenAIModel = 'gpt-3.5-turbo-16k'
            llm = ChatOpenAI(model=OpenAIModel, temperature = 0.1)

            #Load a question answering chain with the specified model
            chain = load_qa_chain(llm, chain_type='stuff')

            with get_openai_callback() as cost:
                response = chain.run(input_documents = docs, question = query)

                return response