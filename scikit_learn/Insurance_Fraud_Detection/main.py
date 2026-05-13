# ============================================================
# Insurance Fraud Detection System
# Algorithms:
# 1. Isolation Forest
# 2. XGBoost Classifier
# ============================================================

# =========================
# Import Libraries
# =========================

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.ensemble import IsolationForest
from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import joblib


# =========================
# Load Dataset
# =========================

df = pd.read_csv("C:/Users/Admin/Documents/pyCodes/scikit_learn/Insurance_Fraud_Detection/insurance_data/fraud_oracle.csv")

print(df.head())

print("-" * 50)

print(df.shape)

print("-" * 50)

print(df.info())

print("-" * 50)

print(df.describe())

print("-" * 50)

print(df.isnull().sum())


# =========================
# Dataset Columns
# =========================

print("-" * 50)

print(df.columns)


# ============================================================
# Exploratory Data Analysis
# ============================================================

# =========================
# Fraud Distribution
# =========================

plt.figure(figsize=(6,5))

sns.countplot(x="FraudFound_P", data=df)

plt.title("Fraud Distribution")

plt.show()


# =========================
# Age Distribution
# =========================

plt.figure(figsize=(8,5))

sns.histplot(df["Age"], bins=30, kde=True)

plt.title("Age Distribution")

plt.show()


# =========================
# Deductible Distribution
# =========================

plt.figure(figsize=(8,5))

sns.histplot(df["Deductible"], bins=30, kde=True)

plt.title("Deductible Distribution")

plt.show()


# ============================================================
# Data Preprocessing
# ============================================================

# Create copy
df_encoded = df.copy()

# Find categorical columns
categorical_cols = df_encoded.select_dtypes(include=['object']).columns

print("\nCategorical Columns:\n")

print(categorical_cols)


# =========================
# Encode categorical columns
# =========================

for col in categorical_cols:

    le = LabelEncoder()

    df_encoded[col] = le.fit_transform(df_encoded[col])


# =========================
# Verify all columns numeric
# =========================

print("\nEncoded Data Types:\n")

print(df_encoded.dtypes)


# ============================================================
# Features and Target
# ============================================================

X = df_encoded.drop("FraudFound_P", axis=1)

y = df_encoded["FraudFound_P"]


# ============================================================
# Train Test Split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nX Train Shape:", X_train.shape)

print("X Test Shape:", X_test.shape)


# ============================================================
# Isolation Forest Model
# ============================================================

iso_model = IsolationForest(
    n_estimators=100,
    contamination=0.06,
    random_state=42
)

iso_model.fit(X_train)


# =========================
# Isolation Forest Prediction
# =========================

iso_pred = iso_model.predict(X_test)

# Convert:
# -1 -> Fraud (1)
#  1 -> Genuine (0)

iso_pred = np.where(iso_pred == -1, 1, 0)


# =========================
# Isolation Forest Evaluation
# =========================

print("\n" + "=" * 50)

print("Isolation Forest Results")

print("=" * 50)

print("\nAccuracy:\n")

print(accuracy_score(y_test, iso_pred))

print("\nClassification Report:\n")

print(classification_report(y_test, iso_pred))


# ============================================================
# XGBoost Model
# ============================================================

xgb_model = XGBClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=5,
    random_state=42
)

xgb_model.fit(X_train, y_train)


# =========================
# XGBoost Prediction
# =========================

xgb_pred = xgb_model.predict(X_test)


# =========================
# XGBoost Evaluation
# =========================

print("\n" + "=" * 50)

print("XGBoost Results")

print("=" * 50)

print("\nAccuracy:\n")

print(accuracy_score(y_test, xgb_pred))

print("\nClassification Report:\n")

print(classification_report(y_test, xgb_pred))


# ============================================================
# Confusion Matrix
# ============================================================

cm = confusion_matrix(y_test, xgb_pred)

plt.figure(figsize=(6,5))

sns.heatmap(cm, annot=True, fmt='d')

plt.title("Confusion Matrix")

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.show()


# ============================================================
# Feature Importance
# ============================================================

importance = xgb_model.feature_importances_

feature_names = X.columns

feature_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})

feature_df = feature_df.sort_values(
    by="Importance",
    ascending=False
)

plt.figure(figsize=(10,6))

sns.barplot(
    x="Importance",
    y="Feature",
    data=feature_df.head(10)
)

plt.title("Top 10 Important Features")

plt.show()


# ============================================================
# Save Models
# ============================================================

joblib.dump(xgb_model, "xgboost_fraud_model.pkl")

joblib.dump(iso_model, "isolation_forest_model.pkl")

print("\nModels Saved Successfully")


# ============================================================
# Load Models
# ============================================================

xgb_loaded = joblib.load("xgboost_fraud_model.pkl")

iso_loaded = joblib.load("isolation_forest_model.pkl")


# ============================================================
# Predict New Sample
# ============================================================

sample = X_test.iloc[[0]]

prediction = xgb_loaded.predict(sample)

print("\nSample Prediction:\n")

if prediction[0] == 1:

    print("Fraudulent Claim")

else:

    print("Genuine Claim")