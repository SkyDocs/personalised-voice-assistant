from cli.utils import user, bot

def main():
	if user.user == 0:
        bot.bot("I am the general user. I am not giving the presonalised voice assistant.")
        bot.bot("To activate the presonalised voice assistant say RECOGNISE")

    elif user.user == 1:
        bot.bot("You the registered User 0!")
        bot.bot("Welcome back!")

    elif user.user == 2:
        bot.bot("You the registered User 1!")
        bot.bot("Welcome back!")

    elif user.user == 3:
        bot.bot("You the registered User 2!")
        bot.bot("Welcome back!")
