# app.py
import streamlit as st

st.title("📊 Internal Sales Dashboard")

username = st.text_input("Enter your name")
sales = st.number_input("Enter today’s sales amount", min_value=0)

if st.button("Submit"):
    st.success(f"Thank you {username}, sales of ₹{sales} submitted!")
