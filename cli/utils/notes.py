from cli.utils import user, bot, write_note

def write(a):
	file = open("user_" + a + "txt", "w")
	note = write_note.write_note()
	file.write(note)
	print("A new note is created!")

def main():
	bot.bot("Searching for Notes")
	try:
		if user.user == 0:
			file = open("general.txt", "r")
			bot.bot(file.read())
		elif user.user == 1:
			file = open("user_1.txt", "r")
		elif user.user == 2:
			file = open("user_2.txt", "r")
		elif user.user == 3:
			file = open("user_3.txt", "r")

	except FileNotFoundError:
		bot.bot("No notes are available.")
		bot.bot("Want to created one now?")
		q = sr.Recognizer()
		t = 0
		with sr.Microphone() as source:
			while t == 0:
				audio = q.listen(source, phrase_time_limit=5)
				try:
					res = q.recognize_google(audio)
					t = 1
					if "yes" in res:
						bot.bot("What should I write?")
					elif user.user == 0:
						cli.utils.notes.write("0")
					elif user.user == 1:
						cli.utils.notes.write("1")
					elif user.user == 2:
						cli.utils.notes.write("2")
					elif user.user == 3:
						cli.utils.notes.write("3")
					else:
						bot.bot("Okay, exiting the note section")
				except:
					print('Not understandable')
					print('Try again')
					t = 0
		bot.bot("A new note is created!")