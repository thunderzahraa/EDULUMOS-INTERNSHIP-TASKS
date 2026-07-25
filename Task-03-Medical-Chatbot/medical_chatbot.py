responses = {
    "fever": "A fever may indicate an infection. Stay hydrated, rest, and consult a doctor if it persists.",
    "cough": "A cough can be caused by a cold, flu, or allergies. If it lasts more than two weeks, seek medical advice.",
    "headache": "Headaches can result from stress, dehydration, or illness. Drink water, rest, and consult a doctor if severe.",
    "stomach pain": "Stomach pain may have many causes. If the pain is severe or persistent, seek medical attention.",
    "cold": "Common cold symptoms usually improve with rest, fluids, and proper nutrition.",
    "diabetes": "Diabetes requires proper medical diagnosis and long-term management by a healthcare professional.",
    "blood pressure": "High blood pressure often has no symptoms. Regular monitoring and a healthy lifestyle are important."
}

def get_response(user_input):
    user_input = user_input.lower()

    for symptom, response in responses.items():
        if symptom in user_input:
            return response

    return "I'm sorry, I couldn't understand your symptoms. Please consult a healthcare professional for medical advice."