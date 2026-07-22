import streamlit as st
import os
import sys
from PIL import Image

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.style import inject_custom_css

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    inject_custom_css()
    
    # 1st Title in Capital Letters
    st.markdown("<h1 style='text-align: center; color: #1f77b4; font-weight: 900; text-transform: uppercase;'>🎓 AI-POWERED STUDENT SUCCESS PREDICTOR</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #7f8c8d; margin-bottom: 20px;'>Harnessing the power of Machine Learning to analyze and predict academic performance.</p>", unsafe_allow_html=True)

    # Hero Image (Thumbnail)
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'ML.png')
    if os.path.exists(image_path):
        img = Image.open(image_path)
        st.image(img, use_container_width=True)
    else:
        st.error(f"Image not found at {image_path}")

    st.markdown("<br>", unsafe_allow_html=True)

    # Feature Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="premium-card">
            <h4>📊 Data Driven</h4>
            <p>Trained on a robust real-world dataset of over 30,000 student records, capturing detailed demographics, habits, and academic history.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="premium-card">
            <h4>🧠 Advanced ML</h4>
            <p>Utilizes a highly optimized Random Forest Classifier with real-time feature engineering for precise performance categorization.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="premium-card">
            <h4>📈 Actionable Insights</h4>
            <p>Explore interactive dashboards, correlation heatmaps, and confusion matrices to deeply understand what drives student success.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    st.markdown("""
    ### 👈 Get Started
    Use the sidebar on the left to navigate:
    - **1_Dashboard**: Explore the raw data and distributions.
    - **2_Prediction**: Test the model with custom student profiles.
    - **3_Data_Insights**: Deep dive into variable correlations.
    - **4_Model_Performance**: Analyze the Random Forest accuracy and precision.
    """)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid #d1d8e0; color: #7f8c8d; font-size: 0.9rem; font-weight: 600;">
        BUILT BY KICKSTACK SUMMER AI/ML INTERNSHIPS
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
