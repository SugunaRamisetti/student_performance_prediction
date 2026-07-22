import pandas as pd
import os

def get_data():
    """Returns the cleaned and engineered dataset from the notebooks folder."""
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'notebooks', 'student_dp.csv')
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at {data_path}. Please ensure it is downloaded.")
        
    df = pd.read_csv(data_path)
    
    # Apply Feature Engineering as done in notebook lines 420-572
    
    if "Student_ID" in df.columns:
        df.drop("Student_ID", axis=1, inplace=True)
        
    df["Study_Efficiency"] = df["Study_Hours"] * (df["Attendance"] / 100)
    df["Academic_Consistency"] = (df["Previous_Grade"] + df["Final_Exam"]) / 2
    df["Assignment_Rate"] = df["Assignments"] * (df["Attendance"] / 100)
    
    def sleep_quality(hours):
        if hours < 6: return "Poor"
        elif hours <= 8: return "Normal"
        else: return "Excellent"
    df["Sleep_Quality"] = df["Sleep_Hours"].apply(sleep_quality)
    
    def attendance_category(x):
        if x < 60: return "Low"
        elif x < 80: return "Medium"
        else: return "High"
    df["Attendance_Category"] = df["Attendance"].apply(attendance_category)
    
    def income_category(x):
        if x < 30000: return "Low"
        elif x < 60000: return "Middle"
        else: return "High"
    df["Income_Category"] = df["Family_Income"].apply(income_category)
    
    df["Grade_Improvement"] = df["Final_Exam"] - df["Previous_Grade"]
    df["Academic_Score"] = (df["Previous_Grade"] + df["Final_Exam"] + df["Assignments"]) / 3
    df["Digital_Learning"] = (df["Internet"] == "Yes").astype(int) * df["Study_Hours"]
    
    education_map = {
        "No Formal Education": 0, "Primary": 1, "High School": 2, 
        "Diploma": 3, "Bachelor Degree": 4, "Master Degree": 5, "Ph.D": 6
    }
    df["Parent_Education_Score"] = df["Parent_Education"].map(education_map)
    df.drop("Parent_Education", axis=1, inplace=True)
    
    df["Study_Sleep_Ratio"] = df["Study_Hours"] / df["Sleep_Hours"]
    
    # Encodings
    df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})
    df["Internet"] = df["Internet"].map({"No": 0, "Yes": 1})
    df["Sleep_Quality"] = df["Sleep_Quality"].map({"Poor": 0, "Normal": 1, "Excellent": 2})
    df["Attendance_Category"] = df["Attendance_Category"].map({"Low": 0, "Medium": 1, "High": 2})
    df["Income_Category"] = df["Income_Category"].map({"Low": 0, "Middle": 1, "High": 2})
    df["Performance_Level"] = df["Performance_Level"].map({"Poor": 0, "Average": 1, "Good": 2, "Excellent": 3})
    
    # Fill any NaNs created by mapping issues just in case
    df = df.fillna(0)
    
    return df
