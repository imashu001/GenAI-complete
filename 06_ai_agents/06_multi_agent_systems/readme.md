# Overview: Multi-Agent Systems (MAS)
A Multi-Agent System is a framework where multiple autonomous AI agents—each equipped with specialized prompts, tools, or roles—collaborate, communicate, or compete to solve complex tasks that are difficult for a single LLM to handle alone.

## Core Architecture Components
Specialized Agents: Breaking down monolithic tasks into modular roles (e.g., Planner, Researcher, Coder, Judge, Summarizer).

Orchestration / Flow Control: How agents interact (e.g., Sequential pipelines, Hierarchical supervision, Feedback loops).

State Management & Shared Memory: Ensuring agents have access to context, intermediate variables, and retrieved artifacts without losing information.

Standard Workflow Example

[User Request] 
       │
       ▼
[Planner Agent] ──(Breaks into Subtasks)──► [Research Agent]
                                                 │
                                           (Pass/Fail Loop)
                                                 │
                                                 ▼
[Summarizer/Builder] ◄──────────────────── [Judge Agent]
       │
       ▼
 [Final Output]