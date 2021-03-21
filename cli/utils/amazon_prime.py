# for this to function you must be logged-in in your default browser


from cli.utils import bot
import webbrowser
import speech_recognition as sr


def amazon_prime():
    bot.bot("Sure, opening amazon prime video")
    q = sr.Recognizer()
    t = 0
    with sr.Microphone() as source:
        bot.bot("what movie or web-series you want to watch?")
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
    url_ott = "https://www.primevideo.com/search/?phrase=" + query.replace(" ", "%20") + "&ie=UTF8"
    webbrowser.open(url_ott)
