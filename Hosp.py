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
hospital_data_path = 'Hospitals.csv'
try:
    hospitals_df = pd.read_csv(hospital_data_path)
except FileNotFoundError:
    st.error("Hospital data file not found. Please ensure 'Hospitals.csv' is in the directory.")
    st.stop()

# Title and description
st.title("Diabetes Prediction and Hospital Recommendation")
st.write("Get a quick prediction and learn ways to improve your health.")

# Collect user health information for prediction
st.header("Enter Your Health Information")
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

# Prediction and recommendations
if st.button("Predict"):
    # Convert input data to the model's expected format
    input_data_as_array = np.array(list(input_data.values())).reshape(1, -1)

    try:
        # Get the prediction
        prediction = loaded_model.predict(input_data_as_array)
        prediction_result = prediction[0]

        # Hospital recommendations based on diabetes prediction
        selected_county = st.selectbox("Select Your County", hospitals_df['COUNTY'].unique())

        if prediction_result == 1:
            st.error("The model suggests that you may have diabetes.")
            st.image("diab_info.jpg", caption="Understanding Diabetes", use_column_width=True)

            st.header("Recommended Hospitals for Diabetes Care")
            recommended_hospitals = hospitals_df[(hospitals_df['COUNTY'] == selected_county) & 
                                                 (hospitals_df['SPECIALTY'].str.contains("Diabetes", case=False, na=False))]

            if not recommended_hospitals.empty:
                for _, row in recommended_hospitals.iterrows():
                    st.write(f"**{row['HOSPITAL_NAME']}** - {row['COUNTY']}")
                    st.write(f"Contact: {row['NHIF_OFFICE']}")
                    st.write("---")
            else:
                st.write("No specialized diabetes hospitals found in your selected county.")
        
        else:
            st.success("You are not likely to have diabetes according to this prediction.")
            st.image("healthy_lifestyle.jpg", caption="Stay Healthy!", use_column_width=True)

            st.header("Hospitals for General Check-Up")
            hospitals_in_county = hospitals_df[hospitals_df['COUNTY'] == selected_county]

            if not hospitals_in_county.empty:
                for _, row in hospitals_in_county.iterrows():
                    st.write(f"**{row['HOSPITAL_NAME']}** - {row['COUNTY']}")
                    st.write(f"Contact: {row['NHIF_OFFICE']}")
                    st.write("---")
            else:
                st.write("No hospitals found in your selected county for a general check-up.")

    except Exception as e:
        st.error(f"Error in prediction: {e}")
