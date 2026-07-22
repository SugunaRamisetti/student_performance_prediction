import streamlit as st
import os
import sys
import pickle
import pandas as pd

# Add parent directory to path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.helper import load_model_from_disk, format_prediction_output
from utils.preprocessing import prepare_input_data
from utils.prediction import get_prediction
from utils.style import inject_custom_css

st.set_page_config(page_title="Prediction", page_icon="🔮", layout="wide")
inject_custom_css()

st.title("🔮 Predict Student Performance Level")
st.markdown("Enter the student's details below to predict their performance category (Poor, Average, Good, or Excellent).")

# Load the trained model using our helper function
model = load_model_from_disk()

# We also need to load the feature list to ensure correct column order
@st.cache_resource
def load_feature_names_from_disk():
    features_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'model', 'features.pkl')
    if os.path.exists(features_path):
        with open(features_path, 'rb') as f:
            return pickle.load(f)
    return None

features = load_feature_names_from_disk()

if model is None or features is None:
    st.error("Model or features list not found! Please run `model/train_model.py` first to train and save the model.")
    st.stop()

# Input form
with st.form("prediction_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Demographics")
        age = st.number_input("Age", min_value=15, max_value=30, value=18, step=1)
        gender = st.selectbox("Gender", options=["Male", "Female"])
        parent_edu = st.selectbox("Parent Education", options=["No Formal Education", "Primary", "High School", "Diploma", "Bachelor Degree", "Master Degree", "Ph.D"])
        income = st.number_input("Family Income (Annual)", min_value=0.0, value=45000.0, step=1000.0)
        
    with col2:
        st.subheader("Habits")
        study_hours = st.number_input("Study Hours (per week)", min_value=0.0, max_value=60.0, value=15.0, step=0.5)
        sleep_hours = st.number_input("Sleep Hours (per night)", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
        internet = st.selectbox("Internet Access", options=["No", "Yes"])
        
    with col3:
        st.subheader("Academics")
        attendance = st.slider("Attendance Rate (%)", min_value=0, max_value=100, value=85)
        previous_grade = st.number_input("Previous Grade (0-100)", min_value=0.0, max_value=100.0, value=75.0, step=1.0)
        final_exam = st.number_input("Final Exam Score (0-100)", min_value=0.0, max_value=100.0, value=78.0, step=1.0)
        assignments = st.number_input("Assignments Score (0-100)", min_value=0.0, max_value=100.0, value=80.0, step=1.0)

    submit_button = st.form_submit_button(label="Predict Performance Level")

if submit_button:
    # 1. Preprocess input data
    input_df = prepare_input_data(
        age, gender, attendance, study_hours, internet, 
        parent_edu, income, sleep_hours, assignments, 
        previous_grade, final_exam
    )
    
    # Reorder columns to match the model training exactly
    input_df = input_df[features]
    
    # 2. Make prediction
    with st.spinner("Predicting..."):
        prediction = get_prediction(model, input_df)
    
    # 3. Display result
    st.success("Prediction Complete!")
    
    # Format the output beautifully using our helper
    formatted_output = format_prediction_output(prediction)
    st.markdown(formatted_output, unsafe_allow_html=True)
    
    if prediction >= 2: # Good or Excellent
        st.balloons()
