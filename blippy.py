import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from conversation import ConversationManager
from emotions import EmotionDetector
from topics import TopicSelector
from jokes import JokeSharer
from memory import MemoryManager
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ML Integration
def train_model(df):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['user_input'])
    y = df['intent']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = MultinomialNB()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print("Model Accuracy:", accuracy_score(y_test, y_pred))
    
    return vectorizer, model

def predict_intent(vectorizer, model, user_input):
    input_vec = vectorizer.transform([user_input])
    predicted_intent = model.predict(input_vec)[0]
    return predicted_intent

# Feedback Mechanism
def collect_feedback(user_id, user_input, response, correct):
    feedback_data = {
        'user_id': user_id,
        'user_input': user_input,
        'esponse': response,
        'correct': correct
    }
    with open('feedback.json', 'a+') as f:
        json.dump(feedback_data, f)
        f.write('\n')

def main():
    conversation_manager = ConversationManager(client)
    emotion_detector = EmotionDetector()
    topic_selector = TopicSelector()
    joke_sharer = JokeSharer()
    memory_manager = MemoryManager()
    
    # Load existing feedback data for ML
    try:
        df = pd.read_json('feedback.json', lines=True)
        vectorizer, ml_model = train_model(df)
    except FileNotFoundError:
        vectorizer, ml_model = None, None
    
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
        
        # Use ML model if available, else fallback to original intent identification
        if ml_model:
            predicted_intent = predict_intent(vectorizer, ml_model, user_input)
            intents = [predicted_intent]
        else:
            intents = conversation_manager.identify_intents(user_input)
        
        response = conversation_manager.respond(intents, user_id, emotion_detector)
        
        if "joke" in intents or user_input.lower() == "joke":
            response += "\n" + joke_sharer.share_joke()
        
        print(f"Blippy: {response}")
        
        # Feedback Mechanism
        feedback_correct = input("Was the response correct? (y/n): ")
        collect_feedback(user_id, user_input, response, feedback_correct.lower() == 'y')
        
        memory_manager.save_conversation(user_id, user_input, response)
        
        # Periodically retrain the model with new feedback data
        if vectorizer and len(pd.read_json('feedback.json', lines=True)) % 100 == 0:
            df = pd.read_json('feedback.json', lines=True)
            vectorizer, ml_model = train_model(df)

if __name__ == "__main__":
    main()