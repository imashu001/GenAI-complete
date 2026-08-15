"""
pydantic_function_handler.py
Part of 02_tools_and_function_calling/
Demonstrates type-safe tool definition using Pydantic, handling tool calls,
and executing the complete OpenAI-style tool execution lifecycle.
"""

import os
import json
from typing import List, Dict, Any, Type
from pydantic import BaseModel, Field

# --- 1. Define Tool Schemas using Pydantic ---
class GetOrderStatusSchema(BaseModel):
    """Returns shipping status for a customer order. Use when a customer asks about delivery, tracking, or order location."""
    order_id: str = Field(description="The customer order ID, e.g., 'ORD-98765'")

class CalculateShippingCostSchema(BaseModel):
    """Calculates estimated shipping cost based on package weight and destination country."""
    weight_kg: float = Field(description="Weight of the package in kilograms")
    destination: str = Field(description="Destination country code, e.g., 'DE', 'US', 'JP'")

# --- 2. Implement the Backend Tool Functions ---
def execute_get_order_status(order_id: str) -> str:
    """Actual database lookup function."""
    print(f"      [Database Execution] Querying order status for: {order_id}")
    # Simulated backend database result
    return json.dumps({
        "order_id": order_id,
        "status": "In Transit",
        "estimated_delivery": "2026-08-20",
        carrier: "GlobalExpress"
    })

def execute_calculate_shipping_cost(weight_kg: float, destination: str) -> str:
    """Actual shipping calculation function."""
    print(f"      [API Execution] Calculating shipping for {weight_kg}kg to {destination}")
    cost = round(weight_kg * 4.5 + (15.0 if destination != "US" else 5.0), 2)
    return json.dumps({"weight_kg": weight_kg, "destination": destination, "estimated_cost_usd": cost})

# Mapping tool names to executable python functions
TOOL_REGISTRY = {
    "GetOrderStatusSchema": execute_get_order_status,
    "CalculateShippingCostSchema": execute_calculate_shipping_cost
}

class ToolExecutionOrchestrator:
    def __init__(self):
        print("Initializing Tool Execution Orchestrator...")

    def simulate_llm_tool_selection(self, user_prompt: str) -> Dict[str, Any]:
        """
        Simulates the LLM's decision to call a specific tool based on the prompt.
        In production with the OpenAI SDK, this comes from response.choices[0].message.tool_calls.
        """
        print(f"\n📨 [User Prompt]: '{user_prompt}'")
        
        if "order" in user_prompt.lower() or "ord-" in user_prompt.lower():
            return {
                "tool_name": "GetOrderStatusSchema",
                "tool_arguments": {"order_id": "ORD-98765"},
                "call_id": "call_abc123"
            }
        elif "shipping cost" in user_prompt.lower():
            return {
                "tool_name": "CalculateShippingCostSchema",
                "tool_arguments": {"weight_kg": 3.5, "destination": "DE"},
                "call_id": "call_xyz789"
            }
        else:
            return {"tool_name": None, "tool_arguments": {}, "call_id": None}

    def run_lifecycle(self, user_prompt: str):
        # Step 1 & 2: User prompt + schema evaluation
        tool_call = self.simulate_llm_tool_selection(user_prompt)
        
        if not tool_call["tool_name"]:
            print("💬 [LLM Response]: No tool needed. Answering directly.")
            return "Hello! How can I assist you with your orders or shipping today?"

        # Step 3: Model returns tool call request
        tool_name = tool_call["tool_name"]
        arguments = tool_call["tool_arguments"]
        print(f"🤖 [LLM Tool Decision]: Model requested tool '{tool_name}' with args: {arguments}")

        # Step 4: Backend Execution
        if tool_name in TOOL_REGISTRY:
            executable_func = TOOL_REGISTRY[tool_name]
            tool_output_json = executable_func(**arguments)
            print(f"👀 [Tool Output]: {tool_output_json}")
            
            # Step 5: Final Synthesis (Mocking second LLM turn with tool output)
            print("🔄 [Second LLM Pass]: Feeding tool output back to model...")
            if tool_name == "GetOrderStatusSchema":
                final_response = f"Your order ORD-98765 is currently In Transit and scheduled to arrive by August 20, 2026."
            else:
                final_response = f"The estimated shipping cost for your 3.5kg package to Germany is $30.75."
                
            print(f"🎉 [Final Answer]: {final_response}")
            return final_response
        else:
            raise ValueError(f"Tool {tool_name} is not registered in backend handlers.")

if __name__ == "__main__":
    orchestrator = ToolExecutionOrchestrator()
    
    # Test Scenario 1: Order tracking query
    orchestrator.run_lifecycle("Can you check the tracking status for order ORD-98765?")
    
    # Test Scenario 2: Shipping cost calculation query
    orchestrator.run_lifecycle("How much will it cost to ship a 3.5kg package to Germany?")