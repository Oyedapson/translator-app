import speech_recognition as sr
import gotrans as trans 
import os
from gtts import gTTS
from playsound import playsound
import random
import time

r =  sr.Recognizer()

def convert(input,lang):
    text, status = trans.translate(input, lang)
    print(text,lang)
    if status == False:
        outSpeech(text, "en")
    else:
        outSpeech(text, status)
    return text
    
def speak():
    input = ""
    print("speak:")
    with sr.Microphone() as source:
        audio = r.listen(source)
        input = r.recognize_google(audio)
    print(input)
    return input

def showLanguages():
    return trans.languages()

def outSpeech(mytext, lang):
    myobj = gTTS(text=mytext, lang=lang, slow=False)
    a = str(random.randint(1,9))+ '.mp3'
    myobj.save(a)
    playsound(a)
    os.remove(a)


def selectLang():
    print(showLanguages())
    return input("Enter any language: ")

        