import pyttsx3
from users import user

def bot(talk):

    if user.user == 0:
        print(talk)
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 160)
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 1.0)
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[33].id)

    elif user.user == 1:
        print(talk)
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[33].id)

    elif user.user == 2:
        print(talk)
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[40].id)

    elif user.user == 3:
        print(talk)
        engine = pyttsx3.init()
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[34].id)

    for i in str(talk).splitlines():
        engine.say(talk)
    engine.runAndWait()
