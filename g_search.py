import requests
import string
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup
import discogs_client
from tokens import yt_token
from random import choice
from random import randint

# to search
# print(chatbot_query('how old is samuel l jackson'))


def discogs_search(query):

    search = {'Жанр': '', 'Исп': '', 'Релиз': '', 'Стиль': ''}

    if len(query) > 0:
        query_list = query.split('/')
        search_str = query_list[0]

        if len(query_list) > 1:
            query_list.remove(search_str)
            for i in query_list:
                pair = i.split(':')
                if len(pair) > 1:
                    if pair[0] in search.keys():
                        search[pair[0]] = pair[1]


    d = discogs_client.Client('ExampleApplication/0.1', user_token=yt_token.DISCOGS_TOKEN)

    results = d.search(search_str, type = 'release', artist=search['Исп'], release=search['Релиз'],
                       style=search['Стиль'], genre=search['Жанр'])

    max_results = 0

    if len(results) == 0:
        return 'Результатов не найдено'
    elif len(results) > 5:
        max_results = 5
    else:
        max_results = len(results)


    max_page = results.pages
    random_page = randint(1, max_page)

    result_str = 'Найдено:'

    output = []
    response = ''
    random_res = choice(results.page(random_page))

    for j in range(max_results):
        while output.count(random_res) > 0:
            random_res = choice(results.page(random_page))

        output.append(random_res)



    for record in output:
        try:
            artist = ','.join(str(e.name) for e in record.artists)
        except:
            artist = 'Unknown artist'
        title = str(record.title)
        country = str(record.country)
        year = str(record.year)
        try:
            styles = ','.join(str(e) for e in record.styles)
        except:
            styles = 'None style'
        jres = '\n' + str(output.index(record) + 1) + '. ' + artist + ' - ' + title + ' (' + country + ', ' + year + ') [' \
                + styles + ']'

        response = response + jres


    return response

