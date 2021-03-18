import speech_recognition as sr
from users import user

def listen():
    mic = sr.Microphone()
    r = sr.Recognizer()
    with mic as source:
        if user.user == 0:
            print("\033[31m[*] General User \033[0m")
            print("say something...")
            audio = r.listen(source, phrase_time_limit=5)
        elif user.user == 1:
            print("\033[31m[*] User 0 \033[0m")
            print("say something...")
            audio = r.listen(source, phrase_time_limit=5) 
        elif user.user == 2:
            print("\033[31m[*] User 1 \033[0m")
            print("say something...")
            audio = r.listen(source, phrase_time_limit=5)
        elif user.user == 3:
            print("\033[31m[*] User 2 \033[0m")
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