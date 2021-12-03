import base64
from flask import Flask, jsonify, request, redirect
from flask_cors import CORS

from cli import voice_assistant as vs


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
def general():
	data_ret = request.get_json()
	command = data_ret["command"]
	command = base64.b64decode(command)
	command = str(command, "utf-8")

	# call the main function
	response = vs.func(command)

	response = {
		"response": response
	}
	response = jsonify(response)
	
	return response


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


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080)