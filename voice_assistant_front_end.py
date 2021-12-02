import base64
import requests
import speech_recognition as sr
import pyttsx3
import json


def listen():
	mic = sr.Microphone()
	r = sr.Recognizer()

	with mic as source:
		print("listening")
		audio = r.listen(source, phrase_time_limit = 5)
		try:
			command = r.recognize_google(audio).lower()
			print(command)
		except sr.UnknownValueError:
			command = listen()
	return command


# command = "hello"
# command = command.encode("utf-8")

def bot(response):
	voice_id = "english-north"

	engine = pyttsx3.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', 190)
	volume = engine.getProperty('volume')
	engine.setProperty('volume', 1.0)
	sound = engine.getProperty('voices')
	engine.setProperty('voice', voice_id)

	for i in str(response).splitlines():
		engine.say(response)
	engine.runAndWait()


def main():
	command = listen()
	command = base64.b64encode(command.encode("utf-8"))
	command = str(command, "utf-8")

	# command = command.decode("utf-8")

	url = "http://127.0.0.1:8080"

	response = requests.post(url,json = {"command":command})

	response = response.text.strip()
	print(response)

	response = json.loads(response)

	response = response['response']
	
	print(response)
	bot(response)

while True:
	main()