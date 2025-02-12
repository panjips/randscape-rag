import os
import glob

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from app.config import Config

def process_document():
    files = glob.glob(os.path.join(Config.FILE_PATH, "*.pdf"))
    documents = []

    for file in files:
        loader = PyPDFLoader(file)
        document = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            separators= ["\n", ".", "!", "?", ";"],
            chunk_size=int(Config.CHUNK_SIZE),
            chunk_overlap=int(Config.CHUNK_OVERLAP)
        )

        text_chunks = splitter.split_documents(document)
        documents.extend(text_chunks)

    embeddings = OllamaEmbeddings(model=Config.OLLAMA_MODEL, base_url=Config.OLLAMA_BASE_URL)

    vectorStore = Chroma(collection_name=Config.CHROMA_COLLECTION, embedding_function=embeddings, persist_directory=Config.DB_PATH)
    vectorStore.add_documents(documents)