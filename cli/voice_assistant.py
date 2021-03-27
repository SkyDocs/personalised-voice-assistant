from cli.utils import *
from subprocess import call
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import datetime
import subprocess
import pyjokes
from time import strftime
import webbrowser
import sys
import os
def clear(): return os.system('clear')


clear()


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
        whoami.main()

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
        search.search()

    elif 'time' in command:
        now = datetime.datetime.now()
        bot.bot('Current time is %d hours %d minutes' % (now.hour, now.minute))

    elif "play video" in command:
        play_video.play_video()

    elif "shop" in command:
        shop.shop()

    elif "prime video" in command:
        amazon_prime.amazon_prime()

    elif "show notes" in command:
        notes.main()

    elif "gmail" in command:
        bot.bot("sure, opening gmail")
        url_mail = "https://www.gmail.com"
        webbrowser.open(url_mail)

    elif "wikipedia" in command:
        bot.bot("Sure! Here you go.")
        url_wiki = "https://www.wikipedia.org/"
        webbrowser.open(url_wiki)

    elif "news" in command:
        news.news()

    elif "map" in command:
        map.map()

    elif "shutdown" in command:
        bot.bot("You are going to poweroff your system. Are you sure?")
        listen()
        if "yes" in command:
            os.system("poweroff")
        else:
            bot.bot("You have aborted the process. Returning back to previous state")
            main(listen())

    elif 'search' in command:
        search.search()

    elif "remind" in command:
        bot.bot("What shall I remind you about?")
        text = listen()
        bot.bot("In how many minutes ?")
        local_time = float(listen())
        local_time = local_time * 60
        time.sleep(local_time)
        bot.bot(text)

    elif "calendar" in command:
        calendar.calendar()

    elif "bye" in command:
        bot.bot("Bye!")
        sys.exit()

    elif "thank you" in command:
        bot.bot("Pleasure to serve you!")
        sys.exit()

    else:
        bot.bot("I am sorry, I am unable to process your request.")
