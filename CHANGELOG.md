# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [1.2.0] - 2025-01-16
### Added
- **Multi-Intent Understanding**: Blippy can now identify multiple intents in user inputs.
- **Emotion Detection**: Basic emotion detection for empathetic responses.
- **Joke Sharing**: Blippy can share jokes on demand.
- **Conversation Topics**: Users can choose from predefined conversation topics.
- **Memory Insights**: Users can view their conversation history.

### Changed
- **Code Refactoring**: Reorganized code into logical modules (conversation, emotions, topics, jokes, memory) for improved maintainability.

### Fixed
- **Error Handling**: Enhanced error handling for better user experience.
- **Input Validation**: Added basic input validation for user inputs.

## [1.1.0] - 2025-01-16
### Added
- **Contextual Memory**: Blippy remembers user names and past messages.
- **AI-Driven Logic**: Saves only important messages to memory.

### Fixed
- **Memory Saving**: Ensures memory is saved on quit.
- **API Quota Error**: Handles API quota errors more gracefully.

## [1.0.0] - 2025-01-15
### Added
- Initial version of Blippy with OpenAI integration.

### Changed
- **Documentation**: Added README and LICENSE files.
- **Environment Variables**: Added `.env` to `.gitignore`.