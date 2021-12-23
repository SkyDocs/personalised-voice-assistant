import base64
from flask import Flask, jsonify, request, redirect
from flask_cors import CORS

from cli import voice_assistant as vs

import speech_recognition as sr

from pydub import AudioSegment
from pydub.playback import play


app = Flask("Personalised Voice Assistant")

CORS(app)

@app.route('/', methods=['GET'])
def home():
	return "Personalised Voice Assistant\n"

@app.route('/about', methods=['GET'])
def about():
	# return redirect('https://github.com/SkyDocs/personalised-voice-assistant')
	return "This is Personalised Voice Assistant. For more visit: https://github.com/SkyDocs/personalised-voice-assistant\n"

@app.route('/', methods=['POST'])
def wav_text():
	data_ret = request.get_json()
	wav_file = data_ret["user_audio"]

	wav = open("temp.wav", "wb")
	wav_file = base64.b64decode(wav_file)
	wav.write(wav_file)
	wav.close()

	song = AudioSegment.from_wav("temp.wav")
	play(song)
	
	r = sr.Recognizer()
	wav = sr.AudioFile('temp.wav')

	with wav as source:
		audio = r.record(source)
	
	try:
		command = r.recognize_google(audio)
		print(command)
		# from cli import main
		# return main.general(command)
	except Exception as e:
		print("Exception "+str(e))

	return "Error"

@app.route('/recongise', methods=['POST'])
def recognise():

	data_ret = request.get_json()
	wav_file = data_ret["user_audio"]
	# get the wav file, and pass it to the pedict function
	wav_file = base64.b64decode(wav_file)

	from cli import predict
	user_id = predict.main(wav_file)
	user_id = {
		"user_id": user_id
	}
	user_id = jsonify(user_id)
	return user_id

# @app.route('/tmp', methods=['POST'])
# def encrypt():
# 	data_ret = request.get_json()
# 	wav_file = data_ret["user_audio"]
# 	wav_file = base64.b64decode(wav_file)

# 	from cli import encrypt
# 	main(wav_file)

# 	return



if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080)