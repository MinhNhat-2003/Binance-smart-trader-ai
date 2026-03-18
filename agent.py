from openclaw.agent import Agent
from tools import analyze_portfolio, trade_strategy

agent = Agent(
    name="Binance Smart Trader AI",
    tools=[analyze_portfolio, trade_strategy]
)

def run_agent(user_input):
    return agent.run(user_input)
