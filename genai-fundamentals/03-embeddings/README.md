# 03 — Embeddings

Purpose
Teach how to compute and use dense vector representations for semantic search, clustering, and downstream tasks.

Learning objectives
- Explain vector embeddings and cosine similarity.
- Build a small embedding index and perform nearest-neighbor retrieval.
- Understand trade-offs between embedding models and sizes.

Key concepts
- Embedding models (instruction-tuned vs general-purpose).
- Indexing options: FAISS, pgvector, Redis Vector, Milvus.
- Reranking with cross-encoders vs bi-encoders.

Exercises
- Compute embeddings for a set of documents and implement a simple search API.
- Compare retrieval results using different embedding models.

Starter code pointers
- Example notebook using `sentence-transformers` or provider SDK to compute embeddings and FAISS for indexing.

References
- Embeddings tutorials from model providers and FAISS documentation.
