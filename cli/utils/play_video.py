from cli.utils import bot
import speech_recognition as sr
import webbrowser

def play_video():
	bot.bot("What to play?")
	q = sr.Recognizer()
	t = 0
	with sr.Microphone() as source:
		print("Search for the term:")
		while t == 0:
			audio = q.listen(source, phrase_time_limit=5)
			try:
				query = q.recognize_google(audio)
				print('you said :{}'.format(query))
				t = 1
			except:
				print('Not understandable')
				print('Try again')
				t = 0
	url = "https://www.youtube.com/results?search_query=" + query
	webbrowser.open(url)

