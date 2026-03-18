import streamlit as st
from agent import run_agent

st.title("Smart Trader AI")

user_input = st.text_input("Ask about crypto or trading:")

if user_input:
    result = run_agent(user_input)
    st.write(result)
