"""
Strands Agents — multi-tool example (weather + currency conversion).
Shows how the model decides, on its own, which tool(s) to call and in
what order, with no graph defined by the developer.
"""
from strands import Agent, tool


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


agent = Agent(tools=[get_weather, convert_currency])

if __name__ == "__main__":
    response = agent(
        "I'm traveling to Santa Cruz with 100 USD. "
        "What's the weather like and how much is that in BOB?"
    )
    print(response)
