from openai import OpenAI
from typing import List, Dict, Any

class ConversationManager:
    def __init__(self, client: OpenAI):
        self.client = client
        self.intent_map = {
            "greeting": self.respond_greeting,
            "question": self.respond_question,
            "statement": self.respond_statement
        }

    def identify_intents(self, user_input: str) -> List[str]:
        # Basic intent identification (extend with NLU libraries like NLTK, spaCy, or Rasa for better accuracy)
        if "hello" in user_input.lower():
            return ["greeting"]
        elif "?" in user_input:
            return ["question"]
        else:
            return ["statement"]

    def respond(self, user_input: str, user_id: str, emotion_detector: Any) -> str:
        intents = self.identify_intents(user_input)
        responses = []
        for intent in intents:
            response = self.intent_map[intent](user_input, user_id, emotion_detector)
            responses.append(response)
        return "\n".join(responses)

    def respond_greeting(self, user_input: str, user_id: str, emotion_detector: Any) -> str:
        # Respond to greetings
        return f"Hello {user_id}! How can I assist you today?"

    def respond_question(self, user_input: str, user_id: str, emotion_detector: Any) -> str:
        # Respond to questions using OpenAI's chat completions
        conversation_history = [{"role": "system", "content": "You are a helpful AI assistant."}]
        conversation_history.append({"role": "user", "content": user_input})
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            max_tokens=50,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

    def respond_statement(self, user_input: str, user_id: str, emotion_detector: Any) -> str:
        # Respond to statements with empathy (if emotional tone is detected)
        emotional_tone = emotion_detector.detect_emotion(user_input)
        if emotional_tone:
            return f"I sense that you're feeling {emotional_tone}. Would you like to talk about it, {user_id}?"
        return f"Thank you for sharing that with me, {user_id}!"