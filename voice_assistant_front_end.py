import base64
import requests
import pyttsx3
import json
import time
import pyaudio
import wave
import validators

user_id = 0

# def recognise():
# 	print("\033[31m[*]\033[0m You will be asked to speak for few seconds for the recognition of the speaker.")
# 	time.sleep(3)
# 	print("\033[31m[*]\033[0m Get Ready!")

def listen():
	""" Taking the voice input """

	chunk = 1024  # Record in chunks of 1024 samples
	sample_format = pyaudio.paInt16  # 16 bits per sample
	channels = 2
	fs = 16000  # Record at 16000 samples per second
	seconds = 3
	filename = "predict.wav"

	p = pyaudio.PyAudio()  # Create an interface to PortAudio

	# print("-------------------------------------------------------------------------------------------")
	print("\033[31m[*]\033[0m Recording")

	stream = p.open(format=sample_format,
					channels=channels,
					rate=fs,
					frames_per_buffer=chunk,
					input=True)

	frames = []  # Initialize array to store frames

	# Store data in chunks for 1 seconds
	for i in range(0, int(fs / chunk * seconds)):
		data = stream.read(chunk)
		frames.append(data)

	# Stop and close the stream
	stream.stop_stream()
	stream.close()
	# Terminate the PortAudio interface
	p.terminate()

	print("\033[31m[*]\033[0m Finished recording")
	# print("-------------------------------------------------------------------------------------------")
	# Save the recorded data as a WAV file
	wf = wave.open(filename, 'wb')
	wf.setnchannels(channels)
	wf.setsampwidth(p.get_sample_size(sample_format))
	wf.setframerate(fs)
	wf.writeframes(b''.join(frames))
	wf.close()

	wav_file = base64.b64encode(filename.encode('utf-8'))
	wav_file = base64.b64encode(open("predict.wav", "rb").read())
	# wav_file = str(wav_file, "utf-8")
	
	return wav_file


# def listen():
# 	mic = sr.Microphone()
# 	r = sr.Recognizer()

# 	with mic as source:
# 		print("listening")
# 		audio = r.listen(source, phrase_time_limit = 5)
# 		try:
# 			command = r.recognize_google(audio).lower()
# 			print(command)
# 		except sr.UnknownValueError:
# 			command = listen()
# 	if command == "recognise":
# 		recognise()

# 	if command = "search":
# 		from cli.utils import search
# 		search()

# 	return command

def validate(response):
	text, url = response.split("\n")
	
	bot(text, user_id)

	if validators.url(url):
		webbrowser.open(url)
	else:
		bot("Sorry this is not a valid url")


def bot(response, user_id):
	if user_id == 0:
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
	else:
		print("user is not general", user_id)

	return


def main():
	command = listen()
	# command = base64.b64encode(command.encode("utf-8"))
	command = str(command, "utf-8")

	# command = command.decode("utf-8")

	url = "http://127.0.0.1:8080"

	response = requests.post(url,json = {"user_audio":command})

	response = response.text.strip()
	print(response)

	response = json.loads(response)

	response = response['response']
	
	print(response)
	validate(response)

while True:
	main()