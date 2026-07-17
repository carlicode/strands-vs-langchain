"""
Minimal Strands Agents example — weather tool.
Install: pip install strands-agents python-dotenv
Uses your default AWS credential chain (aws configure / SSO) to call Bedrock.
Optional: set AWS_PROFILE or AWS_REGION in a .env file (see .env.example).
"""
from dotenv import load_dotenv
from strands import Agent, tool

load_dotenv()


@tool
def get_weather(city: str) -> str:
    """Returns the current weather for a city."""
    return f"It's sunny in {city}."


agent = Agent(tools=[get_weather])

if __name__ == "__main__":
    # agent() already streams the response to stdout as it's generated
    agent("What's the weather in Santa Cruz?")
