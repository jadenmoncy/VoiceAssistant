import pyttsx3

def initialize_engine(rate=150, voice=None):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    voices = engine.getProperty('voices')
    if voice is not None:
        engine.setProperty('voice', voices[voice].id)
    return engine

def speak(text, engine=None):
    if engine is None:
        engine = initialize_engine()
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
