"""
state_graph_workflow.py
Part of 05_agent_workflows/
Demonstrates building an event-driven agent state graph with cyclic loops,
conditional routing, and state persistence using a StateGraph pattern.
"""

from typing import TypedDict, List, Annotated
import operator

# --- 1. Define the Shared State Schema ---
class WorkflowState(TypedDict):
    user_query: str
    messages: Annotated[List[str], operator.add] # Reducer concatenates message lists
    routing_decision: str
    review_status: str
    iteration_count: int

class AgentWorkflowOrchestrator:
    def __init__(self):
        print("Initializing Agent Workflow State Machine Engine...")

    def node_classifier(self, state: WorkflowState) -> dict:
        """Node 1: Analyzes the user query and determines the execution path."""
        query = state["user_query"]
        print(f"\n[Node: Classifier] Analyzing query: '{query}'")
        
        if "code" in query.lower() or "python" in query.lower():
            decision = "code_generator"
        else:
            decision = "general_responder"
            
        return {
            "routing_decision": decision,
            "messages": [f"Classified query route as: {decision}"]
        }

    def node_code_generator(self, state: WorkflowState) -> dict:
        """Node 2A: Handles technical coding tasks."""
        print("[Node: Code Generator] Writing Python solution snippet...")
        return {
            "messages": ["Generated Python code snippet successfully."],
            "review_status": "needs_review",
            "iteration_count": state.get("iteration_count", 0) + 1
        }

    def node_general_responder(self, state: WorkflowState) -> dict:
        """Node 2B: Handles general conversation."""
        print("[Node: General Responder] Drafting standard response...")
        return {
            "messages": ["Drafted standard conversational response."],
            "review_status": "approved",
            "iteration_count": state.get("iteration_count", 0) + 1
        }

    def node_code_reviewer(self, state: WorkflowState) -> dict:
        """Node 3: Quality assurance review node for generated code."""
        print("[Node: Code Reviewer] Inspecting generated code for syntax and safety...")
        # Simulated review approval
        return {
            "messages": ["Code review passed: Syntax valid and secure."],
            "review_status": "approved"
        }

    def route_condition(self, state: WorkflowState) -> str:
        """Conditional Edge Router function."""
        decision = state.get("routing_decision")
        print(f"🔀 [Conditional Router] Directing flow to node: '{decision}'")
        return decision

    def route_review_condition(self, state: WorkflowState) -> str:
        """Conditional Edge for review loops."""
        status = state.get("review_status")
        if status == "needs_review":
            print("🔄 [Review Router] Code needs review. Routing to code_reviewer.")
            return "code_reviewer"
        print("✅ [Review Router] Work approved. Terminating workflow.")
        return "end"

    def run_workflow_simulation(self, query: str):
        """Simulates the state graph traversal flow."""
        print(f"\n🚀 [Starting Workflow Execution] Query: '{query}'")
        
        state: WorkflowState = {
            "user_query": query,
            "messages": [],
            "routing_decision": "",
            "review_status": "",
            "iteration_count": 0
        }

        # Step 1: Classifier Node
        state.update(self.node_classifier(state))

        # Step 2: Conditional Branching
        next_node = self.route_condition(state)
        if next_node == "code_generator":
            state.update(self.node_code_generator(state))
            
            # Step 3: Review Loop Check
            review_next = self.route_review_condition(state)
            if review_next == "code_reviewer":
                state.update(self.node_code_reviewer(state))
        else:
            state.update(self.node_general_responder(state))

        print("\n--- Final Workflow Execution State ---")
        print(f"Final Messages Log: {state['messages']}")
        print(f"Total Iterations: {state['iteration_count']}")
        print(f"Final Review Status: {state['review_status']}")

if __name__ == "__main__":
    orchestrator = AgentWorkflowOrchestrator()
    orchestrator.run_workflow_simulation("Write a Python script to parse JSON logs.")