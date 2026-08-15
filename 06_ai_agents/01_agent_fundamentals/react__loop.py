"""
react_loop_from_scratch.py
Part of 01_agent_fundamentals/
Demonstrates the underlying Thought-Action-Observation loop of an autonomous agent
using pure Python and structured dictionary state tracking.
"""

from typing import List, Dict, Any
import json

class AgentScratchpad:
    """Manages the chronological history (scratchpad) of an agent's execution."""
    def __init__(self):
        self.steps: List[Dict[str, str]] = []

    def add_step(self, thought: str, action: str, observation: str):
        self.steps.append({
            "thought": thought,
            "action": action,
            "observation": observation
        })

    def get_formatted_history(self) -> str:
        history_str = ""
        for idx, step in enumerate(self.steps, 1):
            history_str += f"Step {idx}:\n  Thought: {step['thought']}\n  Action: {step['action']}\n  Observation: {step['observation']}\n"
        return history_str

class FoundationalReActAgent:
    def __init__(self, max_iterations: int = 5):
        self.scratchpad = AgentScratchpad()
        self.max_iterations = max_iterations

    def _simulated_llm_brain(self, goal: str, history: AgentScratchpad) -> Dict[str, Any]:
        """
        Simulates the LLM decision-making process based on current goal and scratchpad history.
        In a live app, this is where you call client.chat.completions.create() with tool schemas.
        """
        step_count = len(history.steps)
        
        if step_count == 0:
            return {
                "type": "action",
                "thought": "The user wants stock data and currency conversion. I should first check the stock price of Apple.",
                "tool": "get_stock_price",
                "tool_input": "AAPL"
            }
        elif step_count == 1:
            return {
                "type": "action",
                "thought": "I have Apple's stock price at $180. Now I need to check the current USD to EUR exchange rate.",
                "tool": "get_exchange_rate",
                "tool_input": "USD_EUR"
            }
        else:
            return {
                "type": "finish",
                "thought": "I have gathered all required data points. I can now present the final calculated response.",
                "output": "Apple (AAPL) is trading at $180, and the USD to EUR exchange rate is 0.92."
            }

    def _execute_tool(self, tool_name: str, tool_input: str) -> str:
        """Executes the external environment tool based on agent's action request."""
        print(f"   🔧 [Environment Tool Execution] Calling '{tool_name}' with input: '{tool_input}'")
        
        if tool_name == "get_stock_price":
            if tool_input.upper() == "AAPL":
                return "AAPL stock price is $180.50 USD."
            return "Stock ticker not found."
        elif tool_name == "get_exchange_rate":
            if tool_input.upper() == "USD_EUR":
                return "1 USD = 0.92 EUR."
            return "Currency pair not found."
        
        return f"Error: Tool '{tool_name}' not recognized."

    def run(self, goal: str) -> str:
        print(f"\n🚀 [Agent Initialized] Goal: '{goal}'")
        
        for iteration in range(1, self.max_iterations + 1):
            print(f"\n--- Loop Iteration {iteration} ---")
            
            # 1. Reason (LLM Decision Phase)
            decision = self._simulated_llm_brain(goal, self.scratchpad)
            thought = decision.get("thought", "")
            print(f"🧠 [Thought]: {thought}")
            
            # 2. Check if agent decided to finish
            if decision.get("type") == "finish":
                final_answer = decision.get("output", "")
                print(f"🎉 [Goal Achieved]: {final_answer}")
                return final_answer
            
            # 3. Act (Execute Tool)
            tool_name = decision.get("tool")
            tool_input = decision.get("tool_input")
            action_str = f"{tool_name}({tool_input})"
            
            # 4. Observe (Environment Feedback)
            observation = self._execute_tool(tool_name, tool_input)
            print(f"👀 [Observation]: {observation}")
            
            # 5. Record to Scratchpad Memory
            self.scratchpad.add_step(thought=thought, action=action_str, observation=observation)

        raise TimeoutError("Agent exceeded max iterations without completing the goal.")

if __name__ == "__main__":
    agent = FoundationalReActAgent()
    agent.run("Find the stock price of AAPL and convert it to Euros.")