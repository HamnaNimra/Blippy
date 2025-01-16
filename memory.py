import json
import os

class MemoryManager:
    def __init__(self):
        self.memory_file = "memory.json"

    def load_memory(self, user_id: str):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as file:
                memory = json.load(file)
                if user_id in memory:
                    return memory[user_id]
        return {}

    def save_memory(self):
        # Save the entire memory (consider implementing incremental saving for large user bases)
        with open(self.memory_file, "w") as file:
            json.dump(self.memory, file, indent=4)

    def save_conversation(self, user_id: str, user_input: str, response: str):
        if user_id not in self.memory:
            self.memory[user_id] = []
        self.memory[user_id].append({"user": user_input, "assistant": response})