import webbrowser
from cli.utils import bot
import speech_recognition as sr

# google search


def search():
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
