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
st.write("Provide your health information for a quick diabetes risk assessment, along with hospital recommendations.Get a quick prediction and learn ways to improve your health! Diabetes is a chronic health condition that affects how the body processes blood sugar (glucose). When unmanaged, high blood sugar levels can lead to severe complications over time, impacting various organs and systems in the body, including the heart, blood vessels, nerves, eyes, and kidneys.By focusing on kidney health in our diabetes prediction and hospital recommendation system, we aim to support early intervention and provide valuable resources for those at risk, helping to prevent severe kidney-related issues.")
st.image("diabetes.jpg", caption="Understanding Diabetes", use_column_width=True)


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
            # Display an educational image about diabetes
            st.image("diab_info.jpg", caption="Understanding Diabetes", use_column_width=True)
            # Display diabetes management resources
            st.header("Resources for Managing Diabetes")
            st.write("Here are some tips and resources to help you manage diabetes:")
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
        else:
            st.success("GREAT!You are not likely to have diabetes according to this prediction.")
            
    except Exception as e:
        st.error(f"Error in prediction: {e}")
        st.stop()

# Hospital Recommendation Section
st.header("Hospital Recommendation Especially For Kidney Care")
st.write("Kidney health is essential for overall well-being, as kidneys filter waste and maintain the body’s fluid balance. In Kenya, the National Hospital Insurance Fund (NHIF) offers support for kidney care, covering dialysis and other treatments in approved hospitals. This makes vital kidney care more accessible, particularly for those managing chronic kidney diseases or diabetes-related complications.Here is a list of NHIF-accredited hospitals across Kenya are equipped to provide quality care, offering patients critical support in managing and improving their kidney health")
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

        


