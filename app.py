import streamlit as st
import pandas as pd
import joblib

# Load the trained model and columns
model = joblib.load('model.pkl')
columns = joblib.load('columns.pkl')

# Page config
st.set_page_config(page_title="Salary Prediction System", layout="centered")

# Header
st.markdown("## 💼 Salary Prediction System")
st.caption("AI-powered salary prediction using Machine Learning. Enter your details to get an estimate of your potential salary.")

# st.title("Salary Prediction System")
# st.caption("Predict salary based on user details")

# -----------------------
# Extract job titles from training columns
# -----------------------
job_titles = []

for col in columns:
    if col.startswith("Job Title_"):
        title = col.replace("Job Title_", "")
        job_titles.append(title)

job_titles = sorted(job_titles)

# User inputs
age = st.number_input("Age", min_value=18, max_value=70, value=25)

experience = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=40,
    value=2
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

education = st.selectbox(
    "Education Level",
    ["High School", "Bachelor's", "Master's", "PhD"]
)

job_title = st.selectbox(
    "Job Title",
    job_titles
)

# st.markdown("###")

# -----------------------
# Prediction Button
# -----------------------
if st.button("Predict Salary"):
    # Create input dictionary with all columns initialized to 0
    input_dict = {col: 0 for col in columns}

    # Numerical values
    if "Age" in input_dict:
        input_dict['Age'] = age

    if "Years of Experience" in input_dict:
        input_dict['Years of Experience'] = experience

    # Categorical encoding
    gender_col = f"Gender_{gender}"
    education_col = f"Education Level_{education}"
    job_col = f"Job Title_{job_title}"

    if gender_col in input_dict:
        input_dict[gender_col] = 1

    if education_col in input_dict:
        input_dict[education_col] = 1

    if job_col in input_dict:
        input_dict[job_col] = 1

    # Convert input dictionary to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Prediction
    prediction = model.predict(input_df)[0]
    prediction = max(prediction, 0)  # Ensure salary is not negative

    # Display result
    st.success("Salary prediction generated successfully!")
    st.metric("Predicted Salary", f"${prediction:,.2f}")

    # Additional insights based on experience
    st.subheader("Insights")

    if experience < 3:
        st.info("Early career stage. Consider gaining more experience to increase your salary potential.")
    elif experience < 5:
        st.info("Mid-level experience. Salaries typically increase as you gain more experience.")
    else:
        st.info("Senior professionals usually command higher salary bands.")


## Add a footer
st.markdown("---")
st.caption("Built with Python, Scikit-learn, and Streamlit")
st.caption("© 2024 Salary Prediction System. All rights reserved.")
st.caption("Disclaimer: This is a predictive model and should be used for informational purposes only. Actual salaries may vary based on various factors.")