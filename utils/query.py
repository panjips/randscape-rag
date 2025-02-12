import os

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from app.config import Config

def get_vector_store():
    embeddings = OllamaEmbeddings(model=Config.OLLAMA_MODEL, base_url=Config.OLLAMA_BASE_URL)
    vectorStore = Chroma(collection_name=Config.CHROMA_COLLECTION, embedding_function=embeddings, persist_directory=Config.DB_PATH)
    
    return vectorStore

def retriver(query, k: int = 5):
    vectorStore = get_vector_store()
    results = vectorStore.similarity_search_with_score(query, k)

    highest = []
    if results :
        highest_doc, _ = max(results, key=lambda x: x[1])
        highest.append(highest_doc.page_content)

    return highest