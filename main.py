import speech_recognition as sr
import datetime
import sys
from assistant import speak, initialize_engine
from npl import process_command

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("I didn't understand. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def tell_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def main():
    engine = initialize_engine()
    speak("Hi! I am your custom voice assistant.", engine)
    while True:
        command = listen()
        if not command:
            continue
        action = process_command(command)

        if action == "time":
            current_time = tell_time()
            speak(f"The current time is {current_time}", engine)
        elif action == "greet":
            speak("Hello! How can I help you?", engine)
        elif action == "exit":
            speak("Goodbye!", engine)
            sys.exit()
        else:
            speak(f"I heard: {command}", engine)

if __name__ == "__main__":
    main()
