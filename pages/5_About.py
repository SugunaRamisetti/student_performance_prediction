import streamlit as st
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.style import inject_custom_css

st.set_page_config(page_title="About", page_icon="ℹ️", layout="centered")
inject_custom_css()

st.title("ℹ️ About This Project")

st.markdown("""
### Overview
The **Student Performance Prediction App** is an educational machine learning project designed to demonstrate how various factors influence a student's academic success.

### Machine Learning Model
We use a **Random Forest Classifier** trained on a real-world dataset of over 30,000 students. The model categorizes students into four distinct Performance Levels: Poor, Average, Good, and Excellent.

#### Features Analyzed:
- **Demographics**: Age, Gender, Family Income, Parent Education.
- **Habits**: Study Hours, Sleep Hours, Internet Access.
- **Academics**: Attendance Rate, Previous Grade, Assignments Score, Final Exam Score.

#### Engineered Features (Calculated Automatically):
- **Study Efficiency**: Ratio of study hours factoring in attendance.
- **Academic Consistency**: Average of previous and current grades.
- **Study-Sleep Ratio**: Balance between studying and resting.
- **Digital Learning Score**: Impact of internet access on study time.

### Technology Stack
- **Frontend**: Streamlit
- **Data Manipulation**: Pandas & NumPy
- **Machine Learning**: Scikit-Learn
- **Visualizations**: Matplotlib, Seaborn, and Plotly

---
*Created as a demonstration of building interactive ML apps with Python and Streamlit.*
""")
