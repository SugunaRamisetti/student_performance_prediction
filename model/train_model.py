import os
import sys
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Add parent directory to path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.data_processing import get_data

def train_and_save_model():
    print("Loading data...")
    df = get_data()
    
    # Drop Student_ID if it exists in the CSV
    if 'Student_ID' in df.columns:
        df = df.drop('Student_ID', axis=1)
        
    X = df.drop('Performance_Level', axis=1)
    y = df['Performance_Level']
    
    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    
    print("Evaluating model...")
    predictions = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, predictions):.4f}")
    print(f"F1 Score (Weighted): {f1_score(y_test, predictions, average='weighted'):.4f}")
    
    # Save the model
    model_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(model_dir, 'model.pkl')
    
    print(f"Saving model to {model_path}...")
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    # We should also save the feature columns so the preprocessing script knows exactly what to feed the model
    features_path = os.path.join(model_dir, 'features.pkl')
    with open(features_path, 'wb') as f:
        pickle.dump(list(X.columns), f)
        
    print("Model and features saved successfully!")

if __name__ == "__main__":
    train_and_save_model()
