# 💼 Salary Prediction System

An end-to-end Machine Learning project that predicts employee salaries based on demographic, educational, and professional features.

Built using Python, Scikit-learn, and Streamlit.

---

## 🚀 Live Demo

Add your deployed app link here after deployment:

```text
https://your-streamlit-app-url.streamlit.app
```

---

## 📌 Project Overview

This project predicts salary using machine learning regression models trained on a real-world salary dataset.

Users can input:

- Age
- Gender
- Education Level
- Job Title
- Years of Experience

and get a predicted salary instantly through a web application.

---

## ✨ Features

- Data cleaning and preprocessing
- Missing value imputation
- Categorical encoding
- Feature engineering
- Regression model training
- Salary prediction web app
- Interactive Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Seaborn

---

## 🤖 Machine Learning Workflow

### 1. Data Preprocessing
- Handled missing values
- Standardized categorical columns
- Cleaned inconsistent labels

### 2. Feature Engineering
- One-hot encoding for categorical features
- Numerical feature preparation

### 3. Model Training
Models used:
- Linear Regression
- Random Forest Regressor ✅ (final model)

### 4. Evaluation Metrics
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## ▶️ Run Locally

Clone repository:

```bash
git clone https://github.com/wikkikhan/salary-prediction-ml.git
cd salary-prediction-ml
```

Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run app:

```bash
streamlit run app.py
```

---

## 📊 Sample Prediction Inputs

Example:

- Age: 25
- Gender: Male
- Education: Bachelor
- Job Title: Software Engineer
- Experience: 2 years

Output:

```text
Predicted Salary: $65,000+
```

---

## 📈 Future Improvements

- Salary confidence intervals
- Better UI/UX
- Docker deployment
- API integration
- Advanced model tuning

---

## 👨‍💻 Author

**Waqar Ahmad**

GitHub: https://github.com/wikkikhan

LinkedIn: www.linkedin.com/in/waqar583