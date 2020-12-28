sys.path.insert(0, "../")
from cli import	voice_assistant

class user_0(VoiceAssistant):
	def bot(talk):
		print(talk)

		engine = pyttsx3.init()
		sound = engine.getProperty('voices')
		engine.setProperty('voice', sound[33].id)

		for i in str(talk).splitlines():
			engine.say(talk)
		engine.runAndWait()


def predict:
	vs = voice_assistant()
	vs.listen()
