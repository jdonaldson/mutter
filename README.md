# Mutter

Mutter is a macOS application that combines speech-to-text technology with AI-powered conversation. It lives in your menu bar, ready to listen and respond whenever you need it.

## Features

- Speech recognition using Whisper
- AI-powered responses using Llama 3.1 via Ollama
- macOS menu bar integration for easy access
- Conversation saving functionality
- Desktop notifications for new messages

## Requirements

- macOS (tested on 10.15+)
- Python 3.8 or higher
- Ollama installed and running with Llama 3.1 model

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/mutter.git
   cd mutter
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have Ollama installed and the Llama 3.1 model pulled:
   ```
   ollama pull llama3.1
   ```

## Usage

1. Run the Mutter application:
   ```
   python mutter/main.py
   ```

2. The Mutter icon will appear in your macOS menu bar.

3. Click on the icon to access the following options:
   - Start Listening: Begins the speech recognition process
   - Stop Listening: Stops the speech recognition process
   - Save Conversation: Saves the current conversation to a text file

4. When "Start Listening" is activated, speak clearly into your microphone. Mutter will transcribe your speech and send it to Llama 2 for a response.

5. You'll receive desktop notifications for new AI responses.

## Configuration

Currently, Mutter uses default settings for Whisper (base model) and Ollama (default URL). To change these, modify the initialization parameters in `mutter/main.py`.

## Contributing

Contributions to Mutter are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for the Whisper model
- Meta AI for the Llama 3.1 model
- Ollama for easy local AI model deployment
- The creators and maintainers of the Python libraries used in this project


