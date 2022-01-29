import requests
from json import loads
from bs4 import BeautifulSoup

def get_img(query):

    s = requests.session()
    #s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'})

    r = s.get('https://www.google.ru/search?q=' + query + '&tbm=isch')

    soup = BeautifulSoup(r.text, "html.parser")

    result = soup.findAll(attrs={'class': 'rg_meta notranslate'})

    for text in soup.findAll(attrs={'class': 'rg_meta notranslate'}):
        text = loads(text.text)
        print(text["ou"])

    return file

 #   for i in range(len({3}))