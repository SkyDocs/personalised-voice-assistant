import os
clear = lambda: os.system('clear')
clear()
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
from subprocess import call

def bot(talk):
	print(talk)

	engine = pyttsx3.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', 160)
	volume = engine.getProperty('volume')
	engine.setProperty('volume', 1.0)
	sound = engine.getProperty('voices')
	engine.setProperty('voice', sound[33].id)

	for i in str(talk).splitlines():
		engine.say(talk)
	engine.runAndWait()


def listen():
	mic = sr.Microphone()
	r = sr.Recognizer()
	with mic as source:
		print("\033[31m[*]\033[0m Say Something...")
		audio = r.listen(source, phrase_time_limit=5)

	try:
		command = r.recognize_google(audio).lower()
		print("You said : " + command)
		# main(command)

	except sr.UnknownValueError:
		# print("Error occured, try again")
		print("Sorry I did not get that. Please try again.")
		command = listen()

	return command

# def activate(talk):
# 	wake_words = {'ok siri'}

# 	talk = talk.lower()
# 	for phrase in wake_words:
# 		if phrase in talk:
# 			return True
# 	return False

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


def main():
	print("\033[31m[*] General Voice Assistant triggered.\033[0m")
	command = listen()
	if "hello" in command:
		current_time = int(strftime('%H'))
		if current_time < 12:
			bot("Hello, Good morning, this is your voice assistant.")
		elif 12 <= current_time < 16:
			bot("Hello, Good afternoon, this is your voice assistant.")
		else:
			bot("Hello, Good evening, this is your voice assistant.")

	elif "who made you" in command:
		bot("I was developed by The Team SkyDocs.")

	elif "how are you" in command:
		bot("I am great. Hoping the same for you.")

	elif "your name" in command:
		bot("My name is Bella.")

	elif "who am i" in command:
		bot("I am the general user. I am not giving the presonalised voice assistant.")
		bot("To activate the presonalised voice assistant say RECOGNISE")

	elif "feature" in command:
		bot("I have lot of features, Some of my features are given below:")
		bot("Say recognise to recognise the user and give presonalised results")
		bot("Greetings")
		bot("Play Video")
		bot("Web Search")
		bot("Give Latest News")
		bot("Add Notes and many more...")
		bot("why not try something and get started.")

	elif "recognise" in command:
		bot("You will be redirected to the recognition part!")
		call(["python", "predict.py"])

	elif "joke" in command:
		bot(pyjokes.get_joke())

	elif "google" in command:
		webbrowser.open("https://www.google.com")
		bot("Check your default web browser!")

	elif 'time' in command:
		now = datetime.datetime.now()
		bot('Current time is %d hours %d minutes' % (now.hour, now.minute))

	elif "play video" in command:

		bot("What to play?")
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

	elif "shop" in command:

		bot("what you want to shop?")
		q = sr.Recognizer()
		t = 0
		with sr.Microphone() as source:
			print("search for the term:")
			while t == 0:
				audio = q.listen(source, phrase_time_limit=5)
				try:
					query = q.recognize_google(audio)
					print('you said :{}'.format(query))
					bot('Here you go')
					bot('Happy shoping!')
					t = 1
				except:
					print('Not understandable')
					print('Try again')
					t = 0
		url = "https://www.amazon.in/s?k=" + query
		webbrowser.open(url)

	elif "write note" in command:
		bot("What should I write?")
		note = write_note()
		file = open('general.txt', 'w')
		file.write(note)

	elif "show notes" in command:
		bot("Searching for Notes")
		try:
			file = open("general.txt", "r")
			bot(file.read())
		except FileNotFoundError:
			bot("No notes are available.")
			bot("Want to create one now?")
			q = sr.Recognizer()
			t = 0
			with sr.Microphone() as source:
				while t == 0:
					audio = q.listen(source, phrase_time_limit=5)
					try:
						res = q.recognize_google(audio)
						t = 1
						if "yes" in res:
							bot("What should I write?")
							file = open('general.txt', 'w')
							note = write_note()
							file.write(note)
							print("A new note is created!")
						else:
							bot("Okay, exiting the note section")
					except:
						print('Not understandable')
						print('Try again')
						t = 0
			bot("A new note is created!")

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
			news_url = "https://news.google.com/news/rss"
			Client = urlopen(news_url)
			xml_page = Client.read()
			Client.close()
			soup_page = soup(xml_page, "xml")
			news_list = soup_page.findAll("item")
			for news in news_list[:15]:
				bot(news.title.text.encode('utf-8'))
		except Exception as e:
			print(e)

	elif "map" in command:
		bot("opening maps powered by google")
		maps_url = "https://www.google.co.in/maps"
		webbrowser.open(maps_url)

	elif "shutdown" in command:
		bot("You are going to poweroff your system. Are you sure?")
		listen()
		if "yes" in command:
			os.system("poweroff")
		else:
			bot("You have aborted the process. Returning back to previous state")
			main(listen())

	# google search
	elif 'search' in command:
		bot('What to search?')
		# listen()

		w = sr.Recognizer()
		t = 0

		with sr.Microphone() as source:
			print('Search for the term:')
			# print(t)

			while t == 0:
				audio = w.listen(source, phrase_time_limit=5)
				try:
					# print('in try block')
					query = w.recognize_google(audio).lower()
					print('you said :{}'.format(query))
					t = 1

				except:
					print('Not understandable')
					print('Try again')
					t = 0

		webbrowser.open("https://google.com/search?q=%s" % query)

	elif "remind" in command:
		bot("What shall I remind you about?")
		text = listen()
		bot("In how many minutes ?")
		local_time = float(listen())
		local_time = local_time * 60
		time.sleep(local_time)
		bot(text)

	elif "bye" in command:
		bot("Bye!")
		sys.exit()

	elif "thank you" in command:
		bot("Pleasure to serve you!")
		sys.exit()

	else:
		bot("I am sorry, I am unable to process your request.")
