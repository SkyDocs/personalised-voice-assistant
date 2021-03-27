from cli.utils import bot
import speech_recognition as sr
import webbrowser


def shop():
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
                bot.bot('Happy shopping!')
                t = 1
            except:
                print('Not understandable')
                print('Try again')
                t = 0
    url = "https://www.amazon.in/s?k=" + query
    webbrowser.open(url)
