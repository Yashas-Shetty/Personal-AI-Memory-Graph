# 🧠 Personal AI Memory Graph

A powerful hybrid long-term memory system for AI. It combines **Semantic Vector Recall** (ChromaDB) with **Structured Graph Reasoning** (Neo4j), all orchestrated by **Google Gemini**.

---

## 🏗️ Architecture

The system follows a modular 6-layer architecture:

1.  **API Layer**: FastAPI endpoints for ingestion, querying, and memory management.
2.  **LLM Layer**: High-level intelligence using Gemini for extraction, summarization, and reasoning.
3.  **Memory Layer**: Orchestrates the storage and retrieval flows between vector and graph planes.
4.  **Database Layer**: 
    - **Vector (ChromaDB)**: Handles "fuzzy" semantic searches via local embeddings.
    - **Graph (Neo4j)**: Handles structured "hard" facts and relationships.
5.  **Services Layer**: Business logic for multi-hop reasoning and context merging.
6.  **Utilities Layer**: Helpers for text normalization, time-stamping, and logging.

---

## ✨ Features

- **Semantic Ingestion**: Automatically vectorizes text using `fastembed` for local, lightning-fast semantic recall.
- **Knowledge Graph Extraction**: Extracts entities and relationships from raw text using Gemini and maps them into Neo4j.
- **Hybrid Retrieval**: Queries both databases simultaneously to provide a comprehensive "surrogate brain" context.
- **Summarization**: Long memories are automatically condensed into concise reflections before storage.
- **Reasoning API**: Ask natural language questions about your collective memories.
- **Admin Tools**: Built-in endpoints for database statistics and hard resets.

---

## 🚀 Setup & Installation

### 1. Prerequisites
- Python 3.10+
- A [Neo4j Aura](https://neo4j.com/cloud/aura/) account (Free tier is fine).
- A [Google Gemini API Key](https://aistudio.google.com/).

### 2. Installation
```bash
# Setup Virtual Environment
python -m venv venv
venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file from `.env.example`:
```env
# Gemini
GEMINI_API_KEY=your_gemini_api_key

# Neo4j
NEO4J_URI=neo4j+s://<your-instance-id>.databases.neo4j.io
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password

# App
CHROMA_PERSIST_DIRECTORY=./data/chroma
```

---

## 🔧 Usage

### Running the App
```bash
python app/main.py
```
Visit `http://localhost:8000/docs` to see the interactive Swagger UI.

### Core Endpoints
- **POST `/ingest`**: Feed new information into the system.
- **POST `/query/reason`**: Ask a question about your stored memories.
- **GET `/memory/stats`**: Check your current memory count.
- **POST `/memory/clear`**: Wipe the system for a fresh start.

---

## 📂 Project Structure
```text
app/
├── api/            # API Route definitions
├── core/           # Config and Constants
├── llm/            # Gemini Clients, Prompts, and Extraction
├── memory/         # Database Clients and Ingest/Retrieve Pipelines
├── services/       # High-level reasoning logic
└── utils/          # Text and Time helpers
```