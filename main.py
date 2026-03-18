from openclaw.agent import Agent
from tools import analyze_portfolio, trade_strategy

agent = Agent(
    name="Binance Smart Trader AI",
    tools=[analyze_portfolio, trade_strategy]
)

while True:
    user_input = input("You: ")
    response = agent.run(user_input)
    print("AI:", response)
