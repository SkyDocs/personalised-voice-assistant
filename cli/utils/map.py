import webbrowser
from cli.utils import bot
import speech_recognition as sr


def map():
    bot.bot("opening maps!")
    q = sr.Recognizer()
    t = 0
    with sr.Microphone() as source:
        bot.bot("what place you want to search for ?")
        print("search for the place:")
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
    maps_url = "https://www.google.com/maps?q=" + query
    webbrowser.open(maps_url)
