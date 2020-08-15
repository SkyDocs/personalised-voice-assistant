import os
import sys
import speech_recognition as sr
import webbrowser
import datetime
import pyttsx3
from selenium import webdriver

def bot(talk):
	print(talk)
	
	engine = pyttsx3.init()
	sound = engine.getProperty('voices')

	for i in str(talk).splitlines():
		engine.say(talk)
	engine.runAndWait()

def listen():
	mic = sr.Microphone()
	r = sr.Recognizer()
	with mic as source:
		audio = r.listen(source, phrase_time_limit=5)
	
	try:
		command = r.recognize_google(audio).lower()
		print("You said : " + command)
		# main(command)
	
	except sr.UnknownValueError:
		print("Error occured, try again")
		command = listen()

	return command	   
	
def main(command):
	if "open google" in command:
		webbrowser.open("https://www.google.com")
		#print("webbrowser opened")
		bot("Your web browser is opened! ")
	elif "current time" in command:
		current = datetime.datetime.now()
		print(current)
	elif "open youtube" in command:
		browser = webdriver.Firefox()
		bot("opening youtube")
		url = "https://www.youtube.com"
		browser.get(url)






main(listen())