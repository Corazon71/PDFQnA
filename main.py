import os
import gradio as gr
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_vertexai import ChatVertexAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.runnables  import RunnablePassthrough

load_dotenv()
Model = ChatVertexAI(model_name = "gemini-1.5-pro")
Splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
Embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
Prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a super talented assistant who provided with an document will answer questions about it. This is the context - {context}"),
    ("human", "{question}"),
])


def start(message, history):
    Path = message["files"][0]["path"]
    Loader = PyPDFLoader(Path)
    Data = Loader.load()
    Docs = Splitter.split_documents(Data)
    Vector_DB = Chroma.from_documents(Docs, Embeddings)
    Retrieve = Vector_DB.as_retriever()
    Rag_chain = {"context": Retrieve, "question": RunnablePassthrough()} | Prompt | Model
    response = Rag_chain.invoke(message["text"])
    return response.content


Demo = gr.ChatInterface(
    start,
    textbox = gr.MultimodalTextbox(),
    multimodal = True,
    title = "PDFQnA"
)

Demo.launch()
