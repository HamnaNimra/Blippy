from openai import OpenAI
import os
import json
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load or initialize memory
def load_memory():
    print("Loading memory...")  # Debugging message
    if os.path.exists("memory.json"):
        try:
            with open("memory.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error decoding JSON from memory.json. Returning an empty memory.")
            return {}
    return {}

def save_memory(memory):
    try:
        with open("memory.json", "w") as file:
            json.dump(memory, file, indent=4)
            print("Memory saved successfully.")  # Debugging message
    except IOError as e:
        print(f"Error saving memory: {e}")
    except Exception as e:
        print(f"Unexpected error while saving memory: {e}")

# Ensure memory is loaded at the start
memory = load_memory()

# AI Decision Logic for Saving Memory
def should_save_message(prompt, user_id):
    # Basic logic to decide whether to save the message
    # For example, only save if the message is a user preference or something meaningful
    important_keywords = ["name", "favorite", "interest", "preferences"]
    
    if any(keyword in prompt.lower() for keyword in important_keywords):
        return True
    return False

# Chat function with memory
# Chat function with memory
def chat_with_gpt(prompt, user_id="default"):
    user_info = memory.get(user_id, {"name": user_id, "chat_history": []})
    user_memory = user_info["chat_history"]  # Always a list

    # Add past conversation to the history
    conversation_history = [{"role": "system", "content": "You are a helpful AI assistant."}]
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

        # Save the latest conversation if it's deemed important
        if should_save_message(prompt, user_id):
            user_memory.append(f"User: {prompt}")
            user_memory.append(f"Assistant: {reply}")
            user_info["chat_history"] = user_memory
            memory[user_id] = user_info
            save_memory(memory)

        return reply

    except Exception as e:
        return f"Error: {e}"


# Chat loop
def start_chat():
    print("Hi! I'm Blippy with memory now. Type 'quit' to exit.")
    user_id = input("What's your name? ")
    
    # Save user name in memory if it's not already saved
    if user_id not in memory:
        memory[user_id] = {"name": user_id, "chat_history": []}  # Store name and initialize empty chat history
        save_memory(memory)
        print(f"Nice to meet you, {user_id}!")

    # Adding functionality to ensure memory is saved even if no chat occurs
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Blippy: Bye! I'll remember this chat!")
            save_memory(memory)  # Save memory before quitting
            break
        response = chat_with_gpt(user_input, user_id)
        print(f"Blippy: {response}")

if __name__ == "__main__":
    # Check if the script can access the current directory and write to it
    print(f"Current working directory: {os.getcwd()}")  # Debugging message
    start_chat()