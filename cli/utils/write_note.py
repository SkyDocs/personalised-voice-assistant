import speech_recognition as sr

def write_note():
	mic = sr.Microphone()
	r = sr.Recognizer()
	with mic as source:
		print("What to write in the note!")
		note = r.listen(source)
	try:
		note = r.recognize_google(note).lower()
		print("The note will be written as: " + note)
	except sr.UnknownValueError:
		print("Sorry I didn't get you. Kindly say again.")
		note = write_note()

	return note
