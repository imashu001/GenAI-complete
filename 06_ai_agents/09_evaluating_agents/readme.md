# Module 09: Evaluating Agents (Scoring Non-Deterministic Trajectories and Tool Calls)
Welcome to Module 09: Evaluating Agents. Moving from standard LLM applications (where you evaluate a single prompt-response pair) to autonomous agents introduces a massive engineering challenge: non-determinism and multi-step trajectories.

When an agent can choose different tools, make varying numbers of reasoning steps, and self-correct along the way, traditional unit testing (assert output == expected_string) completely breaks down.

Suggested Course Module Structure

[Module 09: Evaluating Agents]
 ├── 01_the_agent_evaluation_challenge.md (Why traditional software testing and LLM evals fail)
 ├── 02_trajectory_and_tool_evals.md      (Evaluating intermediate steps, tool selection, and arguments)
 ├── 03_llm_as_a_judge_patterns.md        (Building robust rubrics, self-consistency, and grading agents)
 ├── 04_hands_on_eval_harness.py          (Hands-on: Building a custom evaluation harness with Phoenix/LangSmith concepts)
 └── 05_ci_cd_for_agents.md               (Regression testing, golden datasets, and continuous improvement)

Core Concepts to Teach

## 1. Why Agent Evaluation is Hard

Non-Determinism: Two runs with the exact same user prompt might take different paths (e.g., Tool A $\rightarrow$ Tool B vs. Tool C $\rightarrow$ Tool A) to arrive at the same correct answer—or fail differently.

Compounding Errors: A small mistake in Step 1 (e.g., retrieving the wrong document chunk) derails all subsequent steps in a 10-step agent loop.

Statefulness: Evaluating agents requires inspecting the entire journey (the trajectory), not just the final output string.

## 2. The Three Layers of Agent EvaluationTo thoroughly test an agent, you must evaluate three distinct layers:

Tool Selection & Argument Evals: Did the agent pick the correct tool for the subtask? Did it pass valid JSON arguments into the tool schema?

Trajectory / Path Evals: Did the agent follow an efficient sequence of steps, or did it get stuck in infinite reasoning loops?

Outcome / Final Output Evals: Is the final response factually correct, safe, and aligned with user intent?

Hands-On Python Pattern: Evaluating Tool Selection & TrajectoriesBelow is a hands-on Python example demonstrating how to build a custom evaluation harness that scores an agent's trajectory, tool selection accuracy, and final outcome against a "golden test case."

refer to python pattererns file in same folder / level

### Pedagogical Takeaways for Course Design
Move Beyond Unit Testing: Teach students that asserting exact string matches is useless for LLM agents. Instead, teach semantic evaluation (using LLM-as-a-judge with structured rubrics) and structural evaluation (checking tool schemas and argument types).

The Importance of Tracing Tools: Highlight how production frameworks (like Arize Phoenix, LangSmith, or OpenInference) capture intermediate spans so developers can replay failing agent trajectories step-by-step.

Golden Datasets: Emphasize that building an agent without a growing regression test