"""
Minimal Strands Agents example — weather tool.
Install: pip install strands-agents
"""
from strands import Agent, tool


@tool
def get_weather(city: str) -> str:
    """Returns the current weather for a city."""
    return f"It's sunny in {city}."


agent = Agent(tools=[get_weather])

if __name__ == "__main__":
    response = agent("What's the weather in Santa Cruz?")
    print(response)
