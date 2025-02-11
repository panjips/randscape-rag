import os

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from app.config import Config

def get_vector_store():
    embeddings = OllamaEmbeddings(model=Config.OLLAMA_MODEL, base_url=Config.OLLAMA_BASE_URL)
    vectorStore = Chroma(collection_name=Config.CHROMA_COLLECTION, embedding_function=embeddings, persist_directory=Config.DB_PATH)
    
    return vectorStore

def retriver(query):
    vectorStore = get_vector_store()
    results = vectorStore.similarity_search(query, k=2)

    return [doc.page_content for doc in results]