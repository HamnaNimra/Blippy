import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from conversation import ConversationManager
from emotions import EmotionDetector
from topics import TopicSelector
from jokes import JokeSharer
from memory import MemoryManager

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    conversation_manager = ConversationManager(client)
    emotion_detector = EmotionDetector()
    topic_selector = TopicSelector()
    joke_sharer = JokeSharer()
    memory_manager = MemoryManager()

    print("Hi! I'm Blippy with enhanced features. Type 'quit' to exit.")
    user_id = input("What's your name? ")
    memory_manager.load_memory(user_id)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Blippy: Bye! I'll remember this chat!")
            memory_manager.save_memory()
            break
        elif user_input.lower() == "topics":
            topic_selector.display_topics()
            selected_topic = input("Choose a topic (or type 'back'): ")
            if selected_topic.lower()!= "back":
                user_input = topic_selector.get_topic_question(selected_topic)
        
        intents = conversation_manager.identify_intents(user_input)
        response = conversation_manager.respond(intents, user_id, emotion_detector)
        
        if "joke" in intents or user_input.lower() == "joke":
            response += "\n" + joke_sharer.share_joke()
        
        print(f"Blippy: {response}")
        memory_manager.save_conversation(user_id, user_input, response)

if __name__ == "__main__":
    main()