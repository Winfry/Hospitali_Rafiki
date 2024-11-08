import streamlit as st
import pickle
import pandas as pd

# Load the diabetes model
model_path = 'diabetes_model.pkl'
try:
    loaded_model = pickle.load(open(model_path, 'rb'))
except FileNotFoundError:
    st.error("Diabetes model file not found. Please make sure 'diabetes_model.pkl' is in the directory.")
    st.stop()

# Load hospital data
hospital_data_path = 'hospitals.csv'  # Path to your hospital dataset
try:
    hospitals_df = pd.read_csv(hospital_data_path)
except FileNotFoundError:
    st.error("Hospital data file not found. Please ensure 'hospitals.csv' is in the directory.")
    st.stop()

# Title and subtitle
st.title("Diabetes Prediction and Wellness Guide")
st.write("Get a quick prediction and learn ways to improve your health!")
st.image("diabetes.jpg", caption="Understanding Diabetes", use_column_width=True)

# Collect input data from the user for prediction
st.header("Please Enter Your Health Information")
input_data = {
    "Age": st.number_input("Enter value for Age", min_value=0.0),
    "Sugar Level": st.number_input("Enter value for Sugar Level", min_value=0.0),
    "Blood Pressure": st.number_input("Enter value for Blood Pressure", min_value=0.0),
    "Sodium": st.number_input("Enter value for Sodium", min_value=0.0),
    "Blood Urea": st.number_input("Enter value for Blood Urea", min_value=0.0),
    "Haemoglobin": st.number_input("Enter value for Haemoglobin", min_value=0.0),
}

# Predict diabetes based on the input data
if st.button("Predict"):
    input_data_as_array = list(input_data.values())
    prediction = loaded_model.predict([input_data_as_array])

    # If the prediction indicates diabetes
    if prediction[0] == 1:
        st.error("The model suggests that you may have diabetes.")

        # Display an educational image about diabetes
        st.image("diab_info.jpg", caption="Understanding Diabetes", use_column_width=True)

        # Widgets to provide resources and lifestyle tips
        st.header("Resources for Managing Diabetes")
        
        st.write("Here are some tips and resources to help you manage diabetes:")
        if st.checkbox("Diet and Nutrition Tips"):
            st.write("""
                - Choose foods rich in fiber (whole grains, vegetables, fruits).
                - Avoid sugary drinks and limit high-sugar foods.
                - Include lean proteins and healthy fats.
            """)
        
        if st.checkbox("Exercise Recommendations"):
            st.write("""
                - Aim for at least 150 minutes of moderate exercise each week.
                - Try low-impact activities, like walking or cycling.
                - Incorporate strength training exercises.
            """)
        
        if st.checkbox("Track Blood Sugar Levels"):
            st.write("Monitoring your blood sugar levels regularly is essential. Speak to a healthcare provider for guidance.")

        st.write("For more information, check out this [link to diabetes care resources](https://www.diabetes.org/)")

        # Recommend hospitals
        st.header("Recommended Hospitals for Diabetes Care")
        
        # Filter hospitals based on your criteria, e.g., those with a diabetes specialty
        recommended_hospitals = hospitals_df[hospitals_df['COUNTY'].str.contains('COUNTY', case=False, na=False)]
        
        if not recommended_hospitals.empty:
            for index, row in recommended_hospitals.iterrows():
                st.write(f"**{row['HOSPITAL_NAME']}**")
                st.write(f"Location: {row['COUNTY']}")
                st.write(f"Office: {row['NHIF_OFFICE']}")
                st.write("---")
        else:
            st.write("No hospitals specializing in diabetes care found in your area.")

    # If the prediction does not indicate diabetes
    else:
        st.success("Great news! You are not likely to have diabetes according to this prediction.")

        # Display a healthy lifestyle image
        st.image("healthy_lifestyle.jpg", caption="Stay Healthy!", use_column_width=True)

        # Interactive widgets to promote a healthy lifestyle
        st.header("Tips for Staying Healthy")

        diet_plan = st.radio(
            "Would you like to explore diet plans?",
            ("Yes", "No")
        )
        if diet_plan == "Yes":
            st.write("Try to focus on a balanced diet rich in vegetables, lean proteins, and whole grains.")

        exercise_plan = st.radio(
            "Interested in exercise recommendations?",
            ("Yes", "No")
        )
        if exercise_plan == "Yes":
            st.write("Engage in regular physical activity, like brisk walking, for at least 30 minutes most days of the week.")

        st.write("For more tips on maintaining a healthy lifestyle, check out the resources [here](https://www.cdc.gov/healthyweight/healthy_eating/index.html).")
