from cli.utils import bot
import webbrowser


def calendar():
    bot.bot("Opening Calendar")
    url = "https://calendar.google.com/calendar/"
    webbrowser.open(url)
