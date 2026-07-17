"""
LangChain — multi-tool example (weather + currency conversion).
Same task as the Strands version, showing the extra scaffolding
(prompt template, scratchpad, executor) LangChain expects you to define.
Requires OPENAI_API_KEY in your environment or a .env file (see .env.example).
"""
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


@tool
def get_weather(city: str) -> str:
    """Returns the current weather for a city."""
    return f"It's sunny in {city}, 24°C."


@tool
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """Converts an amount from one currency to another (mock rates)."""
    mock_rates = {("USD", "BOB"): 6.96, ("BOB", "USD"): 0.14}
    rate = mock_rates.get((from_currency, to_currency))
    if not rate:
        return "Exchange rate not available."
    return f"{amount} {from_currency} = {amount * rate:.2f} {to_currency}"


llm = ChatOpenAI(model="gpt-4o")
tools = [get_weather, convert_currency]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful travel assistant."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools)

if __name__ == "__main__":
    result = executor.invoke({
        "input": (
            "I'm traveling to Santa Cruz with 100 USD. "
            "What's the weather like and how much is that in BOB?"
        )
    })
    print(result["output"])
