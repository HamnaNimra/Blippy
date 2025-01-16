import random

class JokeSharer:
    def __init__(self):
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            # Add more jokes as needed
        ]

    def share_joke(self) -> str:
        return random.choice(self.jokes)