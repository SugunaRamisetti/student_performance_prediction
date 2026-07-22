import os
import pickle
import streamlit as st

@st.cache_resource
def load_model_from_disk():
    """
    Loads the trained machine learning model from the model directory.
    Returns None if the model is not found.
    """
    model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'model', 'model.pkl')
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    return None

def format_prediction_output(prediction):
    """
    Returns HTML formatted string for the prediction output based on the Performance Level (0-3).
    """
    mapping = {
        0: ("Poor", "#d62728"),     # Red
        1: ("Average", "#ff7f0e"),  # Orange
        2: ("Good", "#2ca02c"),     # Green
        3: ("Excellent", "#1f77b4") # Blue
    }
    
    status, color = mapping.get(prediction, ("Unknown", "#333333"))
    
    return f"""
    <div style="background-color:#f0f2f6;padding:20px;border-radius:10px;text-align:center;">
        <h2 style="color:#333333;margin:0;">Predicted Performance Level</h2>
        <h1 style="color:{color};font-size:48px;margin:10px 0;">{status}</h1>
    </div>
    """
