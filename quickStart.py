"""
quickstart.py
A quick demo runner for the custom voice assistant.
"""

from assistant import speak, initialize_engine
from npl import process_command

def demo():
    engine = initialize_engine()
    speak("Welcome to the quick start demo.", engine)
    example_commands = [
        "Hello",
        "What is the time",
        "Exit"
    ]
    for cmd in example_commands:
        speak(f"You said: {cmd}", engine)
        action = process_command(cmd)
        if action == "time":
            speak("Pretend I'm telling you the current time!", engine)
        elif action == "greet":
            speak("Hi there! This is a demo greeting.", engine)
        elif action == "exit":
            speak("Demo finished. Goodbye!", engine)

if __name__ == "__main__":
    demo()
