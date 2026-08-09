import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
        return ""

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""

def process_command(command):

    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")

    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com")

    elif "search for" in command:
        search_query = command.replace("search for", "").strip()

        if search_query:
            speak(f"Searching for {search_query}.")
            webbrowser.open(
                "https://www.google.com/search?q=" +
                search_query.replace(" ", "+")
            )
        else:
            speak("What would you like me to search for?")

    elif "exit" in command or "stop" in command or "goodbye" in command:
        speak("Goodbye!")
        return False

    else:
        speak("I don't know how to do that yet.")

    return True


speak("Voice assistant activated. How can I help you?")

running = True

while running:
    command = listen()

    if command:
        running = process_command(command)