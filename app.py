import pickle
import streamlit as st
import numpy as np

# Load model
with open("heart_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("❤️ Heart Disease Prediction App")

st.write("Enter patient details below:")

age = st.slider("Age", 20, 100, 40)
sex = st.selectbox("Sex", ["Female", "Male"])
sex = 1 if sex == "Male" else 0  # 0 = Female, 1 = Male
chest_pain = st.selectbox("Chest Pain Type", [1, 2, 3, 4])
bp = st.slider("Resting Blood Pressure", 80, 200, 120)
cholesterol = st.slider("Cholesterol", 100, 600, 250)
fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
ekg = st.selectbox("EKG Results", [0, 1, 2])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Induced Angina", [0, 1])
st_depression = st.slider("ST Depression", 0, 10, 2)
slope = st.selectbox("Slope of ST", [1, 2, 3])
vessels = st.selectbox("Number of Vessels Fluoroscopy", [0, 1, 2, 3])
thallium = st.selectbox("Thallium", [3, 6, 7])

if st.button("Predict"):
    input_data = np.array([[age, sex, chest_pain, bp, cholesterol,
                            fbs, ekg, max_hr, exercise_angina,
                            st_depression, slope, vessels, thallium]])

    probability = model.predict_proba(input_data)[0][1]

    st.subheader(f"Heart Disease Risk: {probability*100:.2f}%")

    if probability > 0.7:
        st.error("High Risk ⚠️")
    elif probability > 0.3:
        st.warning("Moderate Risk ⚠️")
    else:
        st.success("Low Risk ✅")