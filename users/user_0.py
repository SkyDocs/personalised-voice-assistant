import os
import sys
import speech_recognition as sr
import webbrowser
from time import strftime
import pyjokes
import subprocess
import datetime
import pyttsx3
import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup



def bot(talk):
	print(talk)

	engine = pyttsx3.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', 180)
	volume = engine.getProperty('volume')
	engine.setProperty('volume', 1.0)
	sound = engine.getProperty('voices')
	# engine.setProperty('voice', sound[33].id)

	for i in str(talk).splitlines():
		engine.say(talk)
	engine.runAndWait()

def listen():
	mic = sr.Microphone()
	r = sr.Recognizer()
	with mic as source:
		print("say something")
		audio = r.listen(source)
	
	try:
		command = r.recognize_google(audio).lower()
		print("You said : " + command)
		# main(command)
	
	except sr.UnknownValueError:
		print("Error occured, try again")
		#bot("Sorry I did not get that. Please try again.")
		command = listen()

	return command	  

# def activate(talk):
# 	wake_words = {'ok siri'}

# 	talk = talk.lower()
# 	for phrase in wake_words:
# 		if phrase in talk:
# 			return True
# 	return False  
	
def main(command):
	if "hello" in command:
		current_time = int(strftime('%H'))
		if current_time < 12:
			bot("Hello, Good morning, this is your voice assistant, developed by Team skydocs.")
		elif 12 <= current_time < 16:
			bot("Hello, Good afternoon, this is your voice assistant, developed by Team skydocs.")
		else:
			bot("Hello, Good evening, this is your voice assistant, developed by Team skydocs.")

	elif "how are you" in command:
		bot("I am great. Hoping the same for you.")

	elif "joke" in command:
		bot(pyjokes.get_joke())		

	elif "open google" in command:
		webbrowser.open("https://www.google.com")
		#print("webbrowser opened")
		bot("Your web browser is opened!")

	elif 'time' in command:
		now = datetime.datetime.now()
		bot('Current time is %d hours %d minutes' % (now.hour, now.minute))

	elif "play the video" in command:

		bot("What to play?")
		q=sr.Recognizer()
		t=0
		with sr.Microphone() as source:
			print("Search for the term:")
			while t==0:
				audio =q.listen(source)
				try:
					query = q.recognize_google(audio)
					print('you said :{}'.format(text))
					t=1
				except:
					print('Not understandable')
					print('Try again')
					t==0
		url = "https://www.youtube.com/results?search_query=" + query 
		webbrowser.open(url)



	elif "gmail" in command:
		bot("sure, opening gmail")
		url_mail = "https://www.gmail.com"
		webbrowser.open(url_mail)

	elif "wikipedia" in command:
		bot("Sure! Here you go.")
		url_wiki = "https://www.wikipedia.org/"
		webbrowser.open(url_wiki)
		
	elif "news" in command:
		try:
			news_url="https://news.google.com/news/rss"
			Client=urlopen(news_url)
			xml_page=Client.read()
			Client.close()
			soup_page=soup(xml_page,"xml")
			news_list=soup_page.findAll("item")
			for news in news_list[:15]:
				bot(news.title.text.encode('utf-8'))
		except Exception as e:
			print(e)


	elif "map" in command:
		bot("opening maps powered by google")
		maps_url = "google.com/maps"
		webbrowser.open(maps_url)

	elif "shutdown" in command:
		bot("You are going to poweroff your system. Are you sure?")
		listen()
		if "yes" in command:
			os.system("poweroff")
		else:
			bot("You have aborted the process. Returning back to previous state")
			main(listen())

	#google search
	elif 'search' in command:
		bot('What to search?')
		#listen()

		w=sr.Recognizer()
		t=0

		with sr.Microphone() as source:
			print('Search for the term:')
			
			while t==0:
				audio = w.listen(source)
				try:
					query =w.recognize_google(audio).lower()
					print('you said :{}'.format(query))
					t=1

				except:
					print('Not understandable')
					print('Try again')
					t=0

		webbrowser.open("https://google.com/search?q=%s" % query)
	
	elif "bye" or "exit" in command:
		bot("Bye!")
		sys.exit()
		
	else:
		bot("I am sorry, I am unable to process your request.")


def predict():
	bot("Welcome user 0. Glad to be back. How may I help you today?")
	while True:
		main(listen())

