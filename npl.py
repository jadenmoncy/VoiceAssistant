"""
This file functions in responding to the speech recognised bu engine in main.py file
It responds as told for some particular requests by the source and for the else of 
the requests it responds using transformers library that uses npl(natural processed language)
which generates responses trained from model 'microsoft/DialoGPT-medium'
"""

import numpy as np
import transformers
import main
import quickstart
import os
import webbrowser
import wikipedia

npl=transformers.pipeline("conversational",model="microsoft/DialoGPT-medium",use_auth_token="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")#"microsoft/DialoGPT-medium")
os.environ["TOKENIZERS_PARALLELISM"]="true"

class ChatBot():
    def __init__(self,name):
        self.name=name
    def wake_up(self,text):
        return True if self.name in text.lower() else False

def resp():
    ai=ChatBot(name="bailey")
    while True:
        query=main.takeCommand()
        if ai.wake_up(query) is True:
            res="Hello i am bailey what do u need"
        elif 'time now' in query:
            res=main.now
        elif 'send mail ' in query:
            to="bcd@gmail.com"
            main.speak("what is the subject")
            content=main.takeCommand().lower()
            main.speak("ok....what's the content")
            subject=main.takeCommand().lower()
            quickstart.gmail_send_message(to,content,subject)
            res="done"
        if 'wikipedia' in query:
            main.speak('searching wikipedia')
            results=wikipedia.summary(query,sentences=1)
            main.speak("According to wikipedia...")
            main.speak(results)
        elif any(i in query for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me!","peace out!"])
        elif 'open youtube' in query:
            webbrowser.open("www.youtube")
            res="done"
        elif 'open chrome' in query:
            webbrowser.open("www.chrome")
            res="done"
        elif 'open spotify' in query:
            webbrowser.open("www.spotify")
            res="done"
        elif 'open code' in query:
            codepath = "path of program"
            os.startfile(codepath)
            res="done"
        elif 'quit' in query:return
        else:
            chat=npl(transformers.Conversation(query),pad_token_id=50256)
            res=str(chat)
            res = res[res.find("bot >> ")+6:].strip()
        main.speak(res)
