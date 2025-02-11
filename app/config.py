import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FILE_PATH = os.getcwd() + "/datas/"
    DB_PATH = os.getcwd() + "/db"

    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "deepseek-r1:1.5b")
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    CHUNK_SIZE = os.getenv("CHUNK_SIZE", 1000)
    CHUNK_OVERLAP = os.getenv("CHUNK_OVERLAP", 200)

    CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "exampleCollection")