# 01_agent_fundamentals

Before building complex multi-agent teams or using heavy frameworks like LangGraph, you need to understand the bedrock mechanics of what makes an LLM an agent rather than a standard chatbot.

## 1. The Core Architectural Difference

Stateless Chatbot: Input $\rightarrow$ Prompt $\rightarrow$ Output (Linear, one-shot).

AI Agent: Input $\rightarrow$ LLM Reasoning Engine $\rightarrow$ Tool Execution $\rightarrow$ Environmental Feedback (Observation) $\rightarrow$ Memory Append $\rightarrow$ Next Reasoning Step (Iterative loop).

## 2. The Anatomy of the Scratchpad (Agent State)

An agent's scratchpad is its short-term working memory during execution. It holds the chronological chain of:

$$\text{Thought}_1 \rightarrow \text{Action}_1 \rightarrow \text{Observation}_1 \rightarrow \text{Thought}_2 \rightarrow \text{Action}_2 \rightarrow \text{Observation}_2 \dots$$

## Production Implementation: 
01_agent_fundamentals/react_loop_from_scratch.py
Here is a robust, well-documented script representing the contents of the 01_agent_fundamentals/ folder. It implements a clean ReAct loop with error handling and iteration limits.