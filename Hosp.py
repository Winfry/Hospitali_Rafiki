import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the diabetes prediction model
model_path = 'diabetes_model.pkl'
try:
    loaded_model = pickle.load(open(model_path, 'rb'))
except FileNotFoundError:
    st.error("Diabetes model file not found. Please ensure 'diabetes_model.pkl' is in the directory.")
    st.stop()

# Load hospital data
hospital_data_path = 'cleaned_hospitals.csv'
try:
    hospitals_df = pd.read_csv(hospital_data_path)
except FileNotFoundError:
    st.error("Hospital data file not found. Please ensure 'cleaned_hospitals.csv' is in the directory.")
    st.stop()

# Title and description
st.title("Diabetes Prediction and Hospital Recommendation System")
st.write("Provide your health information for a quick diabetes risk assessment, along with hospital recommendations.")

# Collect input data for prediction
st.header("Please Enter Your Health Information")
input_data = {
    "Age": st.number_input("Age", min_value=0),
    "Blood Pressure": st.number_input("Blood Pressure", min_value=0.0),
    "Specific Gravity": st.number_input("Specific Gravity", min_value=0.0),
    "Albumin": st.number_input("Albumin", min_value=0.0),
    "Sugar": st.number_input("Sugar", min_value=0.0),
    "Blood Glucose Random": st.number_input("Blood Glucose Random", min_value=0.0),
    "Blood Urea": st.number_input("Blood Urea", min_value=0.0),
    "Serum Creatinine": st.number_input("Serum Creatinine", min_value=0.0),
    "Sodium": st.number_input("Sodium", min_value=0.0),
    "Potassium": st.number_input("Potassium", min_value=0.0),
    "Hemoglobin": st.number_input("Hemoglobin", min_value=0.0),
    "Packed Cell Volume": st.number_input("Packed Cell Volume", min_value=0.0),
}

# Convert input data to array format
input_data_as_array = np.array(list(input_data.values())).reshape(1, -1)

# Predict diabetes risk and show result
if st.button("Predict"):
    try:
        prediction = loaded_model.predict(input_data_as_array)
        if prediction[0] == 1:
            st.error("The model suggests that you may have diabetes.")
        else:
            st.success("You are not likely to have diabetes according to this prediction.")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
        st.stop()

# Hospital Recommendation Section
st.header("Hospital Recommendation")
selected_county = st.selectbox("Select Your County", hospitals_df['COUNTY'].unique())

# Filter and display hospitals in the selected county
recommended_hospitals = hospitals_df[hospitals_df['COUNTY'] == selected_county]
if not recommended_hospitals.empty:
    st.write("Recommended hospitals in your area:")
    for _, row in recommended_hospitals.iterrows():
        st.write(f"**{row['HOSPITAL_NAME']}**")
        st.write(f"NHIF Office: {row['NHIF_OFFICE']}")
        st.write(f"Hospital Code: {row['NHIF_HOSPITAL_CODE']}")
        st.write("---")
else:
    st.write("No hospitals found in the selected county.")

        


