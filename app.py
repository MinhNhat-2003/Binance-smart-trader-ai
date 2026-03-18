import streamlit as st
from agent import run_agent

st.title("📊 Binance Smart Trader AI")

question = st.text_input("Ask about your portfolio or trades:")

if question:
    response = run_agent(question)
    st.write(response)
