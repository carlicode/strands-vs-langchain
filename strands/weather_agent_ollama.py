"""
Minimal Strands Agents example — weather tool, running on Ollama (free, local).
Install: pip install 'strands-agents[ollama]' python-dotenv
Requires Ollama running locally: https://ollama.ai
    ollama pull llama3.1
    ollama serve
Optional: set OLLAMA_HOST and OLLAMA_MODEL_ID in a .env file (see .env.example)
to point at a different server or model.
"""
import os

from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.ollama import OllamaModel

load_dotenv()


@tool
def get_weather(city: str) -> str:
    """Returns the current weather for a city."""
    return f"It's sunny in {city}."


ollama_model = OllamaModel(
    host=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
    model_id=os.getenv("OLLAMA_MODEL_ID", "llama3.1"),
)

agent = Agent(model=ollama_model, tools=[get_weather])

if __name__ == "__main__":
    # agent() already streams the response to stdout as it's generated
    agent("What's the weather in Santa Cruz?")
