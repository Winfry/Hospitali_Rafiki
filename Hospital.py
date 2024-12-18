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
st.title("Chronic Kidney Disease Prediction and Hospital Recommendation System")
st.write("Chronic kidney disease (CKD) is a long-term condition where the kidneys gradually lose function, impacting their ability to filter waste and excess fluids from the blood. Often caused by conditions like diabetes and high blood pressure, CKD progresses slowly and may not show symptoms until significant damage has occurred. Managing CKD early can slow its progression and help prevent complications, highlighting the importance of regular check-ups and a proactive approach to kidney health.")
st.image("chronic-kidney-disease-.jpg", caption="Keeping The Kidneys Healthy!", use_column_width=True)


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
            st.error("The model suggests that you may have A Kidney Disease.")
            
        else:
            st.success("GREAT!You are not likely to have a Kidney disease according to this prediction.")
            st.write("For additional support, consider visiting a healthcare provider for regular check-ups, even if no issues are detected. Keeping a proactive approach is key to long-term kidney health!")
            st.image("healthy_lifestyle.jpg", caption="Understanding Chronic Kidney Disease", use_column_width=True)

            # Show general resources for kidney health
            st.header("Resources for Maintaining Kidney Health")
            if st.checkbox("Diet and Nutrition Tips for Kidney Health"):
                st.write("""
                    - Stay hydrated by drinking water throughout the day.
                    - Limit salt intake to reduce kidney strain.
                    - Include fresh fruits and vegetables in your diet.
                """)
            
            if st.checkbox("Exercise Recommendations for Kidney Health"):
                st.write("""
                    - Engage in regular physical activity like walking, cycling, or swimming.
                    - Aim for 30 minutes a day to support overall kidney health.
                    - Avoid high-protein diets, as excess protein can overwork the kidneys.
                """)

    except Exception as e:
        st.error(f"Error in prediction: {e}")

# Hospital Recommendation Section
st.header("Hospital Recommendation")
county_location = st.selectbox("Select Your Location", hospitals_df['COUNTY'].unique())
hospital_code = st.selectbox("Select NHIF Hospital Code ", hospitals_df['NHIF_HOSPITAL_CODE'].unique())

# Function to recommend hospitals
def recommend_hospitals(COUNTY, NHIF_HOSPITAL_CODE):
    filtered_hospitals = hospitals_df[
        (hospitals_df['COUNTY'] == county_location) &
        (hospitals_df['NHIF_HOSPITAL_CODE'] == hospital_code)
    ]
    
    if filtered_hospitals.empty:
        return "No hospitals found for the selected criteria."
    
    return filtered_hospitals

# Recommendation button
if st.button("Get Recommendations"):
    recommended_hospitals = recommend_hospitals(county_location, hospital_code)
    st.write(recommended_hospitals)
    

        