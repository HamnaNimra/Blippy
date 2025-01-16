# Blippy - AI Chatbot with Memory

Blippy is an AI-powered chatbot built using OpenAI's GPT-3.5-turbo model. It allows for interactive conversations while remembering past interactions for a personalized experience. The chatbot can store and recall user preferences and key information across sessions.

## Features
- **Memory**: Blippy saves important information from conversations, including the user's name and preferences.
- **AI-Driven Logic**: The AI decides which parts of the conversation are important enough to be stored.
- **Persistent Memory**: User data is stored in a local `memory.json` file, and only meaningful interactions are saved.

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

2. When prompted, provide your name. The chatbot will remember it and address you by name in future conversations.

3. To quit the chat, type `quit`. Blippy will save the memory before quitting.

## Notes

- `memory.json` is used to store user data, including the user's name and conversation history. The file is added to `.gitignore` to ensure it's not tracked by Git.
- The AI decides which data to save based on certain keywords like "name", "favorite", and "preferences". You can modify this logic to suit your needs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
