import os
import sys
import speech_recognition as sr
import webbrowser

def listen():
	mic = sr.Microphone()
	r = sr.Recognizer()
	with mic as source:
		audio = r.listen(source)

	try:
		command = r.recognize_google(audio).lower()
		print("You said : " + command)
		# main(command)

	except sr.UnknownValueError:
		print("Error occured, try again")
		command = listen()

	return command
	   
	
def main(command):
	if "open" in command:
		webbrowser.open("https://www.google.com")


main(listen())