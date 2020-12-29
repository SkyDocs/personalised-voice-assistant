import sys
sys.path.insert(0, "../")
from cli import	voice_assistant as vs

class user_0(vs.VoiceAssistant):

	def dec_msg(self):
		print("\033[31m[*] Voice Assistant for User 0 is triggered.\033[0m")

	def bot(self, talk):
		print(talk)

		engine = pyttsx3.init()
		sound = engine.getProperty('voices')
		engine.setProperty('voice', sound[33].id)

		for i in str(talk).splitlines():
			engine.say(talk)
			engine.runAndWait()

def predict():
	u0 = user_0()
	u0.dec_msg()
	u0.listen()