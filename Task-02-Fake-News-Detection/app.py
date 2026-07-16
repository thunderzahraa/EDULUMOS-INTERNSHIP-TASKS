import streamlit as st
import joblib

# Load saved model and vectorizer
model = joblib.load("model/fake_news_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# App title
st.title("📰 Fake News Detection")

st.write("Enter a news article below and click Predict.")

# Text input
news = st.text_area("News Article")

# Prediction
if st.button("Predict"):

    if news.strip() == "":
        st.warning("Please enter some news text.")
    else:
        transformed = vectorizer.transform([news])

        prediction = model.predict(transformed)
        probability = model.predict_proba(transformed)

        confidence = probability.max() * 100

        if prediction[0] == 1:
            st.success("✅ This appears to be REAL news.")
        else:
            st.error("❌ This appears to be FAKE news.")

        st.info(f"Confidence: {confidence:.2f}%")
