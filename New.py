import streamlit as st
import pandas as pd
import numpy as np

# Load the dataset (replace 'hospitals.csv' with your extracted CSV file)
@st.cache
def load_data():
    data = pd.read_csv("cleaned_hospitals.csv")
    return data

df = load_data()

st.title("Hospital Recommender System")
st.markdown("Easily find hospitals based on your preferences.")

# Filter options
county = st.selectbox("Select County", ["All"] + df["COUNTY"].unique().tolist())
hospital_name = st.text_input("Search Hospital Name (optional)")

# Apply filters
filtered_df = df
if county != "All":
    filtered_df = filtered_df[filtered_df["COUNTY"] == county]
if hospital_name:
    filtered_df = filtered_df[filtered_df["HOSPITAL_NAME"].str.contains(hospital_name, case=False, na=False)]

st.write(f"### Results ({len(filtered_df)} Hospitals Found)")
st.dataframe(filtered_df)
