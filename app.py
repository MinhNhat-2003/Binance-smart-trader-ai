import streamlit as st
from agent import run_agent

st.set_page_config(page_title="Smart Trader AI", page_icon="📈")

st.title("📊 Binance Smart Trader AI")

st.write("Your AI assistant for crypto trading insights.")

user_input = st.text_input("Enter your question:")

if user_input:
    response = run_agent(user_input)
    st.success(response)
