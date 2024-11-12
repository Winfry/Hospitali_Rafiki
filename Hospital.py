import streamlit as st
import pickle
import pandas as pd
import numpy

# Load the diabetes prediction model
model_path = 'diabetes_model.pkl'  
try:
    loaded_model = pickle.load(open(model_path, 'rb'))
except FileNotFoundError:
    st.error("Diabetes model file not found. Please ensure 'diabetes_model.pkl' is in the directory.")
    st.stop()

# Load hospital data
hospital_data_path = 'Hospitals.csv'  # Path to your hospital dataset
try:
    hospitals_df = pd.read_csv(hospital_data_path)
except FileNotFoundError:
    st.error("Hospital data file not found. Please ensure 'hospitals.csv' is in the directory.")
    st.stop()

# Title and description
st.title("Diabetes Prediction and Hospital Recommendation")
st.write("Get a quick prediction for diabetes and see hospitals recommended for diabetes care.")

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
        # Get the prediction and print its type and content for debugging
        prediction = loaded_model.predict(input_data_as_array)
        st.write(f"Raw Prediction Output: {prediction}")  # Show the raw output
        st.write(f"Prediction Type: {type(prediction)}")  # Show the type

        # Check if prediction is in the expected format (a list or array with at least one element)
        if isinstance(prediction, (list, tuple, np.ndarray)) and len(prediction) > 0:
            prediction_result = prediction[0]
            st.write(f"Prediction Result (First Element): {prediction_result}")  # Output for debugging

            # If the prediction indicates diabetes
            if prediction_result == 1:
                st.error("The model suggests that you may have diabetes.")
                
                # Display additional information and resources
                st.header("Managing Diabetes: Tips and Resources")
                st.write("If you're diagnosed with diabetes, consider the following lifestyle and diet tips:")
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
                
                if st.checkbox("Monitoring Blood Sugar Levels"):
                    st.write("Regular monitoring is essential. Consult a healthcare provider for guidance.")
                
                st.write("For more resources, visit the [American Diabetes Association](https://www.diabetes.org/) website.")

                # Recommend hospitals
                st.header("Recommended Hospitals for Diabetes Care")

                # Allow user to select their county for hospital recommendations
                selected_county = st.selectbox("Select Your County", hospitals_df['COUNTY'].unique())

                # Filter hospitals by selected county and specialized diabetes care
                recommended_hospitals = hospitals_df[(hospitals_df['COUNTY'] == selected_county) & 
                                                    (hospitals_df['SPECIALTY'] == "Diabetes")]

                if not recommended_hospitals.empty:
                    st.write("Here are hospitals in your area specializing in diabetes care:")
                    for index, row in recommended_hospitals.iterrows():
                        st.write(f"**{row['HOSPITAL_NAME']}**")
                        st.write(f"Location: {row['COUNTY']}")
                        st.write(f"Contact: {row['NHIF_OFFICE']}")
                        st.write("---")
                else:
                    st.write("No hospitals specializing in diabetes care found in your selected county.")

            # If the prediction does not indicate diabetes
            else:
                st.success("You are not likely to have diabetes according to this prediction.")

                # Display general healthy lifestyle recommendations
                st.header("General Tips for Staying Healthy")
                diet_plan = st.radio("Would you like to explore diet plans?", ("Yes", "No"))
                if diet_plan == "Yes":
                    st.write("Aim for a balanced diet rich in vegetables, lean proteins, and whole grains.")

                exercise_plan = st.radio("Interested in exercise recommendations?", ("Yes", "No"))
                if exercise_plan == "Yes":
                    st.write("Try brisk walking or other moderate activities for 30 minutes most days.")

                st.write("For more tips on staying healthy, check out [CDC Healthy Weight](https://www.cdc.gov/healthyweight/healthy_eating/index.html).")

        else:
            st.error("Unexpected format for prediction output.")

    except Exception as e:
        st.error(f"Error in prediction: {e}")

