import streamlit as st
from analysis import load_data
from model import train_model, predict
import pandas as pd

st.title("AI Productivity Analyzer")

df = load_data()
model = train_model(df)

st.subheader("Enter Today's Data")

study = st.slider("Study Hours", 0, 12)
sleep = st.slider("Sleep Hours", 0, 12)
phone = st.slider("Phone Usage", 0, 10)

if st.button("Predict Productivity"):
    result = predict(model, study, sleep, phone)
    st.success(f"Predicted Productivity: {result:.2f}")