import os
import sys
import speech_recognition as sr
import webbrowser
import time
import pyjokes
import subprocess
import datetime
import pyttsx3


def bot(talk):
	print(talk)

	engine = pyttsx3.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', 180)
	volume = engine.getProperty('volume')
	engine.setProperty('volume', 1.0)
	sound = engine.getProperty('voices')

	for i in str(talk).splitlines():
		engine.say(talk)
	engine.runAndWait()

def listen():
	mic = sr.Microphone()
	r = sr.Recognizer()
	with mic as source:
		print("say something")
		audio = r.listen(source)
	
	try:
		command = r.recognize_google(audio).lower()
		print("You said : " + command)
		# main(command)
	
	except sr.UnknownValueError:
		print("Error occured, try again")
		#bot("Sorry I did not get that. Please try again.")
		command = listen()

	return command	  

def activate(talk):
	wake_words = {'ok siri'}

	talk = talk.lower()
	for phrase in wake_words:
		if phrase in talk:
			return True
	return False  
	
def main(command):
	if "hello" in command:
		bot("Hey, this is your voice assistant, developed by a team at skydocs.")
	elif "joke" in command:
		bot(pyjokes.get_joke())		
	elif "open google" in command:
		webbrowser.open("https://www.google.com")
		#print("webbrowser opened")
		bot("Your web browser is opened! ")
	elif "current time" in command:
		current = datetime.datetime.now()
		print(current)
	elif "youtube" in command:
		bot("opening youtube")
		url = "https://www.youtube.com"
		webbrowser.open(url)
	elif "gmail" in command:
		bot("sure, opening gmail")
		url_mail = "https://www.gmail.com"
		webbrowser.open(url_mail)
	elif "wikipedia" in command:
		url_wiki = "https://www.wikipedia.org/"
		webbrowser.open(url_wiki)
		bot("Sure! Here you go.")
	elif "lock screen" in command:
		bot("Locking your screen")
		os.popen('gnome-screensaver-command --lock')
	elif "news" in command:
		bot("opening google news")
		news_url = "news.google.com"
		webbrowser.open(news_url)
	elif "map" in command:
		bot("opening maps powered by google")
		maps_url = "google.com/maps"
		webbrowser.open(maps_url)
	elif "shutdown" in command:
		bot("Shutting down your system")
		os.system("poweroff")
	elif "reminder" in command:
		bot("What shall I remind you about ?")
	






main(listen())