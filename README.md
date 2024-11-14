# Hospitali_Rafiki

- Welcome to the NHIF-Friendly Hospitals and Dialysis Centers Recommendation System called Hospitali Rafiki. This Streamlit-based application helps users predict the likelihood of kidney disease using a trained machine learning model. Additionally, it provides hospital recommendations, specifically NHIF-friendly facilities and dialysis centers, based on the user’s location and medical needs.

# Features
Kidney Disease Prediction: A predictive model assesses the likelihood of kidney disease based on user-input health information.
NHIF-Friendly Hospital and Dialysis Centers Recommendation: Recommends nearby hospitals, focusing on those registered with the National Health Insurance Fund (NHIF), especially those with dialysis capabilities.
Resource Tips for Kidney Health: Offers guidelines for a healthy lifestyle, including diet and exercise tips to manage or prevent kidney disease.
Demo
<!-- Replace with an actual screenshot of your app if available -->

# Project Structure
App Interface: Built with Streamlit to provide an intuitive, user-friendly experience.
Machine Learning Model: A pre-trained model to predict the likelihood of kidney disease based on medical input data.
Hospital Data: Includes a dataset, cleaned_hospitals.csv, which stores details about NHIF-friendly hospitals and dialysis centers across counties.
Dataset
The project uses a dataset with information about NHIF-friendly hospitals and dialysis centers, containing the following columns:

- COUNTY: The county where the hospital is located.
- NHIF_OFFICE: NHIF office associated with the hospital.
- NHIF_HOSPITAL_CODE: Hospital code as per NHIF records.
- HOSPITAL_NAME: Name of the hospital.
- Setup Instructions
To set up and run this project locally:

# Clone this repository:
# bash
- Copy code
git clone https://github.com/Winfry/Hospitali_Rafiki.git

# Navigate to the project directory:
- bash
- Copy code
- cd nhif-hospital-recommendation

# Install dependencies:
- bash
- Copy code
pip install -r requirements.txt.
Ensure your dataset and model files (cleaned_hospitals.csv and diabetes_model.pkl) are in the project directory.
Run the Streamlit application:
- bash
- Copy code
streamlit run Hospital.py

# Usage
Open the app in your web browser.
Enter your health information to get a kidney disease prediction.
If at risk, receive recommendations for NHIF-friendly hospitals and dialysis centers nearby.
Explore general health resources for managing or preventing kidney disease.
Screenshots

# Prediction Section
<!-- C:\Users\Pc\Pictures\Screenshots\Screenshot 2024-11-14 161218.png -->

# Hospital Recommendation Section
<!-- C:\Users\Pc\Pictures\Screenshots\Screenshot 2024-11-14 160325.png  -->

Future Improvements
Adding a search filter to narrow down results by NHIF services, county, or hospital type.
Integrating more health tips specific to chronic kidney disease management.
Contributing
Contributions are welcome! Please fork this repository, create a new branch, and submit a pull request.

License