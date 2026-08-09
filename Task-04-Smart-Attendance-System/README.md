# 📊 Smart Attendance System

## Overview

A machine learning-based Smart Attendance System that analyzes student attendance data and predicts whether a student is at risk of low attendance.

The project uses historical attendance-related information to identify attendance patterns and classify students into risk categories.

## Objective

To develop a predictive system that analyzes student attendance patterns and identifies students who may be at risk of low attendance.

## Features

- Student attendance data analysis
- ML-based attendance risk prediction
- Current and previous attendance analysis
- Assignment completion tracking
- Interactive Streamlit interface
- Low-risk and high-risk predictions

## Machine Learning

The system uses a **Random Forest Classifier** trained on attendance-related features including:

- Attendance Percentage
- Classes Attended
- Total Classes
- Assignments Completed
- Previous Attendance

### Prediction Classes

- 🟢 `0` — Student is not currently at risk
- 🔴 `1` — Student is at risk of low attendance

## Technology Stack

**Python • Pandas • Scikit-learn • Streamlit • Git • GitHub**

## Project Structure

```text
Task-04-Smart-Attendance-System/
│
├── attendance_data.csv
├── train_model.py
├── attendance_model.pkl
├── app.py
├── README.md
└── screenshots/
    ├── low_risk.png
    └── high_risk.png