import streamlit as st
import pandas as pd

# Title
st.title("AI-Powered Aspect-Based Customer Feedback Analysis")

st.write("Welcome to my AI Project!")

# Read Dataset
data = pd.read_csv("dataset/customer_reviews.csv")

# Display Dataset
st.subheader("Customer Reviews Dataset")
st.dataframe(data)

# Dataset Statistics
st.subheader("Dataset Statistics")

total_reviews = len(data)
average_rating = data["Rating"].mean()
highest_rating = data["Rating"].max()
lowest_rating = data["Rating"].min()

st.write("Total Reviews :", total_reviews)
st.write("Average Rating :", round(average_rating,2))
st.write("Highest Rating :", highest_rating)
st.write("Lowest Rating :", lowest_rating)

# Search Reviews
st.subheader("Search Reviews")

search = st.text_input("Enter a keyword")

if search:
    filtered_data = data[data["Review"].str.contains(search, case=False)]

    st.write("Search Results")
    st.dataframe(filtered_data)