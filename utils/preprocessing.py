import pandas as pd

def prepare_input_data(age, gender, attendance, study_hours, internet, 
                       parent_edu, income, sleep_hours, assignments, 
                       previous_grade, final_exam):
    """
    Converts raw user inputs into a Pandas DataFrame and applies 
    all feature engineering steps found in the notebook.
    """
    
    # 1. Map simple categories
    gender_map = {"Male": 0, "Female": 1}
    internet_map = {"No": 0, "Yes": 1}
    education_map = {
        "No Formal Education": 0, "Primary": 1, "High School": 2, 
        "Diploma": 3, "Bachelor Degree": 4, "Master Degree": 5, "Ph.D": 6
    }
    
    df = pd.DataFrame({
        'Gender': [gender_map.get(gender, 0)],
        'Age': [age],
        'Attendance': [attendance],
        'Study_Hours': [study_hours],
        'Internet': [internet_map.get(internet, 0)],
        'Parent_Education_Score': [education_map.get(parent_edu, 0)],
        'Family_Income': [income],
        'Sleep_Hours': [sleep_hours],
        'Assignments': [assignments],
        'Previous_Grade': [previous_grade],
        'Final_Exam': [final_exam]
    })
    
    # 2. Engineer Features
    df["Study_Efficiency"] = df["Study_Hours"] * (df["Attendance"] / 100)
    df["Academic_Consistency"] = (df["Previous_Grade"] + df["Final_Exam"]) / 2
    df["Assignment_Rate"] = df["Assignments"] * (df["Attendance"] / 100)
    
    # Sleep Quality
    def sleep_quality(hours):
        if hours < 6: return 0 # Poor
        elif hours <= 8: return 1 # Normal
        else: return 2 # Excellent
    df["Sleep_Quality"] = df["Sleep_Hours"].apply(sleep_quality)
    
    # Attendance Category
    def attendance_category(x):
        if x < 60: return 0 # Low
        elif x < 80: return 1 # Medium
        else: return 2 # High
    df["Attendance_Category"] = df["Attendance"].apply(attendance_category)
    
    # Income Category
    def income_category(x):
        if x < 30000: return 0 # Low
        elif x < 60000: return 1 # Middle
        else: return 2 # High
    df["Income_Category"] = df["Family_Income"].apply(income_category)
    
    df["Grade_Improvement"] = df["Final_Exam"] - df["Previous_Grade"]
    df["Academic_Score"] = (df["Previous_Grade"] + df["Final_Exam"] + df["Assignments"]) / 3
    df["Digital_Learning"] = df["Internet"] * df["Study_Hours"]
    df["Study_Sleep_Ratio"] = df["Study_Hours"] / df["Sleep_Hours"]
    
    # Handle any inf/nan from division
    df = df.fillna(0)
    
    return df
