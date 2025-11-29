from typing import Dict, Any

class NutritionDB:
    """
    Mock nutrition database for demo purposes.
    """
    def __init__(self):
        self.data = {
            "oatmeal": {"name": "Oatmeal", "calories": 150, "protein_g": 5},
            "banana": {"name": "Banana", "calories": 100, "protein_g": 1},
            "chicken": {"name": "Grilled chicken", "calories": 250, "protein_g": 30},
            "lentils": {"name": "Lentil soup", "calories": 300, "protein_g": 18},
            "rice": {"name": "Rice", "calories": 200, "protein_g": 4},
            "water": {"name": "Water", "calories": 0, "protein_g": 0}
        }

    def lookup(self, key: str) -> Dict[str, Any]:
        key = key.lower()
        return self.data.get(key, {"name": key, "calories": 100, "protein_g": 5})
