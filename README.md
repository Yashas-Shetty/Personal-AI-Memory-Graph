# 🧠 Personal AI Memory Graph

A powerful hybrid long-term memory system for AI, combining **Semantic Vector Recall** (ChromaDB) with **Structured Graph Reasoning** (Neo4j).

---

## 🏗️ Project Structure

This repository is split into two main sections:

- **[backend/](./backend)**: The FastAPI server, LLM logic, and database orchestration.
- **[frontend/](./frontend)**: The Next.js user interface (Planned/In Development).

---

## 🚀 Quick Start (Backend)

1.  **Navigate to backend**: `cd backend`
2.  **Setup Environment**: `python -m venv venv` and `source venv/bin/activate`
3.  **Install Dependencies**: `pip install -r requirements.txt`
4.  **Configure**: Create `.env` from `.env.example`
5.  **Run**: `python app/main.py`

---

## ✨ Features
- **Semantic Ingestion**: Local vectorization via `fastembed`.
- **Knowledge Graph**: Entity extraction and Neo4j mapping via Gemini.
- **Reasoning API**: Context-aware answers to natural language queries.
