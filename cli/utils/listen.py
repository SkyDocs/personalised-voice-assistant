import speech_recognition as sr

def listen():
    mic = sr.Microphone()
    r = sr.Recognizer()
    with mic as source:
        print("say something...")
        audio = r.listen(source, phrase_time_limit=5)

    try:
        command = r.recognize_google(audio).lower()
        print("You said : " + command)
        # main(command)

    except sr.UnknownValueError:
        print("Error occured, try again")
        # bot.bot("Sorry I did not get that. Please try again.")
        command = listen()

    return command