import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# ---
student = pd.read_csv("/content/student_performance_dataset.csv")
# ---
student
# ---
student.info()
# ---
student.isnull().sum()
# ---
student.describe()
# ---
# Count duplicate rows
duplicate_count = student.duplicated().sum()

print(f"Number of duplicate rows: {duplicate_count}")
# ---
student["Gender"].unique()
# ---
# Remove leading/trailing spaces and standardize case
student["Gender"] = (
    student["Gender"]
    .str.strip()
    .str.title()
)
# ---
student["Gender"].unique()
# ---
mode_gender = student["Gender"].mode()[0]
print(mode_gender)
# ---
mode_internet = student["Internet"].mode()[0]
print(mode_internet)
# ---
student["Internet"].value_counts()
# ---
student["Internet"] = student["Internet"].replace("Unknown", "Yes")
# ---
student["Gender"].value_counts()
# ---
student["Gender"] = student["Gender"].replace("Other", "Female")
# ---
student["Age"].describe()
# ---
student["Age"].unique()
# ---
invalid_age = student[(student["Age"] < 15) | (student["Age"] > 23)]

print(f"Number of invalid age records: {len(invalid_age)}")
invalid_age
# ---
((student["Age"] < 15) | (student["Age"] > 23)).sum()
# ---
student.loc[(student["Age"] < 15) | (student["Age"] > 23), "Age"].value_counts().sort_index()
# ---
# Calculate the median of valid ages
median_age = student.loc[student["Age"].between(15, 22), "Age"].median()

# Replace invalid age (30) with the median
student.loc[student["Age"] == 30, "Age"] = median_age
# ---
# Check again for invalid ages
student[(student["Age"] < 15) | (student["Age"] > 23)]
# ---
student["Attendance"].dtype
# ---
student["Attendance"].isnull().sum()
# ---
student["Attendance"].sample(20)
# ---
student["Attendance"] = pd.to_numeric(student["Attendance"], errors="coerce")
# ---
mean_attendance = student["Attendance"].mean()
# ---
mean_attendance
# ---
print(student["Attendance"].isnull().sum())
print(student["Attendance"].dtype)
# ---
mean_attendance = student["Attendance"].mean()

student["Attendance"] = student["Attendance"].fillna(mean_attendance)
# ---
student["Attendance"].describe()
# ---
invalid_attendance = student[(student["Attendance"] < 0) | (student["Attendance"] > 100)]

print(f"Number of invalid attendance records: {len(invalid_attendance)}")
invalid_attendance
# ---
student.loc[
    (student["Attendance"] < 0) | (student["Attendance"] > 100),
    "Attendance"
].value_counts().sort_index()
# ---
mean_attendance = student.loc[
    student["Attendance"].between(0, 100),
    "Attendance"
].mean()

student.loc[
    (student["Attendance"] < 0) | (student["Attendance"] > 100),
    "Attendance"
] = mean_attendance
# ---
student["Study_Hours"].dtype
# ---
student.info()
# ---
student["Study_Hours"].isnull().sum()
# ---
student["Study_Hours"].describe()
# ---
# Identify and count invalid 'Study_Hours' (negative values)
invalid_study_hours_count = student[student['Study_Hours'] < 0].shape[0]
print(f"Number of invalid 'Study_Hours' records (negative values): {invalid_study_hours_count}")

# Replace invalid 'Study_Hours' (negative values) with the median of valid study hours
median_study_hours = student.loc[student['Study_Hours'] >= 0, 'Study_Hours'].median()
student.loc[student['Study_Hours'] < 0, 'Study_Hours'] = median_study_hours

# Fill missing 'Study_Hours' with the mean of valid study hours
mean_study_hours = student['Study_Hours'].mean()
student['Study_Hours'] = student['Study_Hours'].fillna(mean_study_hours)

print("\n'Study_Hours' after cleaning:")
display(student['Study_Hours'].describe())
# ---
# Check unique values for 'Internet'
print("Original unique values for 'Internet':")
print(student["Internet"].unique())

# Standardize 'Internet' values
student["Internet"] = student["Internet"].str.strip().str.title().replace({'Y': 'Yes', 'N': 'No'})

# Fill missing 'Internet' values with the mode
mode_internet = student["Internet"].mode()[0]
student["Internet"] = student["Internet"].fillna(mode_internet)

print("\nCleaned unique values for 'Internet':")
print(student["Internet"].unique())
print("\n'Internet' value counts after cleaning:")
print(student["Internet"].value_counts())
# ---
# Check unique values for 'Parent_Education'
print("Original unique values for 'Parent_Education':")
print(student["Parent_Education"].unique())

# Standardize 'Parent_Education' values
student["Parent_Education"] = student["Parent_Education"].str.strip().str.title()
student["Parent_Education"] = student["Parent_Education"].replace({
    "Bachelors": "Bachelor Degree",
    "Bachelor's": "Bachelor Degree",
    "Highschool": "High School",
    "High-School": "High School",
    "Masters": "Master Degree",
    "Doctorate": "Doctorate Degree",
    "No School": "No Formal Education",
    "Unknown": "No Formal Education"
})

# Fill missing 'Parent_Education' values with the mode
mode_parent_education = student["Parent_Education"].mode()[0]
student["Parent_Education"] = student["Parent_Education"].fillna(mode_parent_education)

print("\nCleaned unique values for 'Parent_Education':")
print(student["Parent_Education"].unique())
print("\n'Parent_Education' value counts after cleaning:")
print(student["Parent_Education"].value_counts())
# ---
# Clean 'Family_Income' column: remove non-numeric characters and convert to float
student['Family_Income'] = (student['Family_Income'].astype(str)
                                                 .str.replace('€', '', regex=False)
                                                 .str.replace('₹', '', regex=False)
                                                 .str.replace('$', '', regex=False)
                                                 .str.replace(',', '', regex=False)
                                                 .str.strip())

student['Family_Income'] = pd.to_numeric(student['Family_Income'], errors='coerce')

# Fill missing 'Family_Income' values with the mean
mean_family_income = student['Family_Income'].mean()
student['Family_Income'] = student['Family_Income'].fillna(mean_family_income)

print("\n'Family_Income' describe after cleaning:")
display(student['Family_Income'].describe())
# ---
# Identify and count invalid 'Sleep_Hours' (e.g., very low or very high)
# Assuming typical sleep hours are between 4 and 12 hours. Outliers are outside this range.
invalid_sleep_hours_count = student[(student['Sleep_Hours'] < 4) | (student['Sleep_Hours'] > 12)].shape[0]
print(f"Number of invalid 'Sleep_Hours' records (outside 4-12 hours): {invalid_sleep_hours_count}")

# Replace invalid 'Sleep_Hours' with the median of valid sleep hours
median_sleep_hours = student.loc[student['Sleep_Hours'].between(4, 12), 'Sleep_Hours'].median()
student.loc[(student['Sleep_Hours'] < 4) | (student['Sleep_Hours'] > 12), 'Sleep_Hours'] = median_sleep_hours

# Fill missing 'Sleep_Hours' with the mean of valid sleep hours
mean_sleep_hours = student['Sleep_Hours'].mean()
student['Sleep_Hours'] = student['Sleep_Hours'].fillna(mean_sleep_hours)

print("\n'Sleep_Hours' after cleaning:")
display(student['Sleep_Hours'].describe())
# ---
# Identify and count invalid 'Assignments' (e.g., negative or excessively high)
# Assuming assignment scores are between 0 and 100. Outliers are outside this range.
invalid_assignments_count = student[(student['Assignments'] < 0) | (student['Assignments'] > 100)].shape[0]
print(f"Number of invalid 'Assignments' records (outside 0-100): {invalid_assignments_count}")

# Replace invalid 'Assignments' with the median of valid assignment scores
median_assignments = student.loc[student['Assignments'].between(0, 100), 'Assignments'].median()
student.loc[(student['Assignments'] < 0) | (student['Assignments'] > 100), 'Assignments'] = median_assignments

# Fill missing 'Assignments' values with the mean
mean_assignments = student['Assignments'].mean()
student['Assignments'] = student['Assignments'].fillna(mean_assignments)

print("\n'Assignments' after cleaning:")
display(student['Assignments'].describe())
# ---
# Identify and count invalid 'Previous_Grade' (e.g., negative or excessively high)
# Assuming grades are between 0 and 100. Outliers are outside this range.
invalid_previous_grade_count = student[(student['Previous_Grade'] < 0) | (student['Previous_Grade'] > 100)].shape[0]
print(f"Number of invalid 'Previous_Grade' records (outside 0-100): {invalid_previous_grade_count}")

# Replace invalid 'Previous_Grade' with the median of valid previous grades
median_previous_grade = student.loc[student['Previous_Grade'].between(0, 100), 'Previous_Grade'].median()
student.loc[(student['Previous_Grade'] < 0) | (student['Previous_Grade'] > 100), 'Previous_Grade'] = median_previous_grade

# Fill missing 'Previous_Grade' values with the mean
mean_previous_grade = student['Previous_Grade'].mean()
student['Previous_Grade'] = student['Previous_Grade'].fillna(mean_previous_grade)

print("\n'Previous_Grade' after cleaning:")
display(student['Previous_Grade'].describe())
# ---
print("Info of DataFrame after cleaning:")
student.info()
print("\nMissing values after cleaning:")
student.isnull().sum()
# ---
student.describe()
# ---
student["Parent_Education"].unique()
# ---
# Remove extra spaces and standardize text
student["Parent_Education"] = (
    student["Parent_Education"]
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
    .str.title()
)

# Replace inconsistent values
student["Parent_Education"] = student["Parent_Education"].replace({
    "Bachelor": "Bachelor Degree",
    "Bachelor'S": "Bachelor Degree",
    "Master": "Master Degree",
    "Master'S": "Master Degree",
    "Phd": "Ph.D",
    "Diploma Course": "Diploma",
    "No School": "No Formal Education",
    "None": "No Formal Education"
})
# ---
student["Parent_Education"].unique()
# ---
student["Family_Income"].describe()
# ---
invalid_income = student[student["Family_Income"] < 0]

print(f"Invalid Records: {len(invalid_income)}")
invalid_income
# ---
Q1 = student["Family_Income"].quantile(0.25)
Q3 = student["Family_Income"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
# ---
outliers = student[
    (student["Family_Income"] < lower_limit) |
    (student["Family_Income"] > upper_limit)
]

print(f"Total Outliers: {len(outliers)}")
outliers
# ---
mean_income = student.loc[
    student["Family_Income"] >= 0,
    "Family_Income"
].mean()

student.loc[
    student["Family_Income"] < 0,
    "Family_Income"
] = mean_income
# ---
student["Family_Income"].describe()
# ---
student.head()
# ---
student.info()
# ---
student.isnull().sum()
# ---
student.describe()
# ---
# Download the cleaned student DataFrame to a CSV file
student.to_csv('student_dp.csv', index=False)
print("Cleaned dataset 'cleaned_student_data.csv' downloaded successfully.")
# ---
student_dp = pd.read_csv("/content/student_dp.csv")
# ---
student_dp
# ---
student_dp.info()
# ---
student_dp.isnull().sum()
# ---
student_dp.describe()
# ---
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))

ax = sns.countplot(
    data=student_dp,
    x="Performance_Level",
    order=student_dp["Performance_Level"].value_counts().index
)

plt.title("Distribution of Student Performance Levels")
plt.xlabel("Performance Level")
plt.ylabel("Number of Students")

# Add counts on top of the bars
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')

plt.show()
# ---
plt.figure(figsize=(10,7))

numeric_df = student_dp.select_dtypes(include=["int64","float64"])

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.show()
# ---
plt.figure(figsize=(8,5))

sns.boxplot(
    data=student_dp,
    x="Performance_Level",
    y="Attendance"
)

plt.title("Attendance vs Performance Level")
plt.xlabel("Performance Level")
plt.ylabel("Attendance (%)")

plt.show()
# ---
plt.figure(figsize=(8,6))

sns.scatterplot(
    data=student_dp,
    x="Previous_Grade",
    y="Final_Exam",
    hue="Performance_Level"
)

plt.title("Previous Grade vs Final Exam")

plt.show()
# ---
numerical_columns = [
    "Age",
    "Attendance",
    "Study_Hours",
    "Family_Income",
    "Sleep_Hours",
    "Assignments",
    "Previous_Grade",
    "Final_Exam"
]

student_dp[numerical_columns].hist(
    figsize=(15,10),
    bins=20
)

plt.suptitle("Distribution of Numerical Features")

plt.show()
# ---
student_dp.head(6)
# ---
student_dp.info()
# ---
student_dp.drop("Student_ID", axis=1, inplace=True)
# ---
student_dp["Study_Efficiency"] = student_dp["Study_Hours"] * (student_dp["Attendance"] / 100)
# ---
student_dp.head(5)
# ---
student_dp["Academic_Consistency"] = (
    student_dp["Previous_Grade"] +
    student_dp["Final_Exam"]
) / 2
# ---
student_dp["Assignment_Rate"] = (
    student_dp["Assignments"] *
    student_dp["Attendance"] / 100
)
# ---
def sleep_quality(hours):
    if hours < 6:
        return "Poor"
    elif hours <= 8:
        return "Normal"
    else:
        return "Excellent"

student_dp["Sleep_Quality"] = student_dp["Sleep_Hours"].apply(sleep_quality)
# ---
def attendance_category(x):
    if x < 60:
        return "Low"
    elif x < 80:
        return "Medium"
    else:
        return "High"

student_dp["Attendance_Category"] = student_dp["Attendance"].apply(attendance_category)
# ---
def income_category(x):
    if x < 30000:
        return "Low"
    elif x < 60000:
        return "Middle"
    else:
        return "High"

student_dp["Income_Category"] = student_dp["Family_Income"].apply(income_category)
# ---
student_dp["Grade_Improvement"] = (
    student_dp["Final_Exam"] -
    student_dp["Previous_Grade"]
)
# ---
student_dp.head(5)
# ---
student_dp["Academic_Score"] = (
    student_dp["Previous_Grade"] +
    student_dp["Final_Exam"] +
    student_dp["Assignments"]
) / 3
# ---
student_dp["Digital_Learning"] = (
    (student_dp["Internet"] == "Yes").astype(int)
    * student_dp["Study_Hours"]
)
# ---
education_map = {
    "No Formal Education": 0,
    "Primary": 1,
    "High School": 2,
    "Diploma": 3,
    "Bachelor Degree": 4,
    "Master Degree": 5,
    "Ph.D": 6
}

student_dp["Parent_Education_Score"] = (
    student_dp["Parent_Education"]
    .map(education_map)
)
# ---
student_dp["Study_Sleep_Ratio"] = (
    student_dp["Study_Hours"] /
    student_dp["Sleep_Hours"]
)
# ---
student_dp.info()
# ---
student_dp.select_dtypes(include="object").columns
# ---
student_dp.head(5)
# ---
student_dp["Gender"].unique()
# ---
student_dp["Internet"].unique()
# ---
Gender = {
    "Male": 0,
    "Female": 1
}

student_dp["Gender"] = student_dp["Gender"].map(Gender)
# ---
internet_map = {
    "No": 0,
    "Yes": 1
}

student_dp["Internet"] = student_dp["Internet"].map(internet_map)
# ---
student_dp["Parent_Education_Score"].unique()
# ---
student_dp.drop("Parent_Education", axis=1, inplace=True)
# ---
student_dp["Sleep_Quality"].unique()
# ---
sleep_map = {
    "Poor": 0,
    "Normal": 1,
    "Excellent": 2
}

student_dp["Sleep_Quality"] = student_dp["Sleep_Quality"].map(sleep_map)
# ---
student_dp["Attendance_Category"].unique()
# ---
attendance_map = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

student_dp["Attendance_Category"] = student_dp["Attendance_Category"].map(attendance_map)
# ---
student_dp["Income_Category"].unique()
# ---
income_map = {
    "Low": 0,
    "Middle": 1,
    "High": 2
}

student_dp["Income_Category"] = student_dp["Income_Category"].map(income_map)
# ---
student_dp["Performance_Level"].unique()
# ---
performance_map = {
    "Poor": 0,
    "Average": 1,
    "Good": 2,
    "Excellent": 3
}

student_dp["Performance_Level"] = student_dp["Performance_Level"].map(performance_map)
# ---
student_dp.info()
# ---
student_dp.select_dtypes(include="object").columns
# ---
student_dp.head(5)
# ---
X = student_dp.drop("Performance_Level", axis=1)

y = student_dp["Performance_Level"]
# ---
X.head(5)
# ---
y.head(5)
# ---
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
# ---
X_train
# ---
X_test
# ---
y_train
# ---
y_test
# ---
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)
# ---
X_train_scaled
# ---
student_dp
# ---
x_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)

x_train_scaled.head(5)
# ---
print(X_train_scaled.shape)
print(X_test_scaled.shape)
# ---
from sklearn.linear_model import LogisticRegression
# ---
logistic_regression = LogisticRegression(random_state=42)
# ---
logistic_regression.fit(X_train_scaled, y_train)
# ---
y_pred = logistic_regression.predict(X_test_scaled)
# ---
print(y_test.head())
# ---
comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

comparison.head(20)
# ---
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
# ---
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
# ---
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print(cm)
# ---
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()
# ---
from sklearn.tree import DecisionTreeClassifier
# ---
decision_tree = DecisionTreeClassifier(random_state=42)
# ---
decision_tree.fit(X_train, y_train)
# ---
y_pred_dt = decision_tree.predict(X_test)
# ---
print(y_pred_dt)
# ---
from sklearn.metrics import accuracy_score

accuracy_dt = accuracy_score(y_test, y_pred_dt)

print("Decision Tree Accuracy:", accuracy_dt)
# ---
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred_dt))
# ---
from sklearn.metrics import confusion_matrix

cm_dt = confusion_matrix(y_test, y_pred_dt)

print(cm_dt)
# ---
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,5))

sns.heatmap(
    cm_dt,
    annot=True,
    fmt="d",
    cmap="Oranges"
)

plt.title("Confusion Matrix - Decision Tree")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()
# ---
from sklearn.ensemble import RandomForestClassifier
# ---
random_forest = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)
# ---
random_forest.fit(X_train, y_train)
# ---
y_pred_rf = random_forest.predict(X_test)
# ---
y_pred_rf
# ---
from sklearn.metrics import accuracy_score

accuracy_rf = accuracy_score(y_test, y_pred_rf)

print("Random Forest Accuracy:", accuracy_rf)
# ---
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred_rf))
# ---
from sklearn.metrics import confusion_matrix

cm_rf = confusion_matrix(y_test, y_pred_rf)

print(cm_rf)
# ---
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,5))

sns.heatmap(
    cm_rf,
    annot=True,
    fmt="d",
    cmap="Greens"
)

plt.title("Confusion Matrix - Random Forest")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()
# ---
from sklearn.neighbors import KNeighborsClassifier
# ---
knn = KNeighborsClassifier(n_neighbors=7)
# ---
knn.fit(X_train_scaled, y_train)
# ---
y_pred_knn = knn.predict(X_test_scaled)
# ---
y_pred_knn
# ---
from sklearn.metrics import accuracy_score

accuracy_knn = accuracy_score(y_test, y_pred_knn)

print("KNN Accuracy:", accuracy_knn)
# ---
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred_knn))
# ---
from sklearn.metrics import confusion_matrix

cm_knn = confusion_matrix(y_test, y_pred_knn)

print(cm_knn)
# ---
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,5))

sns.heatmap(
    cm_knn,
    annot=True,
    fmt="d",
    cmap="Purples"
)

plt.title("Confusion Matrix - KNN")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()
# ---
from sklearn.svm import SVC
# ---
svm = SVC(
    kernel='rbf',
    random_state=42
)
# ---
svm.fit(X_train_scaled, y_train)
# ---
y_pred_svm = svm.predict(X_test_scaled)
# ---
y_pred_svm
# ---
from sklearn.metrics import accuracy_score

accuracy_svm = accuracy_score(y_test, y_pred_svm)

print("SVM Accuracy:", accuracy_svm)
# ---
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred_svm))
# ---
from sklearn.metrics import confusion_matrix

cm_svm = confusion_matrix(y_test, y_pred_svm)

print(cm_svm)
# ---
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,5))

sns.heatmap(
    cm_svm,
    annot=True,
    fmt="d",
    cmap="Reds"
)

plt.title("Confusion Matrix - Support Vector Machine")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()
# ---
import pandas as pd

comparison_df = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "K-Nearest Neighbors (KNN)",
        "Support Vector Machine (SVM)"
    ],

    "Scaling Required": [
        "Yes",
        "No",
        "No",
        "Yes",
        "Yes"
    ],

    "Accuracy (%)": [
        round(accuracy * 100, 2),
        round(accuracy_dt * 100, 2),
        round(accuracy_rf * 100, 2),
        round(accuracy_knn * 100, 2),
        round(accuracy_svm * 100, 2)
    ]
})

comparison_df
# ---
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

plt.bar(
    comparison_df["Model"],
    comparison_df["Accuracy (%)"]
)

plt.title("Machine Learning Models Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy (%)")

plt.xticks(rotation=20)

plt.show()
# ---
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

comparison_df = pd.DataFrame({

    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "K-Nearest Neighbors",
        "Support Vector Machine"
    ],

    "Scaling Required": [
        "Yes",
        "No",
        "No",
        "Yes",
        "Yes"
    ],

    "Accuracy (%)": [
        round(accuracy_score(y_test, y_pred) * 100, 2),
        round(accuracy_score(y_test, y_pred_dt) * 100, 2),
        round(accuracy_score(y_test, y_pred_rf) * 100, 2),
        round(accuracy_score(y_test, y_pred_knn) * 100, 2),
        round(accuracy_score(y_test, y_pred_svm) * 100, 2)
    ],

    "Precision (%)": [
        round(precision_score(y_test, y_pred, average='weighted') * 100, 2),
        round(precision_score(y_test, y_pred_dt, average='weighted') * 100, 2),
        round(precision_score(y_test, y_pred_rf, average='weighted') * 100, 2),
        round(precision_score(y_test, y_pred_knn, average='weighted') * 100, 2),
        round(precision_score(y_test, y_pred_svm, average='weighted') * 100, 2)
    ],

    "Recall (%)": [
        round(recall_score(y_test, y_pred, average='weighted') * 100, 2),
        round(recall_score(y_test, y_pred_dt, average='weighted') * 100, 2),
        round(recall_score(y_test, y_pred_rf, average='weighted') * 100, 2),
        round(recall_score(y_test, y_pred_knn, average='weighted') * 100, 2),
        round(recall_score(y_test, y_pred_svm, average='weighted') * 100, 2)
    ],

    "F1-Score (%)": [
        round(f1_score(y_test, y_pred, average='weighted') * 100, 2),
        round(f1_score(y_test, y_pred_dt, average='weighted') * 100, 2),
        round(f1_score(y_test, y_pred_rf, average='weighted') * 100, 2),
        round(f1_score(y_test, y_pred_knn, average='weighted') * 100, 2),
        round(f1_score(y_test, y_pred_svm, average='weighted') * 100, 2)
    ]
})

comparison_df
# ---
feature_importance = pd.DataFrame({
    "Feature": X_train.columns,
    "Importance": random_forest.feature_importances_
})

feature_importance
# ---
import matplotlib.pyplot as plt
import seaborn as sns

top_features = feature_importance.sort_values(by='Importance', ascending=False).head(10)

plt.figure(figsize=(10,6))

sns.barplot(
    data=top_features,
    x="Importance",
    y="Feature",
    hue="Feature", # Assign "Feature" to hue to resolve the FutureWarning
    palette="viridis",
    legend=False # Set legend to False as recommended by the FutureWarning
)

plt.title("Top 10 Feature Importance - Random Forest")
plt.xlabel("Importance Score")
plt.ylabel("Features")

plt.show()
# ---
import joblib

joblib.dump(random_forest, "random_forest_model.pkl")
joblib.dump(scaler, "scaler.pkl")
# ---
