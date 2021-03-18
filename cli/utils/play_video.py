# Firefox won't auto-play the video when opened. 
# Ref: https://support.mozilla.org/bm/questions/1260002

import re
import urllib.request
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

	query = "https://www.youtube.com/results?search_query=" + query.replace(' ', '+') 
	html = urllib.request.urlopen(query)
	url = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	# print(html)
	# print(url)
	# print("http://www.youtube.com/watch?v=" + url[0])
	webbrowser.open("http://www.youtube.com/watch?v={}".format(url[0]))

