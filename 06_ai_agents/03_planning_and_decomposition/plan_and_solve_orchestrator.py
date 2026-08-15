"""
plan_and_solve_orchestrator.py
Part of 03_planning_and_decomposition/
Demonstrates the Plan-and-Solve paradigm where an agent creates an upfront
structured roadmap before systematically executing each sub-task.
"""

from typing import List, Dict, Any
import json

class PlanAndSolveOrchestrator:
    def __init__(self):
        print("Initializing Plan-and-Solve Strategic Planning Engine...")

    def generate_plan(self, complex_goal: str) -> List[str]:
        """Phase 1: Planning Phase - Decomposes objective into sequential sub-tasks."""
        print(f"\n🗺️ [Phase 1: Planning] Analyzing goal: '{complex_goal}'")
        
        # Simulated LLM planning output
        if "market expansion" in complex_goal.lower():
            plan = [
                "Step 1: Gather regional competitor pricing data for target market.",
                "Step 2: Calculate logistics and shipping overhead costs per unit.",
                "Step 3: Analyze regulatory compliance requirements in the destination country.",
                "Step 4: Synthesize findings into a final strategic financial recommendation."
            ]
        else:
            plan = [
                "Step 1: Parse user request requirements.",
                "Step 2: Execute necessary data gathering.",
                "Step 3: Format final response."
            ]
            
        print(f"   📋 Generated Plan ({len(plan)} steps):")
        for step in plan:
            print(f"      - {step}")
            
        return plan

    def execute_step(self, step_description: str, context: Dict[str, Any]) -> str:
        """Phase 2: Solving Phase - Executes individual steps sequentially with state awareness."""
        print(f"\n⚙️ [Phase 2: Solving] Executing: '{step_description}'")
        
        if "competitor pricing" in step_description.lower():
            result = "Competitor average price is $145.50 per unit."
        elif "logistics" in step_description.lower():
            result = "Shipping overhead is calculated at $12.25 per unit via regional carriers."
        elif "regulatory compliance" in step_description.lower():
            result = "Compliance requires local data residency and ISO certification (Verified)."
        elif "synthesize" in step_description.lower():
            result = "Recommendation: Proceed with expansion. Margins remain healthy at ~32% after logistics and compliance."
        else:
            result = "Step executed successfully."
            
        print(f"   📊 [Step Output]: {result}")
        return result

    def run(self, complex_goal: str) -> str:
        print(f"\n🚀 [Starting Plan-and-Solve Workflow]: {complex_goal}")
        
        # Phase 1: Plan
        plan = self.generate_plan(complex_goal)
        
        # Phase 2: Solve (Sequential Execution with Context Accumulation)
        execution_context: Dict[str, Any] = {}
        for idx, step in enumerate(plan, 1):
            step_result = self.execute_step(step, execution_context)
            execution_context[f"step_{idx}"] = step_result

        final_summary = f"Workflow completed successfully. Final Synthesis: {execution_context.get(f'step_{len(plan)}')}"
        print(f"\n🎉 [Workflow Complete]: {final_summary}")
        return final_summary

if __name__ == "__main__":
    orchestrator = PlanAndSolveOrchestrator()
    orchestrator.run("Develop a comprehensive market expansion analysis for European operations.")