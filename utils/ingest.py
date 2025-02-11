import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

FILE_PATH = os.getcwd() + "/datas/example.pdf"
DB_PATH = os.getcwd() + "/db"

def process_document():
    loader = PyPDFLoader(FILE_PATH)
    documents = loader.load()

    splitter = CharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20
    )
    text_chunks = splitter.split_documents(documents)
    document_list = [
        Document(page_content=chunk.page_content, metadata={"source": "example"})
        for chunk in text_chunks
    ]

    embeddings = OllamaEmbeddings(model="deepseek-r1:1.5b", base_url="http://localhost:11434")

    vectorStore = Chroma(collection_name="example", embedding_function=embeddings, persist_directory=DB_PATH)
    vectorStore.add_documents(document_list)