import streamlit as st
import pickle
import pandas as pd
import numpy as np  # Import numpy to handle np.ndarray

# Load the diabetes prediction model
model_path = 'diabetes_model.pkl'  
try:
    loaded_model = pickle.load(open(model_path, 'rb'))
except FileNotFoundError:
    st.error("Diabetes model file not found. Please ensure 'diabetes_model.pkl' is in the directory.")
    st.stop()

# Load hospital data
hospital_data_path = 'hospitals.csv'  # Path to your hospital dataset
try:
    hospitals_df = pd.read_csv(hospital_data_path)
except FileNotFoundError:
    st.error("Hospital data file not found. Please ensure 'hospitals.csv' is in the directory.")
    st.stop()

# Title and description
st.title("Diabetes Prediction and Hospital Recommendation")
st.write("Get a quick prediction for diabetes and see hospitals recommended for diabetes care or general check-ups.")

# Collect input data from the user for prediction
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

# Predict diabetes based on the input data
if st.button("Predict"):
    # Convert input data to the format expected by the model
    input_data_as_array = [list(input_data.values())]

    try:
        # Get the prediction
        prediction = loaded_model.predict(input_data_as_array)
        prediction_result = prediction[0]

        if prediction_result == 1:
            st.error("The model suggests that you may have diabetes.")
            
            # Display diabetes management resources
            st.header("Managing Diabetes: Tips and Resources")
            st.write("If you're diagnosed with diabetes, consider these lifestyle tips:")
            if st.checkbox("Diet and Nutrition Tips"):
                st.write("""
                    - Choose fiber-rich foods like vegetables, fruits, and whole grains.
                    - Avoid sugary drinks and high-sugar foods.
                    - Include lean proteins and healthy fats.
                """)
            
            if st.checkbox("Exercise Recommendations"):
                st.write("""
                    - Aim for 150 minutes of moderate exercise per week.
                    - Try walking, cycling, or low-impact activities.
                    - Add strength training exercises as well.
                """)
            
            st.write("For more resources, visit the [American Diabetes Association](https://www.diabetes.org/) website.")

            # Hospital recommendation for diabetes care
            st.header("Recommended Hospitals for Diabetes Care")

            selected_county = st.selectbox("Select Your County", hospitals_df['COUNTY'].unique())
            recommended_hospitals = hospitals_df[(hospitals_df['COUNTY'] == selected_county) & 
                                                (hospitals_df['SPECIALTY'] == "Diabetes")]

            if not recommended_hospitals.empty:
                st.write("Hospitals in your area specializing in diabetes care:")
                for _, row in recommended_hospitals.iterrows():
                    st.write(f"**{row['HOSPITAL_NAME']}**")
                    st.write(f"Location: {row['COUNTY']}")
                    st.write(f"Contact: {row['NHIF_OFFICE']}")
                    st.write("---")
            else:
                st.write("No specialized diabetes hospitals found in your selected county.")

        else:
            st.success("You are not likely to have diabetes according to this prediction.")

            # Healthy lifestyle recommendations
            st.header("General Tips for Staying Healthy")
            if st.radio("Explore Diet Plans", ["Yes", "No"]) == "Yes":
                st.write("Try a balanced diet with vegetables, lean proteins, and whole grains.")
            
            if st.radio("Exercise Recommendations", ["Yes", "No"]) == "Yes":
                st.write("Consider brisk walking or other moderate activities for 30 minutes most days.")

            st.write("For more tips, visit [CDC Healthy Weight](https://www.cdc.gov/healthyweight/healthy_eating/index.html).")

            # Hospital recommendation for general check-up
            st.header("Hospitals for General Check-Up")

            selected_county = st.selectbox("Select Your County for Check-Up", hospitals_df['COUNTY'].unique())
            hospitals_in_county = hospitals_df[hospitals_df['COUNTY'] == selected_county]

            if not hospitals_in_county.empty:
                st.write("Hospitals in your area available for a general check-up:")
                for _, row in hospitals_in_county.iterrows():
                    st.write(f"**{row['HOSPITAL_NAME']}**")
                    st.write(f"Location: {row['COUNTY']}")
                    st.write(f"Contact: {row['NHIF_OFFICE']}")
                    st.write("---")
            else:
                st.write("No hospitals found in your selected county for general check-up.")

    except Exception as e:
        st.error(f"Error in prediction: {e}")
