import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("attendance_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("📊 Smart Attendance System")
st.write("Predict whether a student is at risk of low attendance.")

st.divider()

# Student details
student_id = st.text_input("Student ID", "S021")

attendance = st.number_input(
    "Current Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

classes_attended = st.number_input(
    "Classes Attended",
    min_value=0,
    value=30
)

total_classes = st.number_input(
    "Total Classes",
    min_value=1,
    value=40
)

assignments = st.number_input(
    "Assignments Completed",
    min_value=0,
    value=7
)

previous_attendance = st.number_input(
    "Previous Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

if st.button("Predict Attendance Risk"):

    input_data = pd.DataFrame({
        "Attendance_Percentage": [attendance],
        "Classes_Attended": [classes_attended],
        "Total_Classes": [total_classes],
        "Assignments_Completed": [assignments],
        "Previous_Attendance": [previous_attendance]
    })

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f"⚠️ {student_id} is at risk of low attendance.")
    else:
        st.success(f"✅ {student_id} is not currently at risk.")
        