import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load your trained model
model = joblib.load("student_prediction_model.pkl")

# -------------------------------
# App Title & Intro
# -------------------------------
st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓", layout="wide")

st.title("Student Performance Predictor")
st.markdown(
    """
    Welcome to the **Student Prediction Dashboard**.  
    Adjust the study time slider and let our AI estimate the final score.  
    """
)

# -------------------------------
# Input Section
# -------------------------------
st.subheader("Enter Study Time")

study_time = st.slider("Study Time (hrs/week)", 0, 20, 5)
features = np.array([[study_time]])

# -------------------------------
# Prediction & Visualization
# -------------------------------
st.subheader("Prediction Results")

if st.button("Predict"):
    prediction = model.predict(features)[0]
    st.metric(label="Predicted Final Score", value=f"{prediction:.2f}")

    # Show how predictions vary with study hours
    hours = np.arange(0, 21)
    preds = [model.predict([[h]])[0] for h in hours]
    df = pd.DataFrame({"Hours Studied": hours, "Predicted Score": preds})

    st.line_chart(df.set_index("Hours Studied"))

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown(
    """
    💡 *Tip: Move the slider to see how study time influences predicted performance.*  
    """
)