import os
import sys
import speech_recognition as sr
import webbrowser
import datetime
# from gtts import gTTS
# import playsound
import pyttsx3

def bot(talk):
	print(talk)
	# text_to_speech = gTTS(text=talk, lang='en', slow=False)
	# x = text_to_speech.save('sound.mp3')
	# playsound.playsound(x, True)
	engine = pyttsx3.init()
	sound = engine.getProperty('voices')

	for i in str(talk).splitlines():
		engine.say(talk)
	engine.runAndWait()
	

def listen():
	mic = sr.Microphone()
	r = sr.Recognizer()
	with mic as source:
		audio = r.listen(source, phrase_time_limit= 5)
	
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
		#print("webbrowser opened")
		bot("Your web browser is opened! ")
	elif "time" in command:
		current = datetime.datetime.now()
		print(current)




main(listen())