# Blippy - AI Chatbot with Memory

## Overview

Blippy is an AI-powered chatbot built using OpenAI's GPT-3.5-turbo model. It enables interactive conversations while remembering past interactions for a personalized experience. The chatbot can store and recall user preferences, key information, and conversation history across sessions.

## Features
------------

* **Memory**: Blippy saves important information from conversations, including:
    + User's name and preferences
    + Conversation history (with **Memory Insights** to view past conversations)
* **AI-Driven Logic**: The AI decides which parts of the conversation are important enough to be stored
* **Persistent Memory**: User data is stored in a local `memory.json` file, with only meaningful interactions saved
* **Multi-Intent Understanding**: Blippy can identify multiple intents in user inputs
* **Emotion Detection**: Basic emotion detection for empathetic responses
* **Joke Sharing**: Blippy can share jokes on demand
* **Conversation Topics**: Users can choose from predefined conversation topics


## Requirements

- Python 3.11 (or compatible)
- OpenAI API key
- `.env` file containing the `OPENAI_API_KEY` environment variable.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/HamnaNimra/Blippy.git
    cd Blippy
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Get OpenAI API Key
- Go to [OpenAI API](https://platform.openai.com/) and log in or sign up.
- Generate an API key.
- Create a .env file in your project folder and add your key:

    ```
    OPENAI_API_KEY=your-api-key-here
    ```

## How to Use

1. Run the script:

    ```bash
    python blippy.py
    ```

2. Provide your name when prompted. The chatbot will remember it and address you by name in future conversations
3. Explore conversation topics by typing topics
4. Share a joke by typing joke
5. View conversation history by typing memory
6. Quit the chat by typing quit. Blippy will save the memory before quitting



2. When prompted, provide your name. The chatbot will remember it and address you by name in future conversations.

3. To quit the chat, type `quit`. Blippy will save the memory before quitting.

## Notes

- `memory.json` is used to store user data, including the user's name and conversation history. The file is added to `.gitignore` to ensure it's not tracked by Git.
- The AI decides which data to save based on certain keywords like "name", "favorite", and "preferences". You can modify this logic to suit your needs.
- Error Handling and Input Validation have been improved for a better user experience


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
