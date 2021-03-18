import os
clear = lambda: os.system('clear')
clear()

print("\033[31m[*] General Voice Assistant triggered.\033[0m")

import sys
import webbrowser
from time import strftime
import pyjokes
import subprocess
import datetime
import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from subprocess import call
from cli.utils import *


def main():
	func(listen.listen())

def func(command):
	if "hello" in command:
		current_time = int(strftime('%H'))
		if current_time < 12:
			bot.bot("Hello, Good morning, this is your voice assistant.")
		elif 12 <= current_time < 16:
			bot.bot("Hello, Good afternoon, this is your voice assistant.")
		else:
			bot.bot("Hello, Good evening, this is your voice assistant.")

	elif "who made you" in command:
		bot.bot("I was developed by The Team SkyDocs.")

	elif "how are you" in command:
		bot.bot("I am great. Hoping the same for you.")

	elif "your name" in command:
		bot.bot("My name is Bella.")

	elif "who am i" in command:
		bot.bot("I am the general user. I am not giving the presonalised voice assistant.")
		bot.bot("To activate the presonalised voice assistant say RECOGNISE")

	elif "feature" in command:
		bot.bot("I have lot of features, Some of my features are given below:")
		bot.bot("Say recognise to recognise the user and give presonalised results")
		bot.bot("Greetings")
		bot.bot("Play Video")
		bot.bot("Web Search")
		bot.bot("Give Latest News")
		bot.bot("Add Notes and many more...")
		bot.bot("why not try something and get started.")

	elif "recognise" in command:
		bot.bot("You will be redirected to the recognition part!")
		cur_dir = os.getcwd()
		parent_dir = os.path.dirname(cur_dir)
		if (cur_dir == os.path.join(parent_dir, "cli")):
			# print('found')
			pass
		else:
			os.chdir("cli")
			# print('done')
		call(["python", "predict.py"])

	elif "joke" in command:
		bot.bot(pyjokes.get_joke())

	elif "google" in command:
		webbrowser.open("https://www.google.com")
		bot.bot("Check your default web browser!")

	elif 'time' in command:
		now = datetime.datetime.now()
		bot.bot('Current time is %d hours %d minutes' % (now.hour, now.minute))

	elif "play video" in command:
		play_video.play_video()

	elif "shop" in command:

		bot.bot("what you want to shop?")
		q = sr.Recognizer()
		t = 0
		with sr.Microphone() as source:
			print("search for the term:")
			while t == 0:
				audio = q.listen(source, phrase_time_limit=5)
				try:
					query = q.recognize_google(audio)
					print('you said :{}'.format(query))
					bot.bot('Here you go')
					bot.bot('Happy shoping!')
					t = 1
				except:
					print('Not understandable')
					print('Try again')
					t = 0
		url = "https://www.amazon.in/s?k=" + query
		webbrowser.open(url)

	elif "write note" in command:
		bot.bot("What should I write?")
		note = write_note.write_note()
		file = open('general.txt', 'w')
		file.write(note)

	elif "show notes" in command:
		bot.bot("Searching for Notes")
		try:
			file = open("general.txt", "r")
			bot.bot(file.read())
		except FileNotFoundError:
			bot.bot("No notes are available.")
			bot.bot("Want to create one now?")
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
							file = open('general.txt', 'w')
							note = write_note.write_note()
							file.write(note)
							print("A new note is created!")
						else:
							bot.bot("Okay, exiting the note section")
					except:
						print('Not understandable')
						print('Try again')
						t = 0
			bot.bot("A new note is created!")

	elif "gmail" in command:
		bot.bot("sure, opening gmail")
		url_mail = "https://www.gmail.com"
		webbrowser.open(url_mail)

	elif "wikipedia" in command:
		bot.bot("Sure! Here you go.")
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
				bot.bot(news.title.text.encode('utf-8'))
		except Exception as e:
			print(e)

	elif "map" in command:
		bot.bot("opening maps powered by google")
		maps_url = "https://www.google.co.in/maps"
		webbrowser.open(maps_url)

	elif "shutdown" in command:
		bot.bot("You are going to poweroff your system. Are you sure?")
		listen()
		if "yes" in command:
			os.system("poweroff")
		else:
			bot.bot("You have aborted the process. Returning back to previous state")
			main(listen())

	# google search
	elif 'search' in command:
		bot.bot('What to search?')
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
		bot.bot("What shall I remind you about?")
		text = listen()
		bot.bot("In how many minutes ?")
		local_time = float(listen())
		local_time = local_time * 60
		time.sleep(local_time)
		bot.bot(text)

	elif "bye" in command:
		bot.bot("Bye!")
		sys.exit()

	elif "thank you" in command:
		bot.bot("Pleasure to serve you!")
		sys.exit()

	else:
		bot.bot("I am sorry, I am unable to process your request.")

