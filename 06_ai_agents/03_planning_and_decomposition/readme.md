# planning and decomposition

Standard reactive agents (like the basic ReAct loop) make decisions step-by-step without a global roadmap. When faced with complex, multi-hop tasks—such as financial forecasting, strategic code refactoring, or multi-step logistical scheduling—step-by-step reaction often leads to dead ends or logical contradictions.

Folder 3 covers advanced cognitive patterns that give agents foresight: Plan-and-Solve, Task Decomposition, and Tree-of-Thought (ToT) Search.

## 1. Core Planning Paradigms
### A. Plan-and-Solve (Two-Phase Execution)
Instead of blending planning and execution together (like standard Chain-of-Thought), Plan-and-Solve explicitly separates the process into two phases:

**The Planning Phase:** The agent analyzes the objective and outputs a structured sequence of distinct sub-goals before touching any tools or executing code.

**The Solving Phase:** The agent systematically steps through the plan, updating intermediate variables and checking dependencies.

### B. Tree-of-Thought (ToT) Exploration
When a single linear plan isn't enough, Tree-of-Thought empowers the agent to explore multiple reasoning paths in parallel:

**Branching:** At any step, the model generates multiple potential "thoughts" or action strategies.

**Evaluation:** A heuristic or self-evaluation judge scores each branch (e.g., Promising, Dead-end, Optimal).

**Backtracking:** If a branch fails or hits a contradiction, the agent prunes that branch, backtracks to a previous node, and explores an alternative path (akin to human System 2 slow thinking).