import pyttsx3

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
