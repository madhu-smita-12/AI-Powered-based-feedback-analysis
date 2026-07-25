import streamlit as st
import pandas as pd

st.title("AI-Powered Aspect-Based Customer Feedback Analysis")

st.write("Welcome to my AI Project!")
# Read Dataset
data = pd.read_csv("dataset/customer_reviews.csv")

# Display Dataset
st.subheader("Customer Reviews Dataset")
st.dataframe(data)