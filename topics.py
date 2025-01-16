class TopicSelector:
    def __init__(self):
        self.topics = {
            "tech": "What's your favorite programming language?",
            "movies": "Have you seen any good movies lately?",
            "travel": "If you could travel anywhere, where would you go?"
        }

    def display_topics(self):
        print("Available topics:")
        for topic in self.topics:
            print(topic)

    def get_topic_question(self, topic: str) -> str:
        return self.topics.get(topic, "Topic not found!")