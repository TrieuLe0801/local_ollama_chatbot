# Local Ollama Chatbot

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

A lightweight, privacy-focused chatbot application powered by **Ollama** and **LangChain**, built with **Streamlit**. Run large language models locally on your machine without relying on cloud services or APIs.

## What This Project Does

Local Ollama Chatbot is a conversational AI application that allows you to interact with open-source language models running entirely on your local machine. It provides a user-friendly web interface powered by Streamlit where you can:

- Chat with locally-hosted LLMs (Llama, DeepSeek, CodeLlama, etc.)
- Fine-tune model behavior with advanced parameters
- Maintain chat history within a session
- Stream responses for real-time interaction

## Why Use This Project

### Key Features

- **Privacy-First**: All conversations stay on your local machine—no data sent to external servers
- **Cost-Free**: No API costs or subscriptions required
- **Customizable**: Configure model parameters, temperature, sampling strategies, and more
- **Multiple Models**: Easy switching between different Ollama-supported language models
- **Real-Time Streaming**: Watch responses stream in real-time as the model generates them
- **Session Management**: Built-in chat reset and conversation tracking
- **Docker Support**: Simplified setup using Docker Compose

### Ideal For

- Developers testing LLM applications locally
- Privacy-conscious users who want to keep conversations private
- Researchers experimenting with different models and parameters
- Learning and prototyping AI applications

## Getting Started

### Prerequisites

- **Python 3.8+**
- **Ollama** installed and running ([Download](https://ollama.ai))
- **Docker & Docker Compose** (optional, for containerized setup)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/TrieuLe0801/local_ollama_chatbot.git
   cd local_ollama_chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

3. **Configure environment**
   
   Create or update the `.env` file:
   ```env
   OLLAMA_HOST="http://localhost:11434"
   ```

4. **Start Ollama** (in a separate terminal)
   ```bash
   ollama serve
   ```
   
   Or using the makefile:
   ```bash
   make run_ollama
   ```

5. **Pull a model** (if not already available)
   ```bash
   ollama pull llama3.1
   ```
   
   Available models in the app:
   - `llama3.1` (default)
   - `deepseek-r1:8b`
   - `codellama:13b`

### Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will open at `http://localhost:8501` in your browser.

### Using Docker Compose

For a quick setup without manual Ollama installation:

```bash
docker-compose up -d
streamlit run app.py
```

This starts the Ollama service in a container on port `11434`.

## Usage Examples

### Basic Chat

1. Open the app in your browser
2. Select a model from the sidebar dropdown
3. Adjust model parameters as desired (optional)
4. Type your message in the chat input box
5. Watch the response stream in real-time
6. Click "Reset chat" to start a new conversation

### Adjusting Model Behavior

Use the sidebar controls to tune model parameters:

| Parameter | Effect |
|-----------|--------|
| **Temperature** | Lower (0.0) = more deterministic, Higher (1.0) = more creative |
| **Top-P** | Controls diversity—lower values focus on probable tokens |
| **Top-K** | Limits token selection to K most probable tokens |
| **Mirostat** | Sampling algorithm for better output quality |
| **Context Size** | How much previous conversation to remember |

## Project Structure

```
local_ollama_chatbot/
├── app.py                 # Main Streamlit application
├── src/
│   ├── chat_engine.py     # ChatEngineOllama class wrapping LangChain
│   ├── sidebar.py         # Model configuration UI components
│   └── __init__.py
├── docker-compose.yaml    # Docker setup for Ollama
├── requirement.txt        # Python dependencies
├── makefile               # Development utilities
├── .env                   # Environment configuration
└── README.md              # This file
```

## Development

### Code Quality

Format and lint your code:

```bash
# Format code
make format

# Check code quality
make quality
```

### Available Make Commands

```bash
make format      # Format code with black and isort
make quality     # Run flake8, black, and isort checks
make clean       # Remove cache and build artifacts
make run_ollama  # Start Ollama service
```

## Troubleshooting

### Ollama Connection Issues

**Problem**: "Connection refused" or "Cannot connect to Ollama"

**Solution**:
- Ensure Ollama is running: `ollama serve`
- Verify `OLLAMA_HOST` in `.env` matches your Ollama server
- Check if Ollama is accessible on `http://localhost:11434`

### Model Not Found

**Problem**: Model selection dropdown is empty or model fails to load

**Solution**:
- Pull the model: `ollama pull llama3.1`
- List available models: `ollama list`
- Restart the Streamlit app

### Performance Issues

**Solution**:
- Use smaller models (e.g., `llama2:7b`) for faster responses
- Reduce context size in sidebar parameters
- Ensure sufficient system memory and GPU (if available)

## Dependencies

- **streamlit**: Web UI framework
- **langchain-ollama**: LangChain integration with Ollama
- **python-dotenv**: Environment variable management
- **flake8, black, isort**: Code quality tools

See `requirement.txt` for all dependencies.

## Support & Resources

- **Ollama Documentation**: https://ollama.ai
- **LangChain Documentation**: https://python.langchain.com
- **Streamlit Documentation**: https://docs.streamlit.io
- **Issues & Discussions**: Open an issue on GitHub

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes and ensure code quality (`make quality`)
4. Format your code (`make format`)
5. Commit and push to your fork
6. Open a pull request

Please ensure your code follows the project's style guidelines and includes appropriate tests or documentation.

## License

This project is licensed under the **Apache License 2.0**. See [LICENSE](LICENSE) for details.

## Maintainer

**TrieuLe0801** - Project creator and maintainer

---

**Get started with local AI today!** 🚀