def general(command):
	# call the main function
	response = vs.func(command)

	response = {
		"response": response
	}
	response = jsonify(response)
	
	return response
