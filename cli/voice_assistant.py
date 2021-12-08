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


# def main():
#     func(listen.listen())


def func(command, user_id):
    if "hello" in command:
        current_time = int(strftime('%H'))
        if current_time < 12:
            # return("Hello, Good morning, this is your voice assistant.")
            return ("Hello, Good morning, this is your voice assistant.")
        elif 12 <= current_time < 16:
            # return("Hello, Good afternoon, this is your voice assistant.")
            return ("Hello, Good afternoon, this is your voice assistant.")
        else:
            # return("Hello, Good evening, this is your voice assistant.")
            return ("Hello, Good evening, this is your voice assistant.")

    elif "who made you" in command:
        return("I was developed by The Team SkyDocs.")

    elif "how are you" in command:
        return("I am great. Hoping the same for you.")

    elif "your name" in command:
        return("I dont have a name yet. Would like to give me one?")

    elif "who am i" in command:
        return(whoami.main(user_id))

    elif "feature" in command:
        return("I have lot of features, Some of my features are given below:")
        return("Say recognise to recognise the user and give presonalised results")
        return("Greetings")
        return("Play Video")
        return("Web Search")
        return("Give Latest News")
        return("Add Notes and many more...")
        return("why not try something and get started.")

    elif "recognise" in command:
        return("You will be redirected to the recognition part!")
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
        return(pyjokes.get_joke())

    elif "google" in command:
        search.search()

    elif 'time' in command:
        now = datetime.datetime.now()
        return('Current time is %d hours %d minutes' % (now.hour, now.minute))

    elif "play video" in command:
        play_video.play_video()

    elif "shop" in command:
        shop.shop()

    elif "prime video" in command:
        amazon_prime.amazon_prime()

    elif "show notes" in command:
        notes.main()

    elif "gmail" in command:
        return("sure, opening gmail")
        url_mail = "https://www.gmail.com"
        webbrowser.open(url_mail)

    elif "wikipedia" in command:
        return("Sure! Here you go.")
        url_wiki = "https://www.wikipedia.org/"
        webbrowser.open(url_wiki)

    elif "news" in command:
        news.news()

    elif "map" in command:
        map.map()

    elif "shutdown" in command:
        return("You are going to poweroff your system. Are you sure?")
        listen()
        if "yes" in command:
            os.system("poweroff")
        else:
            return("You have aborted the process. Returning back to previous state")
            main(listen())

    elif 'search' in command:
        search.search()

    elif "remind" in command:
        return("What shall I remind you about?")
        text = listen()
        return("In how many minutes ?")
        local_time = float(listen())
        local_time = local_time * 60
        time.sleep(local_time)
        return(text)

    elif "calendar" in command:
        calendar.calendar()

    elif "bye" in command:
        return("Bye!")
        sys.exit()

    elif "thank you" in command:
        return("Pleasure to serve you!")
        sys.exit()

    else:
        # return("I am sorry, I am unable to process your request.")
        return command
