import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

# Function to handle voice commands
def handle_commands(query):
    if "hello" in query:
        speak("Hello! How can I assist you?")
    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "date" in query:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif "search" in query:
        speak("What would you like to search for?")
        search_query = recognize_speech()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    else:
        speak("I'm sorry, I don't understand that command.")

# Main loop
if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        user_query = recognize_speech()
        
        if user_query == "exit":
            speak("Goodbye!")
            break

        if user_query:
            handle_commands(user_query)
    