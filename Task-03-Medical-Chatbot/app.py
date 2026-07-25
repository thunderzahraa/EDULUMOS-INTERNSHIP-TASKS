import streamlit as st
from medical_chatbot import get_response

st.set_page_config(page_title="Medical Chatbot", page_icon="🩺")

st.title("🩺 Medical Chatbot")
st.write("Describe your symptoms below and receive general health information.")

st.warning("⚠️ This chatbot is for educational purposes only and is not a substitute for professional medical advice.")

user_input = st.text_area("Enter your symptoms")

if st.button("Get Advice"):

    if user_input.strip() == "":
        st.warning("Please enter your symptoms.")
    else:
        response = get_response(user_input)
        st.success(response)