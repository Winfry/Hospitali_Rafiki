import streamlit as st
import pickle
import pandas as pd

# Load the diabetes model
model_path = 'diabetes_model.pkl'  # Replace with the correct path if necessary
try:
    loaded_model = pickle.load(open(model_path, 'rb'))
except FileNotFoundError:
    st.error("Diabetes model file not found. Please make sure 'diabetes_model.sav' is in the directory.")
    st.stop()

# Load the hospital dataset
hospital_data_path = 'Hospitals.csv'  # Replace with the actual path of your hospital dataset
try:
    hospital_data = pd.read_csv(hospital_data_path)
except FileNotFoundError:
    st.error("Hospital data file not found. Please make sure 'hospital_data.csv' is in the directory.")
    st.stop()

# User inputs for diabetes prediction
st.title("Diabetes Prediction and Hospital Recommendation")

st.write("Please enter your health data for diabetes prediction.")

# Collect input data
# Replace these with your model's required inputs
input_data = {
    "Feature1": st.number_input("Enter value for Feature1", min_value=0.0),
    "Feature2": st.number_input("Enter value for Feature2", min_value=0.0),
    # Add more features as required by your model
}

# Prediction button
if st.button("Predict Diabetes"):
    input_data_as_array = list(input_data.values())
    prediction = loaded_model.predict([input_data_as_array])

    if prediction[0] == 1:
        st.warning("You may have diabetes. We recommend consulting with a healthcare provider.")

        # Recommend nearby hospitals based on user location input
        county = st.selectbox("Select your county", hospital_data['COUNTY'].unique())
        
        filtered_hospitals = hospital_data[hospital_data['COUNTY'] == county]

        if not filtered_hospitals.empty:
            st.write("Here are some hospitals in your area:")
            st.dataframe(filtered_hospitals[['Hospital Name', 'Address', 'Contact Number', 'NHIF Accepted']])
        else:
            st.error("No hospitals found in the selected county.")
    else:
        st.success("You do not have diabetes according to this model.")

