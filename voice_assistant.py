import os
import speech_recognition as sr
import sys


def listen():
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
        r.recognize_google(audio)
       