import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys

# Add parent directory to path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.data_processing import get_data
from utils.style import inject_custom_css

st.set_page_config(page_title="Data Insights", page_icon="📈", layout="wide")
inject_custom_css()

st.title("📈 Data Insights")
st.markdown("Deep dive into the real student performance dataset with interactive visualizations.")

# Load data
@st.cache_data
def load_data():
    df = get_data()
    # Map the numerical Performance Level back to strings for better visualization
    perf_map = {0: "Poor", 1: "Average", 2: "Good", 3: "Excellent"}
    if "Performance_Level" in df.columns:
        df["Performance_Label"] = df["Performance_Level"].map(perf_map)
    return df

df = load_data()

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribution of Performance Levels")
    if "Performance_Label" in df.columns:
        fig1 = px.histogram(
            df, 
            x="Performance_Label", 
            color="Performance_Label",
            category_orders={"Performance_Label": ["Poor", "Average", "Good", "Excellent"]},
            title="Count of Students by Performance"
        )
        st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Attendance vs. Performance Level")
    if "Attendance" in df.columns and "Performance_Label" in df.columns:
        fig2 = px.box(
            df, 
            x="Performance_Label", 
            y="Attendance",
            color="Performance_Label",
            category_orders={"Performance_Label": ["Poor", "Average", "Good", "Excellent"]},
            title="Attendance Distribution per Level"
        )
        st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

st.subheader("Correlation Heatmap")
# Only plot correlations for numerical features
numeric_df = df.select_dtypes(include=["int64", "float64"])
fig3 = px.imshow(
    numeric_df.corr().round(2), 
    text_auto=True, 
    aspect="auto",
    color_continuous_scale="RdBu_r",
    title="Feature Correlation"
)
st.plotly_chart(fig3, use_container_width=True)
