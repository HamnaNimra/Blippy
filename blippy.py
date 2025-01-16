import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    try:
        # Send the prompt to OpenAI's API using the new interface
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        # Extract the chatbot's reply
        reply = response['choices'][0]['text'].strip()
        return reply

    except Exception as e:
        return f"Error: {e}"

def start_chat():
    print("Hi! I'm your AI chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Bye! Have a great day.")
            break
        response = chat_with_gpt(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chat()
