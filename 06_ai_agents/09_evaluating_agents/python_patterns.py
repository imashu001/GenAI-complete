import json
from typing import List, Dict, Any

# --- 1. Define a Golden Test Case ---
GOLDEN_TEST_CASE = {
    "user_prompt": "What is the weather in Tokyo, and convert that temperature to Fahrenheit?",
    "expected_tools_called": ["get_weather", "convert_temperature"],
    "expected_final_keywords": ["Tokyo", "Fahrenheit"]
}

# --- 2. Simulate an Agent Execution Run (Trajectory) ---
def mock_agent_execution(user_prompt: str) -> Dict[str, Any]:
    # Simulated agent trace
    trajectory = [
        {"step": 1, "thought": "I need to check the weather in Tokyo.", "tool": "get_weather", "args": {"location": "Tokyo"}},
        {"step": 2, "thought": "Now I need to convert Celsius to Fahrenheit.", "tool": "convert_temperature", "args": {"temp_c": 22}},
    ]
    final_output = "The weather in Tokyo is 22°C, which is 71.6°F."
    return {
        "trajectory": trajectory,
        "final_output": final_output
    }

# --- 3. Build the Evaluation Harness ---
def evaluate_agent_run(test_case: dict, agent_run: dict) -> dict:
    actual_trajectory = agent_run["trajectory"]
    
    # Metric 1: Tool Selection Accuracy
    actual_tools = [step["tool"] for step in actual_trajectory]
    expected_tools = test_case["expected_tools_called"]
    tool_match = actual_tools == expected_tools
    
    # Metric 2: Argument Validity Check (Example: check if location is present)
    args_valid = all("location" in step["args"] or "temp_c" in step["args"] for step in actual_trajectory)
    
    # Metric 3: Output Keyword Match
    final_output = agent_run["final_output"]
    keywords_matched = all(kw.lower() in final_output.lower() for kw in test_case["expected_final_keywords"])
    
    # Overall Score Calculation
    score = sum([1.0 if tool_match else 0.0, 1.0 if args_valid else 0.0, 1.0 if keywords_matched else 0.0]) / 3.0
    
    return {
        "passed": score == 1.0,
        "score": round(score, 2),
        "tool_match": tool_match,
        "args_valid": args_valid,
        "keywords_matched": keywords_matched
    }

# --- Run Evaluation ---
if __name__ == "__main__":
    agent_result = mock_agent_execution(GOLDEN_TEST_CASE["user_prompt"])
    eval_results = evaluate_agent_run(GOLDEN_TEST_CASE, agent_result)
    
    print("--- Agent Evaluation Report ---")
    print(json.dumps(eval_results, indent=2))