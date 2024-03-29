from cli.utils import bot
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


def news():
    try:
        news_url = "https://news.google.com/news/rss"
        Client = urlopen(news_url)
        xml_page = Client.read()
        Client.close()
        soup_page = soup(xml_page, "xml")
        news_list = soup_page.findAll("item")
        for news in news_list[:15]:
            bot.bot(news.title.text.encode('utf-8'))
    except Exception as e:
        print(e)
