from typing import Dict, Any

class SessionMemory:
    def __init__(self):
        self.store: Dict[str, Any] = {}

    def get(self, key: str, default=None):
        return self.store.get(key, default)

    def set(self, key: str, value):
        self.store[key] = value

    def append_history(self, key: str, value):
        hist = self.store.get(key, [])
        hist.append(value)
        self.store[key] = hist
