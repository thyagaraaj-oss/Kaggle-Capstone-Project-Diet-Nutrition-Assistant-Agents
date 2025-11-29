from typing import Dict, Any, List
from project.tools.tools import NutritionDB

class Worker:
    def __init__(self, memory=None):
        self.memory = memory
        self.db = NutritionDB()

    def work(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generates candidate meal items or responses based on the plan.
        """
        intent = plan.get("intent", "general")
        user_input = plan.get("user_input", "")
        if intent == "generate_meal_plan":
            # Very simple demo: return a single-day meal plan
            meals = [
                {"name": "Oatmeal with banana", "calories": 350, "protein_g": 10},
                {"name": "Grilled chicken salad", "calories": 450, "protein_g": 35},
                {"name": "Lentil soup with rice", "calories": 500, "protein_g": 20}
            ]
            return {"candidates": meals, "note": "Generated a basic 1-day plan"}
        else:
            # Fallback: use the DB to lookup a sample food
            item = self.db.lookup(user_input.split()[0]) if user_input else {"name": "water", "calories": 0}
            return {"candidates": [item], "note": "Lookup fallback"}
