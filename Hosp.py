import streamlit as st
import pandas as pd

# Load hospital data
hospital_data_path = 'cleaned_hospitals.csv'  # Path to your hospital dataset
try:
    hospitals_df = pd.read_csv(hospital_data_path)
except FileNotFoundError:
    st.error("Hospital data file not found. Please ensure 'cleaned_hospitals.csv' is in the directory.")
    st.stop()

# Title and description
st.title("Hospital Recommendation System")
st.write("Select your county to find recommended hospitals in your area.")

# Select county
county_selected = st.selectbox("Select Your County", hospitals_df['COUNTY'].unique())

# Filter hospitals by selected county
recommended_hospitals = hospitals_df[hospitals_df['COUNTY'] == county_selected]

# Display recommended hospitals
if not recommended_hospitals.empty:
    st.write("Hospitals in your selected county:")
    for _, row in recommended_hospitals.iterrows():
        st.write(f"**{row['HOSPITAL_NAME']}**")
        st.write(f"NHIF Office: {row['NHIF_OFFICE']}")
        st.write(f"Hospital Code: {row['NHIF_HOSPITAL_CODE']}")
        st.write("---")
else:
    st.write("No hospitals found in the selected county.")

        


