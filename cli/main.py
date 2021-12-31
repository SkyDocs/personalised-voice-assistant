from flask import jsonify

def general(command, user_id):
	# call the main function
	import cli.voice_assistant as vs
	response = vs.func(command, user_id)

	response = {
		"response": response
	}
	response = jsonify(response)
	
	return response
