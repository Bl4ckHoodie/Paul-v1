import bs4
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
def GetNews():
 news_url = "https://news.google.com/news/rss"
 Client =urlopen(news_url)
 xml_page = Client.read()
 Client.close()
 soup_page = bs(xml_page,"xml")
 news_list = soup_page.findAll("item")
 out =  ""
 for news in news_list:
  out += news.title.text+". \n.\n"
 return out
