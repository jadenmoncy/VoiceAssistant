
import pyttsx3
import speech_recognition as sr
import datetime
import npl

engine = pyttsx3.init('sapi5') #sapi5
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """function that wishes as you start the program"""
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("hey!good morning....so how can i help you start your day?")
    elif hour>12 and hour<18:
        speak("hey!good afternoon...how was your day going on?")
    else : 
        speak("hey!good evening...wanna listen some pleasent music?")

def takeCommand():  #docstring
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        query=r.recognize_google(audio,language='en-in')
    except Exception as e:
        speak("Say that again please..")
        return "none"
    return query

def now():
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    return strTime

if __name__ =="__main__":
    wishMe()
    npl.resp()
        
