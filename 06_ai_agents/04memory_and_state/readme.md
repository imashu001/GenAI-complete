# memory and state

An agent without memory is stateless—it forgets every prior turn, tool execution, and user preference the moment the HTTP request terminates. To build production-grade, context-aware agents, you must implement a robust Memory & State Architecture.

## 1. The Four Pillars of Agent Memory
Production systems separate memory into distinct architectural tiers based on scope, lifespan, and retrieval mechanics:

### Short-Term Memory (Working Memory / Checkpointing):

Manages immediate conversational state and scratchpad history within a single running thread or session.

**Implementation:** In-memory checkpointers (MemorySaver) for development, or durable database checkpointers (PostgresSaver, RedisSaver) for production crash recovery.

### Episodic Memory:

Records specific past events, user interactions, and outcomes across distinct sessions (e.g., "What did the user ask me last Tuesday?").

**Implementation:** Logged event stores with timestamp metadata and recency weights.

### Semantic Memory (Long-Term Factual):

Stores persistent facts, user preferences, and general knowledge learned over time.

**Implementation:** Cross-thread namespace stores (InMemoryStore / RedisStore) combined with vector embeddings for semantic retrieval.

## Procedural Memory:

Stores learned rules, guidelines, and effective tool-calling workflows that optimize future agent actions.

## 2. Production Code Implementation (04_memory_and_state/agent_memory_manager.py)
Here is a clean, production-grade Python script demonstrating how to manage short-term thread states and long-term semantic user preferences using structured namespaces: