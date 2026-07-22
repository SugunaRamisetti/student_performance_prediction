import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Add parent directory to path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.data_processing import get_data
from utils.style import inject_custom_css

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")
inject_custom_css()

st.title("📊 Data Exploration Dashboard")
st.markdown("Explore the **real** student performance dataset from your Jupyter notebook.")

# Load data - rename function to clear old streamlit cache
@st.cache_data
def load_real_data():
    return get_data()

df = load_real_data()

# Overview
st.header("Dataset Overview")
st.dataframe(df.head(10))

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Students", len(df))
with col2:
    st.metric("Average Final Exam", f"{df['Final_Exam'].mean():.2f}")
with col3:
    st.metric("Average Study Hours", f"{df['Study_Hours'].mean():.2f}")

st.markdown("---")

# Visualizations
st.header("Visualizations")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribution of Final Exam Scores")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df['Final_Exam'], bins=30, kde=True, ax=ax, color='skyblue')
    st.pyplot(fig)

with col2:
    st.subheader("Study Hours vs. Final Exam")
    fig, ax = plt.subplots(figsize=(8, 5))
    # We map performance level to text for the legend
    perf_map = {0: "Poor", 1: "Average", 2: "Good", 3: "Excellent"}
    df['Perf_Label'] = df['Performance_Level'].map(perf_map)
    sns.scatterplot(x='Study_Hours', y='Final_Exam', hue='Perf_Label', data=df, ax=ax, palette='viridis')
    st.pyplot(fig)

st.markdown("---")

st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(12, 8))
numeric_df = df.select_dtypes(include=["int64", "float64"])
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
st.pyplot(fig)
