"""
agent_memory_manager.py
Part of 04_memory_and_state/
Demonstrates the separation of short-term thread checkpointers and 
long-term cross-thread semantic memory management for an AI agent.
"""

from typing import List, Dict, Any, Tuple

class SimulatedMemoryStore:
    """Simulates a persistent cross-thread store (like RedisStore or LangGraph Store)."""
    def __init__(self):
        self.store: Dict[Tuple[str, str], Dict[str, Any]] = {}

    def put(self, namespace: Tuple[str, str], key: str, value: Dict[str, Any]):
        """Saves a long-term memory item under a specific namespace."""
        composite_key = (namespace[0], namespace[1], key)
        self.store[composite_key] = value
        print(f"💾 [Long-Term Memory STORED] Namespace: {namespace} | Key: {key}")

    def search(self, namespace_prefix: Tuple[str, str]) -> List[Dict[str, Any]]:
        """Retrieves memories matching a namespace prefix (e.g., user preferences)."""
        results = []
        for (ns_type, ns_id, key), value in self.store.items():
            if ns_type == namespace_prefix[0] and ns_id == namespace_prefix[1]:
                results.append({"key": key, "value": value})
        print(f"🔍 [Long-Term Memory SEARCH] Found {len(results)} items for namespace: {namespace_prefix}")
        return results

class StatefulAgentMemoryOrchestrator:
    def __init__(self):
        print("Initializing Stateful Agent Memory & State Manager...")
        self.long_term_store = SimulatedMemoryStore()
        # Short-term thread state checkpointer simulation
        self.thread_checkpoints: Dict[str, List[Dict[str, str]]] = {}

    def save_checkpoint(self, thread_id: str, scratchpad_history: List[Dict[str, str]]):
        """Simulates short-term thread checkpointing for crash recovery."""
        self.thread_checkpoints[thread_id] = scratchpad_history
        print(f"📌 [Short-Term Checkpoint Saved] Thread ID: {thread_id} ({len(scratchpad_history)} steps recorded)")

    def load_checkpoint(self, thread_id: str) -> List[Dict[str, str]]:
        """Restores thread state after an interruption or server restart."""
        history = self.thread_checkpoints.get(thread_id, [])
        print(f"📂 [Short-Term Checkpoint Restored] Thread ID: {thread_id} found {len(history)} prior steps.")
        return history

    def extract_and_store_preferences(self, user_id: str, user_utterance: str):
        """Extracts long-term facts from dialogue and persists them across threads."""
        if "prefer" in user_utterance.lower() or "favorite" in user_utterance.lower():
            # In production, an LLM extracts key-value facts here
            self.long_term_store.put(
                namespace=("user_preferences", user_id),
                key="preferred_currency",
                value={"fact": user_utterance, "category": "preference"}
            )

    def get_agent_context(self, user_id: str, thread_id: str) -> Dict[str, Any]:
        """Aggregates short-term thread history and long-term user preferences."""
        print(f"\n--- Aggregating Agent Context for User: {user_id} (Thread: {thread_id}) ---")
        short_term_history = self.load_checkpoint(thread_id)
        long_term_prefs = self.long_term_store.search(("user_preferences", user_id))
        
        return {
            "thread_history": short_term_history,
            "persistent_preferences": long_term_prefs
        }

if __name__ == "__main__":
    manager = StatefulAgentMemoryOrchestrator()
    
    user_id = "user_992"
    thread_id = "thread_alpha_01"
    
    # 1. Simulate saving a user preference in a long-term memory store
    manager.extract_and_store_preferences(user_id, "I always prefer my financial reports denominated in Euros.")
    
    # 2. Simulate saving a short-term execution step checkpoint
    manager.save_checkpoint(thread_id, [{"thought": "Checked stock price", "action": "get_stock_price(AAPL)"}])
    
    # 3. Later, across a completely new session/thread, retrieve the user context
    new_thread_id = "thread_beta_02"
    context = manager.get_agent_context(user_id, new_thread_id)
    
    print("\n--- Final Assembled Agent Context ---")
    print(context)