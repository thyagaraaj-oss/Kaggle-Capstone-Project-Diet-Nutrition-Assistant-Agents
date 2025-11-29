from typing import Dict, Any
from project.memory.session_memory import SessionMemory
from project.agents.planner import Planner
from project.agents.worker import Worker
from project.agents.evaluator import Evaluator
from project.core.context_engineering import build_context
from project.core.observability import Observability

class MainAgent:
    def __init__(self):
        self.memory = SessionMemory()
        self.planner = Planner(memory=self.memory)
        self.worker = Worker(memory=self.memory)
        self.evaluator = Evaluator(memory=self.memory)
        self.obs = Observability()

    def handle_message(self, user_input: str) -> Dict[str, Any]:
        # Build context
        context = build_context(self.memory.store, user_input)
        self.obs.log("Received input", {"input": user_input})

        # Planner creates a plan
        plan = self.planner.plan(user_input)
        self.obs.log("Plan created", {"plan": plan})

        # Worker generates candidates
        work_result = self.worker.work(plan)
        candidates = work_result.get("candidates", [])
        self.obs.log("Worker produced candidates", {"count": len(candidates)})

        # Evaluator scores candidates
        constraints = {}
        # if user has target calories in memory, use it
        cal_target = self.memory.get("calorie_target")
        if cal_target:
            constraints["calories"] = cal_target
        eval_result = self.evaluator.evaluate(candidates, constraints=constraints)
        best = eval_result.get("best", {}).get("item") if eval_result.get("best") else None
        response_text = ""
        if plan.get("intent") == "generate_meal_plan":
            response_text = f\"Here is a simple meal plan (best choice: {best.get('name') if best else 'N/A'}).\"
        else:
            response_text = f\"I found: {best.get('name') if best else 'No suggestion'}.\"

        # Save to memory
        self.memory.append_history("interactions", {"input": user_input, "response": response_text})

        return {"response": response_text, "plan": plan, "candidates": candidates, "evaluation": eval_result, "logs": self.obs.get_logs()}

def run_agent(user_input: str):
    agent = MainAgent()
    result = agent.handle_message(user_input)
    return result["response"]
