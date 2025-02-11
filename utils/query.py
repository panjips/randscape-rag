import os

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

DB_PATH = os.getcwd() + "/db"

def get_vector_store():
    embeddings = OllamaEmbeddings(model="deepseek-r1:1.5b", base_url="http://localhost:11434")
    vectorStore = Chroma(collection_name="example", embedding_function=embeddings, persist_directory=DB_PATH)
    
    return vectorStore

def retriver(query):
    vectorStore = get_vector_store()
    results = vectorStore.similarity_search(query, k=1)

    return [doc.page_content for doc in results]