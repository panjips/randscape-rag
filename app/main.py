import uvicorn
import os   
import sys  
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from fastapi import FastAPI
from models import QueryRequest, QueryResponse
from utils import retriver, process_document

app = FastAPI(title="Simple RAG Chatbot", version="0.1")

DB_PATH = os.getcwd() + "/db"
if not os.path.exists(DB_PATH) or not os.listdir(DB_PATH):
    process_document()

@app.get("/")
def read_root():
    return {"message: Welcome to the Simple RAG Chatbot"}

@app.post("/query/", response_model=QueryResponse)
def query_chatbot(request: QueryRequest):
    question = request.question
    results = retriver(question)
    return QueryResponse(answer=results)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)