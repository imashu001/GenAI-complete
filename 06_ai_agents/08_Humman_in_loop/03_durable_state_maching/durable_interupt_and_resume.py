import uuid
from typing import Dict, Any, Optional

# --- 1. Durable State & Checkpoint Store (Simulating a Database) ---
class CheckpointStore:
    def __init__(self):
        self.store: Dict[str, Dict[str, Any]] = {}

    def save(self, thread_id: str, state: Dict[str, Any]):
        # Deep copy or serialize state to persistent storage
        self.store[thread_id] = dict(state)

    def load(self, thread_id: str) -> Optional[Dict[str, Any]]:
        return self.store.get(thread_id)

db = CheckpointStore()

# --- 2. Workflow Node Functions ---
def agent_planning_node(state: Dict[str, Any]) -> Dict[str, Any]:
    print(f"\n[Agent] Step 1: Analyzing user request...")
    user_prompt = state["user_prompt"]
    
    # Simulate agent deciding to run a high-risk tool
    if "transfer" in user_prompt.lower():
        state["proposed_action"] = "EXECUTE_WIRE_TRANSFER_$5000"
        state["status"] = "PENDING_APPROVAL"
        print(f"[Agent] High-risk action identified: {state['proposed_action']}")
    else:
        state["proposed_action"] = "COMPLETED_NORMALLY"
        state["status"] = "FINISHED"
        
    return state

def high_risk_execution_node(state: Dict[str, Any]) -> Dict[str, Any]:
    print(f"\n[System] Executing approved action: {state['proposed_action']}...")
    state["status"] = "SUCCESSFULLY_EXECUTED"
    return state

# --- 3. Orchestrator with Interrupt & Resume Logic ---
def run_workflow_until_interrupt(thread_id: str, user_prompt: Optional[str] = None) -> dict:
    # Try to load existing checkpoint
    state = db.load(thread_id)
    
    if not state:
        # Initialize brand new state
        state = {"thread_id": thread_id, "user_prompt": user_prompt, "status": "STARTED"}
        
    # Execute planning node if we haven't reached approval yet
    if state["status"] == "STARTED":
        state = agent_planning_node(state)
        db.save(thread_id, state) # Save checkpoint
        
    # Check if we hit an interrupt gate
    if state["status"] == "PENDING_APPROVAL":
        print(f"[Workflow Paused] Thread {thread_id} is waiting for human intervention.")
        return state
        
    return state

def resume_workflow(thread_id: str, human_decision: str, feedback: str = "") -> dict:
    state = db.load(thread_id)
    if not state:
        raise ValueError(f"No active session found for thread {thread_id}")
        
    print(f"\n[Human Reviewer] Decision received: {human_decision} (Feedback: {feedback})")
    state["human_decision"] = human_decision
    state["human_feedback"] = feedback
    
    if human_decision == "APPROVE":
        state["status"] = "APPROVED"
        db.save(thread_id, state)
        # Resume execution of the next node
        state = high_risk_execution_node(state)
        state["status"] = "FINISHED"
    else:
        state["status"] = "REJECTED_BY_HUMAN"
        print(f"[Workflow Terminated] Action blocked by human supervisor.")
        
    db.save(thread_id, state)
    return state

# --- Simulation Run ---
if __name__ == "__main__":
    thread_id = str(uuid.uuid4())
    
    # 1. Start the workflow (Simulates user request)
    print("--- Phase 1: Initial Run ---")
    current_state = run_workflow_until_interrupt(
        thread_id=thread_id, 
        user_prompt="Please transfer $5000 to account #9921."
    )
    
    # At this point, the server process could shut down entirely, 
    # and the state is safely saved in `db`.
    
    # 2. Days later, human reviews and resumes workflow
    print("\n--- Phase 2: Resuming After Human Approval ---")
    final_state = resume_workflow(
        thread_id=thread_id, 
        human_decision="APPROVE", 
        feedback="Verified via phone call with client."
    )
    
    print(f"\nFinal Workflow Status: {final_state['status']}")