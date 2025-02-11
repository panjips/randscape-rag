# Simple RAG [IN DEVELOPMENT]

This project is a **Retrieval-Augmented Generation (RAG) Chatbot** built using **FastAPI**. It processes PDF documents, stores them in a vector database using embeddings, and provides a chatbot interface to retrieve answers based on user queries.

## Features

- **PDF Ingestion**: Loads and splits PDF documents into chunks.
- **Embeddings Generation**: Uses **OllamaEmbeddings** with to generate vector embeddings.
- **Vector Storage**: Stores processed embeddings in **ChromaDB**.
- **FastAPI Backend**: Provides a REST API to query the chatbot.
- **Automatic Database Creation**: Runs ingestion if no database exists.

## Folder Structure

```
rag/
├── app/
│   ├── __init__.py  # Initializes the app module
│   ├── main.py      # FastAPI main entry point
│   ├── models.py    # Pydantic models for request and response
│   └── config.py    # Configuration settings
├── utils/
│   ├── __init__.py  # Initializes the utils module
│   ├── ingest.py    # Document ingestion and processing
│   └── query.py     # Retrieval logic for answering queries
├── datas/           # Folder containing PDF documents
├── db/              # Vector database storage (auto-created if missing)
│
├── requirements.txt # List of package
└── README.md        # Project documentation
```

## How It Works

1. **Ingestion Phase**

   - Loads the PDF files from `datas/`
   - Splits text into smaller chunks
   - Generates embeddings and stores them in ChromaDB

2. **Query Phase**
   - Accepts a user question
   - Retrieves the most relevant chunks using vector search
   - Returns the most relevant answer(s)

## Notes

- If the `db/` folder is missing, the script will **automatically run ingestion** before serving queries.
- You can modify `config.py` to customize settings like chunk size, overlap, or model parameters.
