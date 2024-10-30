import streamlit as st
import pandas as pd

# Load the dataset
df_hospitals = pd.read_csv("Hospitals.csv")  # Update with your CSV file name

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
    
#The NEW ONE     
    
import streamlit as st
import pandas as pd
import joblib  # for loading the trained model

# Load your diabetes prediction model
diabetes_model = joblib.load("diabetes_model.pkl")

# Load your hospital dataset
df_hospitals = pd.read_csv("Hospitals.csv")

# Function for diabetes prediction
def predict_diabetes(input_data):
    prediction = diabetes_model.predict([input_data])
    return "Diabetic" if prediction[0] == 1 else "Not Diabetic"

# Streamlit UI
st.title("Dialysis Hospital Recommendation and Diabetes Prediction")

# Diabetes Prediction Inputs
st.header("Diabetes Prediction")
age = st.number_input("Age", min_value=0)
glucose_level = st.number_input("Glucose Level", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)

# Gather input data for prediction
input_data = [age, glucose_level, blood_pressure]  # Add more features as needed

if st.button("Predict Diabetes"):
    result = predict_diabetes(input_data)
    st.write(f"Prediction: {result}")

# Hospital Recommendation Section
st.header("Hospital Recommendation")
county_location = st.selectbox("Select Your Location", df_hospitals['COUNTY'].unique())
hospital_code = st.selectbox("Select NHIF Hospital Code ", df_hospitals['NHIF HOSPITAL CODE'].unique())

# Function to recommend hospitals
def recommend_hospitals(COUNTY, NHIF HOSPITAL CODE):
    filtered_hospitals = df_hospitals[
        (df_hospitals['COUNTY'] == county_location) &
        (df_hospitals['NHIF HOSPITAL CODE'] == hospital_code)
    ]
    
    if filtered_hospitals.empty:
        return "No hospitals found for the selected criteria."
    
    return filtered_hospitals

# Recommendation button
if st.button("Get Recommendations"):
    recommended_hospitals = recommend_hospitals(location, specialization)
    st.write(recommended_hospitals)
    

