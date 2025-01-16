from openai import OpenAI
import os
import json
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    conversation_history = [{"role": "system", "content": "You are a helpful AI assistant."}]

    # Add past conversation to the history
    for i in user_memory[-5:]:  # Last 5 messages
        role, content = i.split(":", 1)
        conversation_history.append({"role": role.strip().lower(), "content": content.strip()})

    # Add the new user input
    conversation_history.append({"role": "user", "content": prompt})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            max_tokens=50,
            temperature=0.7
        )
        reply = response.choices[0].message.content.strip()

        # Save the latest conversation
        user_memory.append(f"User: {prompt}")
        user_memory.append(f"Assistant: {reply}")
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
