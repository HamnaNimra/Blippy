# Blippy - AI Chatbot with Memory

## Overview

Blippy is an AI-powered chatbot built using OpenAI's GPT-3.5-turbo model. 


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

2. Ask Blippy anything at all, make sure to pay for tokens through OpenAI. 

3. To quit the chat, type `quit`. Blippy will save the memory before quitting.

## Notes

- Error Handling and Input Validation have been improved for a better user experience


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
