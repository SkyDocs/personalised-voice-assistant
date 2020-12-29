import sys
sys.path.insert(0, "../")
from cli import	voice_assistant as vs

class user_1(vs.VoiceAssistant):

	def dec_msg(self):
		print("\033[31m[*] Voice Assistant for User 1 is triggered.\033[0m")

	def bot(self, talk):
		print(talk)
		print("---")
		engine = pyttsx3.init()
		sound = engine.getProperty('voices')
		engine.setProperty('voice', sound[32].id)

		for i in str(talk).splitlines():
			engine.say(talk)
			engine.runAndWait()


def predict():
	u1 = user_1()
	u1.dec_msg()
	u1.listen()
