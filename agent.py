def run_agent(user_input):
    q = user_input.lower()

    if "btc" in q:
        return """
📊 BTC Analysis

Market trend: Volatile  
Risk level: Medium  

💡 Insight:
BTC often reacts strongly to macro news. Consider using DCA instead of going all-in to reduce risk.
"""

    if "eth" in q:
        return """
📊 ETH Analysis

Market trend: Expanding ecosystem  
Risk level: Medium  

💡 Insight:
ETH benefits from DeFi and L2 growth. Suitable for long-term positioning.
"""

    if "portfolio" in q:
        return """
📊 Portfolio Strategy

💡 Key ideas:
- Diversify across BTC, ETH, and stablecoins  
- Avoid overexposure to a single asset  
- Rebalance periodically  
"""

    if "trade" in q:
        return """
📊 Trading Tips

💡 Rules:
- Always set stop-loss  
- Trade with the trend  
- Avoid emotional decisions  
"""

    return "Ask me about BTC, ETH, portfolio, or trading strategies."
