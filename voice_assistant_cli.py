from cli import voice_assistant as vs
print("\033[31m[*] General Voice Assistant triggered.\033[0m")

while True:
	vs.VoiceAssistant().listen()
