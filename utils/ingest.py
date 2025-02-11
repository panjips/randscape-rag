import os
import glob

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from app.config import Config

def process_document():
    loader = PyPDFLoader(Config.FILE_PATH+"example.pdf")
    documents = loader.load()

    splitter = CharacterTextSplitter(
        chunk_size=int(Config.CHUNK_SIZE),
        chunk_overlap=int(Config.CHUNK_OVERLAP)
    )
    text_chunks = splitter.split_documents(documents)
    document_list = [
        Document(page_content=chunk.page_content, metadata={"source": Config.CHROMA_COLLECTION})
        for chunk in text_chunks
    ]

    embeddings = OllamaEmbeddings(model=Config.OLLAMA_MODEL, base_url=Config.OLLAMA_BASE_URL)

    vectorStore = Chroma(collection_name=Config.CHROMA_COLLECTION, embedding_function=embeddings, persist_directory=Config.DB_PATH)
    vectorStore.add_documents(document_list)