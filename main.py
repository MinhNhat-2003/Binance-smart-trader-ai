from openclaw.agent import Agent

def analyze_portfolio(input_text):
    return "Portfolio looks okay, consider diversification."

def trade_strategy(input_text):
    return "Consider trend and risk management before trading."

agent = Agent(
    name="Binance Smart Trader AI",
    tools=[analyze_portfolio, trade_strategy]
)

while True:
    user_input = input("You: ")
    response = agent.run(user_input)
    print("AI:", response)
