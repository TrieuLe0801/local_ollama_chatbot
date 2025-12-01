from langchain_ollama import ChatOllama

class ChatEngineOllama(ChatOllama):
    """Chat engine using Ollama LLM."""

    def __init__(self, model: str = "llama3.1", base_url: str ="http://localhost:11434", temperature: float = 0.7, top_p: float = 0.9, **kwargs):
        super().__init__(model=model, base_url=base_url, temperature=temperature, top_p=top_p, **kwargs)
        self.model = model
        self.temperature = temperature
        self.top_p = top_p
    
    