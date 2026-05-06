import streamlit as st
import pandas as pd

df = pd.read_csv(r"E:\Practice_Datasets\creditcard.csv")

st.title("💳 Credit Card Fraud Analysis")

# Show data
if st.checkbox("Show Data"):
    st.write(df.head())

# Class distribution
st.subheader("Fraud vs Normal")
st.bar_chart(df["Class"].value_counts())

# Pivot table
st.subheader("Pivot Table (Amount vs Class)")
pivot = df.pivot_table(values="Amount", index="Class", aggfunc="mean")
st.write(pivot)

# Amount filter
amount = st.slider("Select Amount", 0, 5000, 1000)
st.write(df[df["Amount"] > amount])
