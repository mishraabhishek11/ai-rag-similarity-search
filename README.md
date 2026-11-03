# 🔎 AI RAG Similarity Search

A **Python Retrieval-Augmented Generation (RAG)** pipeline that splits a document into chunks, embeds them into a persistent ChromaDB vector store, retrieves the best matches with hybrid (semantic + keyword) scoring, re-ranks them with an LLM, and generates an answer grounded only in the retrieved context.

This project demonstrates a RAG system built from small, separate parts: chunking, embeddings, vector storage, hybrid retrieval, LLM re-ranking, answer generation and retrieval evaluation.

---

## 🚀 Features

### ✂ Chunking

- Splits text into word-based chunks (200 words, 50-word overlap)
- Each chunk keeps its `source` and `chunk_id`

### 🧬 Embeddings & Vector Store

- Embeddings come from any OpenAI-compatible endpoint
- Chunks are stored in a persistent ChromaDB collection (`./chroma_db`)
- Chunks are upserted by `<source>_<chunk_id>`, so re-running does not duplicate them

### 🔍 Hybrid Retrieval

- Semantic score from ChromaDB vector distance: `1 / (1 + distance)`
- Keyword score: share of query words found in the chunk
- Combined score: `0.7 × semantic + 0.3 × keyword`
- `retriever.py` also provides in-memory `semantic_search` and `hybrid_search` using cosine similarity (NumPy)

### 🥇 LLM Re-ranking

- Each candidate is scored 0–100 for relevance by the chat model (temperature 0)
- Non-numeric replies score 0
- The top 3 chunks are passed on to answer generation

### 💬 Grounded Answer Generation

- The model must answer only from the retrieved context
- If the answer is not in the context, it says the information is not available

### 📏 Evaluation

- `evaluate_retrieval` checks whether the expected chunk is among the retrieved chunks

---

## 🛠 Tech Stack

### Core

- Python 3

### Libraries

- OpenAI Python SDK (any OpenAI-compatible endpoint)
- ChromaDB (vector store)
- NumPy (cosine similarity)
- python-dotenv

### Storage

- ChromaDB persistent store (`chroma_db/`)

---

## 📂 Project Structure

```
ai-rag-similarity-search/
├─ Documents
│  └─ python.txt        # Sample knowledge base
├─ chroma_db            # Persistent vector store (generated)
├─ advanced_rag.py      # Builds the knowledge base and runs hybrid retrieval + re-ranking
├─ chroma_store.py      # ChromaDB collection: add and search
├─ chunker.py           # Word-based chunking with overlap
├─ embeddings.py        # Creates embeddings for text and chunks
├─ evaluation.py        # Retrieval evaluation helper
├─ generator.py         # Generates the grounded answer
├─ reranker.py          # LLM-based relevance re-ranking
├─ retriever.py         # Cosine similarity, keyword score, in-memory hybrid search
├─ main.py              # Entry point (interactive chat loop)
└─ .env                 # API configuration (not committed)
```

---

## ⚙ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/mishraabhishek11/ai-rag-similarity-search.git
cd ai-rag-similarity-search
```

### 2️⃣ Create and activate a virtual environment

```
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install openai chromadb numpy python-dotenv
```

### 4️⃣ Configure environment variables

Create a `.env` file in the project root:

```
BASE_URL=<OpenAI-compatible API base URL>
API_KEY=<your API key>
MODEL=<chat model name>
EMBEDDING_MODEL=<embedding model name>
```

### 5️⃣ Run the app

```
python main.py
```

---

## 🧑‍💻 Usage

```
Building RAG knowledge base...

Advanced RAG is ready.

You : What is Python?
```

1. Run `python main.py`
2. Wait for the knowledge base to be built
3. Type a question at the `You :` prompt
4. Read the ranked sources and the generated answer
5. Type `exit` or `quit` to stop

To use your own content, replace `Documents/python.txt` (or change `DOCUMENT_PATH` in `main.py`).

---

## 🔁 How It Works

1. `main.py` reads the document and calls `build_rag`
2. `chunker.py` splits the text into overlapping chunks
3. `embeddings.py` embeds every chunk, and `chroma_store.py` upserts them into ChromaDB
4. For each question, the query is embedded and ChromaDB returns the closest chunks
5. Each chunk gets a hybrid score (70% semantic, 30% keyword) and the candidates are sorted
6. `reranker.py` asks the LLM to score each candidate and keeps the top 3
7. `generator.py` answers the question using only those chunks

---

## 🎯 Learning Objectives

- Retrieval-Augmented Generation design
- Text chunking strategies
- Embeddings and similarity search
- Hybrid semantic and keyword retrieval
- LLM-based re-ranking
- Vector databases with ChromaDB

---

## 🔮 Future Enhancements

- Support for more document types (PDF, Markdown)
- Tests for chunking, retrieval and evaluation
- A `requirements.txt` to pin dependencies
- Batch embedding to speed up indexing
- Retrieval metrics over a labelled question set
- Web or chat interface

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch  
   git checkout -b feature/your-feature

3. Commit changes  
   git commit -m "feat(scope): your message"

4. Push changes  
   git push origin feature/your-feature

5. Open Pull Request

---

## 👨‍💻 Author

Abhishek Mishra  
GitHub: https://github.com/mishraabhishek11

---

## ⭐ Support

Give a ⭐ if you like this project!
