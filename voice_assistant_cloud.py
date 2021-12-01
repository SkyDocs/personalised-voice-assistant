import base64
from flask import Flask, jsonify, request
from flask_cors import CORS

from cli import voice_assistant as vs


app = Flask("Personalised Voice Assistant")

CORS(app)

@app.route('/', methods=['POST'])

def predict():
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


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)