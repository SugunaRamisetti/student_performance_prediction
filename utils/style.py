import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
    /* Global Font and Background styling */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }
    
    /* App background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* Metric Cards Premium Styling */
    div[data-testid="stMetricValue"] {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1f77b4;
    }
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.5);
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.25);
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #2b303b;
    }
    
    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #1f77b4 0%, #2ca02c 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        color: white;
    }

    /* Headers and Titles */
    h1, h2, h3 {
        color: #2c3e50;
        font-weight: 800;
    }

    /* Form and Inputs */
    .stNumberInput input, .stSelectbox, .stSlider {
        border-radius: 8px;
        border: 1px solid #d1d8e0;
    }

    /* Card styling for Markdown */
    .premium-card {
        background: white;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    .premium-card h4 {
        color: #1f77b4;
        margin-top: 0;
    }
    </style>
    """, unsafe_allow_html=True)
