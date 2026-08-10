# GenAI-complete

An organized, study-focused roadmap for learning Generative AI and related engineering topics.

### Table of Contents
1. Overview
2. How to use this repo
3. Suggested study path
4. Detailed roadmap
    - 01. GenAI Fundamentals
    - 02. Prompt Engineering
    - 03. LLM Application Development
    - 04. Retrieval-Augmented Generation (RAG)
    - 05. AI Agents
    - 06. AI Frameworks
    - 07. AI Data Layer
    - 08. AI Engineering
    - 09. AI Security
    - 10. Production & Cloud
    - 11. Senior-Level
5. Learning tips & exercises
6. Contributing
7. License

## Overview
This repository collects a comprehensive roadmap for studying modern Generative AI systems. Each top-level folder corresponds to a topic area with notes, references, code snippets, and exercises where applicable. Use the roadmap to plan study sessions, build projects, and prepare for interviews.

## How to use this repo
- Start at the section matching your current skill level (Fundamentals → Advanced).
- Follow the suggested study path (next section) if you're new to the field.
- For each topic folder: read theory, run any included examples, then complete the exercises or mini-projects.
- Add notes, links, and local examples as you learn; create PRs to improve the content.

### Suggested study path
1. GenAI Fundamentals — get solid on tokens, attention, transformers, embeddings, and model APIs.
2. Prompt Engineering — learn how to instruct models, structure outputs, and use chains of thought.
3. LLM Application Development — practice using model APIs, local models, and streaming/ multimodal features.
4. RAG — learn document processing, chunking, embeddings, and vector search.
5. AI Agents & Frameworks — implement simple agents, explore LangChain/LlamaIndex patterns.
6. Data Layer & Engineering — focus on vector DBs, pgvector/Redis, observability, and cost/latency optimizations.
7. Production & Security — containerize, deploy, secure, and scale your systems.
8. Senior topics — system design, trade-offs, and interview preparation.

### Detailed roadmap

### 01. GenAI Fundamentals
- Goal: Understand the core building blocks of modern LLMs.
- Topics: tokens & tokenization, embeddings, transformer architecture, self-attention, context windows, sampling methods, model APIs and limits.
- Study suggestions: implement a toy tokenizer, visualize attention maps, compute embeddings with an SDK, compare sampling strategies.

### 02. Prompt Engineering
- Goal: Learn to craft prompts for reliable/robust outputs.
- Topics: zero-shot / few-shot prompting, chain-of-thought, structured outputs (JSON), function calling, prompt templates, evaluation metrics.
- Study suggestions: build prompt templates, create a small prompt-evaluation harness, test with multiple models.

### 03. LLM Application Development
- Goal: Build applications that use LLMs safely and efficiently.
- Topics: OpenAI-compatible APIs, alternative APIs (Anthropic, Gemini), running local models, streaming responses, multimodal inputs, tool/function calling, model routing and fallbacks.
- Study suggestions: build a simple chat app with streaming and a tool-call handler.

### 04. Retrieval-Augmented Generation (RAG)
- Goal: Combine retrieval systems with LLMs for grounded responses.
- Topics: document ingestion, parsing, chunking, embeddings, vector databases, retrieval strategies, hybrid search, reranking, metadata filtering, evaluation and pitfalls (hallucination, freshness, poisoning).
- Study suggestions: create a small RAG pipeline using local documents and a vector DB (pgvector or FAISS), add reranking and evaluate quality.

### 05. AI Agents
- Goal: Implement agents that plan, call tools, and maintain state.
- Topics: agent patterns, tool interfaces, planning & memory, state management, multi-agent coordination, Model Control Plane (MCP), human-in-loop designs.
- Study suggestions: implement a planner + executor that performs multi-step tasks using a model and tool mocks.

### 06. AI Frameworks
- Goal: Learn popular frameworks and when to use them.
- Topics: LangChain, LangGraph, LlamaIndex, model SDKs, MCP/agent SDKs; compare trade-offs and integration patterns.
- Study suggestions: port a small RAG or agent flow between two frameworks to compare ergonomics.

### 07. AI Data Layer
- Goal: Build reliable storage and retrieval for embeddings and metadata.
- Topics: PostgreSQL + pgvector, Redis, hosted vector DBs, search engines, data pipelines, indexing, schema design for embeddings and metadata.
- Study suggestions: design a metadata schema for documents and store/retrieve using pgvector and SQL filters.

### 08. AI Engineering
- Goal: Operate AI systems with quality and cost-efficiency.
- Topics: evaluation metrics and workflows, observability and tracing, prompt/version management, caching, latency and cost optimization, reliability patterns.
- Study suggestions: add logging/tracing to an LLM app, measure latency/cost for different model choices, and add caching.

### 09. AI Security
- Goal: Protect systems from misuse and data leakage.
- Topics: prompt injection defenses, jailbreak mitigation, data privacy, RAG poisoning detection, tool abuse prevention, excessive agent autonomy, tenant isolation.
- Study suggestions: simulate prompt-injection attacks and implement input sanitization and output filtering.

### 10. Production & Cloud
- Goal: Deploy and scale AI services.
- Topics: Docker, CI/CD, cloud integration (AWS/Azure/GCP), Kubernetes, secrets management, autoscaling, observability in production.
- Study suggestions: containerize a minimal RAG service and deploy it to a test cluster or cloud run environment.

### 11. Senior-Level
- Goal: Prepare for system design and leadership-level trade-offs.
- Topics: AI system design patterns, RAG system design at scale, agent orchestration, LLM gateway concepts, AI SaaS architecture, architecture trade-offs, interview prep.
- Study suggestions: design a high-level architecture for a multi-tenant RAG SaaS and draft a cost/latency/security trade-off document.

## Learning tips & exercises
- Cycle of study: read theory → small implementation → evaluate → extend into a mini-project.
- Keep a learning journal: store notes and short summaries in the repo for future reference.
- Build progressively: every major topic should conclude with a small project (chatbot, RAG search, agent demo).
- Peer review: request feedback via PRs and discuss alternative approaches.
- Timebox experiments: run short experiments (1–3 days) to compare models, embeddings, or retrieval setups.

## Contributing
- Want to improve this roadmap? Contributions welcome.
- How to contribute: fork the repo, add content under the appropriate folder, and submit a PR with explanations and sources.
- Guidelines: prefer concise explanations, include links to references, and add runnable examples where possible.

## License
This repository is intended as an educational resource. Include your preferred license file if you want to make reuse terms explicit.

---