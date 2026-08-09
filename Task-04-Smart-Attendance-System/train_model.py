import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load attendance dataset
data = pd.read_csv("attendance_data.csv")

# Features used for prediction
features = [
    "Attendance_Percentage",
    "Classes_Attended",
    "Total_Classes",
    "Assignments_Completed",
    "Previous_Attendance"
]

X = data[features]
y = data["Risk"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save trained model
with open("attendance_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")