def run_agent(user_input):
    q = user_input.lower()

    if "btc" in q:
        return """
BTC Analysis:

- Market trend: Volatile
- Risk level: Medium
- Suggestion: Consider DCA strategy instead of all-in.
"""

    if "eth" in q:
        return """
ETH Analysis:

- Market trend: Growing ecosystem
- Risk level: Medium
- Suggestion: Good for long-term holding.
"""

    if "portfolio" in q:
        return """
Portfolio Advice:

- Avoid putting 100% into one asset
- Consider diversification (BTC, ETH, stablecoins)
- Manage risk carefully
"""

    if "trade" in q:
        return """
Trading Tips:

- Always use stop-loss
- Follow trend, don't fight it
- Avoid emotional trading
"""

    return "Ask me about BTC, ETH, portfolio, or trading strategies."
