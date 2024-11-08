import streamlit as st
import pickle
import pandas as pd

# Load the diabetes prediction model
try:
    model_path = 'diabetes_model.pkl'
    loaded_model = pickle.load(open(model_path, 'rb'))
except FileNotFoundError:
    st.error("Diabetes model file not found. Please make sure 'diabetes_model.pkl' is in the directory.")
    st.stop()

# Load hospital dataset
try:
    hospital_data_path = 'Hospitals.csv'  # Adjust the path if needed
    hospital_data = pd.read_csv(hospital_data_path)
except FileNotFoundError:
    st.error("Hospital data file not found. Please make sure 'Hospitals.csv' is in the directory.")
    st.stop()

# App Title
st.title("Diabetes Prediction and Health Management")

# User Input
st.write("### Enter Your Health Data")
# Replace these with actual feature inputs for your model
input_data = {
    "Feature1": st.number_input("Enter value for Feature1", min_value=0.0),
    "Feature2": st.number_input("Enter value for Feature2", min_value=0.0),
    # Add additional inputs as needed by your model
}

# Prediction Button
if st.button("Predict Diabetes"):
    input_data_as_array = list(input_data.values())
    prediction = loaded_model.predict([input_data_as_array])

    # Scenario 1: If the person is predicted to have diabetes
    if prediction[0] == 1:
        st.warning("The model predicts a risk of diabetes.")
        
        # Follow-up Actions for Diabetes
        st.write("#### Recommended Next Steps:")
        
        # Option to find a hospital
        if st.checkbox("Find a nearby hospital"):
            county = st.selectbox("Select your county", hospital_data['COUNTY'].unique())
            nearby_hospitals = hospital_data[hospital_data['COUNTY'] == county]
            
            if not nearby_hospitals.empty:
                st.write("Here are some hospitals in your area:")
                st.dataframe(nearby_hospitals[['Hospital Name', 'Address', 'Contact Number', 'NHIF Accepted']])
            else:
                st.error("No hospitals found in the selected county.")
        
        # Option for diabetes management tips
        if st.checkbox("View diabetes management tips"):
            st.write("""
            - **Monitor your blood sugar regularly**.
            - **Maintain a balanced diet with low sugar intake**.
            - **Stay physically active; aim for at least 30 minutes daily**.
            - **Take prescribed medications consistently**.
            - **Consult your healthcare provider regularly**.
            """)

        # Feedback Widget
        st.text_input("Any questions or concerns you'd like to share?", key="feedback_diabetes")
    
    # Scenario 2: If the person is predicted to not have diabetes
    else:
        st.success("The model predicts that you do not have diabetes.")
        
        # Lifestyle Tips for Health Maintenance
        st.write("#### Tips to Maintain Your Health:")
        
        if st.checkbox("Healthy lifestyle tips"):
            st.write("""
            - **Eat a balanced diet rich in fruits, vegetables, and whole grains**.
            - **Exercise regularly**; aim for at least 30 minutes of physical activity most days.
            - **Stay hydrated and get enough sleep**.
            - **Avoid excessive sugar and processed foods**.
            """)

        # Health Topics Exploration
        topic = st.selectbox("Choose a health topic to learn more about:", 
                             ["Heart Health", "Healthy Eating", "Exercise and Fitness", "Mental Health"])
        
        if topic == "Heart Health":
            st.write("### Heart Health Tips")
            st.write("""
            - **Maintain a diet low in saturated fats**.
            - **Exercise regularly to keep your heart strong**.
            - **Monitor blood pressure and cholesterol levels**.
            """)
        elif topic == "Healthy Eating":
            st.write("### Healthy Eating Tips")
            st.write("""
            - **Incorporate more fruits and vegetables** into your meals.
            - **Limit sugary drinks and choose water instead**.
            - **Choose whole grains over refined grains**.
            """)
        elif topic == "Exercise and Fitness":
            st.write("### Exercise and Fitness Tips")
            st.write("""
            - **Aim for a mix of cardio, strength training, and flexibility exercises**.
            - **Start with small goals if you're new to exercising**.
            """)
        elif topic == "Mental Health":
            st.write("### Mental Health Tips")
            st.write("""
            - **Practice stress management techniques like meditation or journaling**.
            - **Seek support from friends, family, or mental health professionals**.
            - **Get adequate sleep and exercise regularly**.
            """)

        # Optional feedback from users who do not have diabetes
        st.text_input("Share your feedback or any other health concerns:", key="feedback_no_diabetes")

