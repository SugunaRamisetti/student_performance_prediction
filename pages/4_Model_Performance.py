import streamlit as st
import pandas as pd
import pickle
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Add parent directory to path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.data_processing import get_data
from utils.style import inject_custom_css

st.set_page_config(page_title="Model Performance", page_icon="⚙️", layout="wide")
inject_custom_css()

st.title("⚙️ Classification Model Performance")
st.markdown("Analyze how well our Random Forest Classifier predicts Performance Levels.")

@st.cache_resource
def load_model_from_disk():
    model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'model', 'model.pkl')
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    return None

@st.cache_data
def load_and_evaluate_model_fresh(_model):
    df = get_data()
    if 'Student_ID' in df.columns:
        df = df.drop('Student_ID', axis=1)
        
    X = df.drop('Performance_Level', axis=1)
    y = df['Performance_Level']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    predictions = _model.predict(X_test)
    
    acc = accuracy_score(y_test, predictions)
    prec = precision_score(y_test, predictions, average='weighted')
    rec = recall_score(y_test, predictions, average='weighted')
    f1 = f1_score(y_test, predictions, average='weighted')
    cm = confusion_matrix(y_test, predictions)
    
    # Feature importances
    importances = _model.feature_importances_
    feature_names = X.columns
    feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
    
    return acc, prec, rec, f1, cm, feature_importance_df

model = load_model_from_disk()

if model is None:
    st.error("Model not found! Please run `model/train_model.py` first.")
    st.stop()

# Evaluate
with st.spinner("Evaluating model performance..."):
    acc, prec, rec, f1, cm, feature_importance_df = load_and_evaluate_model_fresh(model)

# Metrics
st.header("Evaluation Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Accuracy", f"{acc:.4f}")
col2.metric("Precision (Weighted)", f"{prec:.4f}")
col3.metric("Recall (Weighted)", f"{rec:.4f}")
col4.metric("F1 Score (Weighted)", f"{f1:.4f}")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.header("Confusion Matrix")
    fig, ax = plt.subplots(figsize=(6, 5))
    labels = ['Poor', 'Average', 'Good', 'Excellent']
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax, 
                xticklabels=labels, yticklabels=labels)
    ax.set_xlabel("Predicted Label")
    ax.set_ylabel("True Label")
    st.pyplot(fig)

with col2:
    st.header("Feature Importance")
    st.markdown("Which factors contribute most to the prediction?")
    fig, ax = plt.subplots(figsize=(8, 8))
    sns.barplot(x='Importance', y='Feature', data=feature_importance_df, palette='viridis', ax=ax)
    st.pyplot(fig)
