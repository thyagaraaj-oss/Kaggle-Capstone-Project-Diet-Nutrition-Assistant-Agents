from typing import Dict, Any

class Planner:
    def __init__(self, memory=None):
        self.memory = memory

    def plan(self, user_input: str) -> Dict[str, Any]:
        """
        Simple planner that interprets user input and creates a plan dict.
        """
        plan = {
            "intent": "generate_meal_plan" if "meal" in user_input.lower() or "diet" in user_input.lower() else "general",
            "user_input": user_input,
            "steps": ["parse_requirements", "generate_candidates", "finalize"]
        }
        return plan
