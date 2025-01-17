from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Chat function without memory
def chat_with_gpt(prompt):
    conversation_history = [{"role": "system", "content": "You are a helpful AI assistant."}]
    conversation_history.append({"role": "user", "content": prompt})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            max_tokens=50,
            temperature=0.7
        )
        reply = response.choices[0].message.content.strip()
        return reply

    except Exception as e:
        return f"Error: {e}"

# Chat loop
def start_chat():
    print("Hi! I'm Blippy. Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Blippy: Bye!")
            break
        response = chat_with_gpt(user_input)
        print(f"Blippy: {response}")

if __name__ == "__main__":
    print(f"Current working directory: {os.getcwd()}")
    start_chat()
