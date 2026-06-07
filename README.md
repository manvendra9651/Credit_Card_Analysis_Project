# Credit Card Fraud Detection Using Machine Learning

## Project Overview

This project focuses on detecting fraudulent credit card transactions using Machine Learning techniques. Credit card fraud detection is an imbalanced classification problem where fraudulent transactions represent only a small portion of the dataset. The objective is to build a reliable model that can accurately identify fraudulent transactions while minimizing false alarms.

---

## Objectives

- Analyze credit card transaction data.
- Perform Exploratory Data Analysis (EDA).
- Handle class imbalance using SMOTE.
- Build and evaluate Machine Learning models.
- Detect fraudulent transactions effectively.

---

## Dataset Information

The dataset contains anonymized transaction features along with transaction amount and class labels.

**Target Variable:**

- 0 → Legitimate Transaction
- 1 → Fraudulent Transaction

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Imbalanced-Learn (SMOTE)

---

## Exploratory Data Analysis (EDA)

The following analyses were performed:

- Dataset Overview
- Missing Values Check
- Statistical Summary
- Class Distribution Analysis
- Transaction Amount Analysis
- Correlation Analysis
- Fraud vs Non-Fraud Comparison

---

## Data Preprocessing

- Checked for missing values.
- Scaled numerical features where required.
- Split data into training and testing sets.
- Applied SMOTE to address class imbalance.

---

## Machine Learning Models

### Logistic Regression
A baseline classification model used for fraud prediction.

### Random Forest Classifier
An ensemble learning model used to improve prediction performance and detect fraud transactions more effectively.

---

## Model Evaluation

The models were evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

### Why Precision, Recall, and F1-Score?

Since fraud detection is a highly imbalanced classification problem, Accuracy alone is not sufficient.

- **Precision** measures how many predicted fraud transactions were actually fraud.
- **Recall** measures how many actual fraud transactions were successfully detected.
- **F1-Score** provides a balance between Precision and Recall.

Recall is especially important because failing to detect a fraudulent transaction can result in financial losses.

---

## Key Insights

- The dataset was highly imbalanced.
- SMOTE helped balance the classes and improve model performance.
- Random Forest achieved better fraud detection performance compared to Logistic Regression.
- Precision, Recall, and F1-Score provided a more reliable evaluation than Accuracy alone.

---

## Future Improvements

- Hyperparameter Tuning
- XGBoost Implementation
- LightGBM Implementation
- Cross Validation
- Streamlit Deployment
- Model Monitoring

---

## Author

**Manvendra Kumar**

Aspiring Data Scientist | Machine Learning Enthusiast

LinkedIn: Add Your LinkedIn Profile Here

GitHub: Add Your GitHub Profile Here
