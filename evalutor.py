from typing import Dict, Any, List

class Evaluator:
    def __init__(self, memory=None):
        self.memory = memory

    def evaluate(self, candidates: List[Dict[str, Any]], constraints: Dict[str, Any]=None) -> Dict[str, Any]:
        """
        Very simple evaluator that scores candidates by closeness to calorie target if provided.
        """
        constraints = constraints or {}
        calorie_target = constraints.get("calories")
        scored = []
        for c in candidates:
            cal = c.get("calories", 0)
            score = 1.0
            if calorie_target:
                score = max(0.0, 1.0 - abs(cal - calorie_target) / max(1, calorie_target))
            scored.append({"item": c, "score": score})
        scored = sorted(scored, key=lambda x: x["score"], reverse=True)
        return {"scored": scored, "best": scored[0] if scored else None}
