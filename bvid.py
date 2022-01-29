#!/usr/bin/env python3

from googleapiclient.discovery import build
from googlesearch import search
from bs4 import BeautifulSoup
import random
from tokens import yt_token
import requests
import string

#import urllib2
#import simplejson
#import cStringIO

from lxml import html
#from google_images_search import GoogleImagesSearch

DEVELOPER_KEY = yt_token.DEVELOPER_KEY
SEARCH_KEY = yt_token.SEARCH_KEY
CX_KEY = yt_token.CX_KEY
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(word):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=word,
    part='snippet',
    maxResults=100
  ).execute()

  videos = []

  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s' % (search_result['id']['videoId']))

  if len(videos) == 0:
    result = "По запросу " + "{" + word + "} - нихуя не найдено!"
  else:
    result = 'https://www.youtube.com/watch?v=' + videos[random.randint(0, len(videos)-1)]

  return result

def g_search(query, index=0):
   fallback = 'Sorry, I cannot think of a reply for that.'
   result = ''

   try:
       search_result_list = list(search(query, lang="ru", tld="co.in", num=10, stop=3, pause=1))

       for elem in search_result_list:

           page = requests.get(elem)
           soup = BeautifulSoup(page.content, features="lxml")
           article_text = ''
           article = soup.findAll('p')
           for element in article:
               article_text += '\n' + ''.join(element.findAll(text=True))
           article_text = article_text.replace('\n', '')
           first_sentence = article_text.split('.')
           first_sentence = first_sentence[0].split('?')[0]

           chars_without_whitespace = first_sentence.translate(
               {ord(c): None for c in string.whitespace}
           )
           if len(chars_without_whitespace) > 0:
                result = result + "**" + str(search_result_list.index(elem) + 1) + '. ' + first_sentence + '...** \n' + elem + '\n'
           else:
                continue
       return result
   except:
       if len(result) == 0: result = fallback
       return result

def image_search(query):


    #fetcher = urllib2.build_opener()
    #startIndex = 0
    #searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + query + "&start=" + startIndex
    #f = fetcher.open(searchUrl)
    #deserialized_output = simplejson.load(f)

    #imageUrl = deserialized_output['responseData']['results'][0]['unescapedUrl']
    #file = cStringIO.StringIO(urllib.urlopen(imageUrl).read())
    #img = Image.open(file)


        return 'Пикча не найдена!'