import openai
import os
import json
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load or initialize memory
def load_memory():
    if os.path.exists("memory.json"):
        with open("memory.json", "r") as file:
            return json.load(file)
    return {}

def save_memory(memory):
    with open("memory.json", "w") as file:
        json.dump(memory, file, indent=4)

memory = load_memory()

# Chat function with memory
def chat_with_gpt(prompt, user_id="default"):
    user_memory = memory.get(user_id, [])
    conversation_history = "\n".join(user_memory[-5:])  # Use last 5 messages
    
    full_prompt = f"{conversation_history}\nUser: {prompt}\nBlippy:"

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=full_prompt,
            max_tokens=150,
            temperature=0.7
        )
        reply = response.choices[0].text.strip()
        
        # Update memory
        user_memory.append(f"User: {prompt}")
        user_memory.append(f"Blippy: {reply}")
        memory[user_id] = user_memory
        save_memory(memory)
        
        return reply
    except Exception as e:
        return f"Error: {e}"

# Chat loop
def start_chat():
    print("Hi! I'm Blippy with memory now. Type 'quit' to exit.")
    user_id = input("What's your name? ")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Blippy: Bye! I'll remember this chat!")
            break
        response = chat_with_gpt(user_input, user_id)
        print(f"Blippy: {response}")

if __name__ == "__main__":
    start_chat()
