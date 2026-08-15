Linear chains and basic ReAct loops break down when applications require complex business logic, cyclic dependencies, parallel fan-out, and reliable state persistence. Folder 5 explores Agent Workflows & State Machine Orchestration (principally powered by libraries like LangGraph), shifting the paradigm from rigid sequential prompts to stateful, graph-driven execution flowcharts.

## 1. The Core Primitives of State Graph Workflows
Modern production agent workflows model execution as a directed graph consisting of four essential primitives:

**State:** A shared schema (e.g., a TypedDict or Pydantic model) that acts as the agent's central working memory, updated incrementally by each node.

**Nodes:** Python functions that perform discrete units of work (e.g., calling an LLM, executing a tool, or validating data) and return partial state updates.

**Edges (Unconditional & Conditional):** Deterministic or routing transitions that define how control flows from one node to the next based on the current state.

**Checkpointers:** Persistence layers (such as SQLite or PostgreSQL) that automatically save the state after every node transition, enabling fault recovery, long-running tasks, and time-travel debugging.

## 2. Production Code Implementation (05_agent_workflows/state_graph_workflow.py)
Here is a clean, production-grade Python script demonstrating how to define a cyclic state machine workflow with conditional routing and state reduction: