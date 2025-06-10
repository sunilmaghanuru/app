# app.py
import streamlit as st

st.title("Simple Interest Calculator")

P = st.number_input("Enter principal (₹)", min_value=0)
R = st.number_input("Enter rate (%)", min_value=0.0)
T = st.number_input("Enter time (years)", min_value=0.0)

if st.button("Calculate"):
    SI = (P * R * T) / 100
    st.success(f"Simple Interest = ₹{SI:.2f}")
