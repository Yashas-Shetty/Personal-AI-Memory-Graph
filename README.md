# Personal AI Memory Graph

A hybrid long-term memory system for AI, combining semantic vector recall with structured graph reasoning.

## 🧱 Architecture

The system is organized into several layers:
- **API**: Thin FastAPI layer for ingestion and querying.
- **Memory**: Orchestration of Vector (ChromaDB) and Graph (Neo4j) storage.
- **LLM**: Intelligence layer using Google Gemini for entity extraction and reflection.
- **Services**: High-level reasoning and recommendation logic.

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Activate virtual environment
venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration
Create a `.env` file based on `.env.example`:
```env
GEMINI_API_KEY=your_key_here
```

### 3. Run the App
```bash
python app/main.py
```

## 📂 Project Structure
(See documentation for full tree)