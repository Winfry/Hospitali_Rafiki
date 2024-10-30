import streamlit as st
import pandas as pd

# Load the dataset
df_hospitals = pd.read_csv("your_hospital_data.csv")  # Update with your CSV file name

# Streamlit app
st.title("Hospital Recommendation System")

# User inputs
location = st.selectbox("Select Your Location", df_hospitals['Location'].unique())
specialization = st.selectbox("Select Specialization", df_hospitals['Specialization'].unique())

# Function to recommend hospitals
def recommend_hospitals(location, specialization):
    filtered_hospitals = df_hospitals[
        (df_hospitals['Location'] == location) &
        (df_hospitals['Specialization'] == specialization)
    ]
    
    if filtered_hospitals.empty:
        return "No hospitals found for the selected criteria."
    
    return filtered_hospitals

# Recommendation button
if st.button("Get Recommendations"):
    recommended_hospitals = recommend_hospitals(location, specialization)
    st.write(recommended_hospitals)

