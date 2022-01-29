import sqlite3
from datetime import datetime
from random import randint
from random import choice
from PIL import

def add_phrases(phrase) -> object:

    # подключаемся к базе
    conn = sqlite3.connect("imgen/igbase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    # запишем тройки пикселей
    lst = phrase.split()
    for i in range(len(lst) - 1):

        if i+1 == len(lst) - 1:
            break

        triple = (lst[i], lst[i + 1], lst[i+2], place)

        # определим есть ли в базе это слово
        cursor.execute('SELECT COUNT(*) FROM three_pix WHERE pix1 LIKE ? AND pix2 LIKE ? AND pix3 LIKE ?', triple)
        count_find = cursor.fetchone()
        if count_find[0] == 0:
            cursor.execute("INSERT INTO triples (word1, word2, word3, place) VALUES (?,?,?,?)", triple)
            conn.commit()


def create_phrase(user_phr):

    # подкючаемся к базе
    conn = sqlite3.connect("database/mcbase2.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    # найдём общее количество записей в таблице фраз, для того чтобы определить зону поиска
    cursor.execute('SELECT COUNT(*) FROM triples')
    count_table = cursor.fetchone()

    len_new_phr = randint(1, 25)    # длина генерируемого ответа

    # разобьём входную фразу на слова, что провести поиск
    lst = user_phr.split()

    new_phrase = ""
    results = ""
    fresult = ""

    # сделаем поиск по случаному слову из сообщения
    fword = choice(lst)

    finded = False

    # определим есть ли в базе записи с данным словом
    cursor.execute('SELECT COUNT(*) FROM triples WHERE word1 LIKE ? AND place LIKE ?', (fword, "START"))
    count_find = cursor.fetchone()

    # если запись есть, выгрузим их в results
    if count_find[0] != 0:
        cursor.execute('SELECT word1,word2,word3,place FROM triples WHERE word1 LIKE ? AND place LIKE ?', (fword, "START"))
        results = cursor.fetchall()
        finded = True

    # определим вероятность использования этой пары слов в генерируемом сообщении
    rand_use_fword = randint(0, 10)

    # Если условия соблюдены, первую пару слов берём случайно из results
    # Иначе берём просто случайную тройку слов из базы
    if finded == True and rand_use_fword > 4:
        fresult = choice(results)
    else:
        int_id = (randint(1, count_table[0]))
        cursor.execute('SELECT word1,word2,word3 FROM triples WHERE Id=?', [int_id])
        fresult = cursor.fetchone()

    new_phrase = str(fresult[0]) + " " + str(fresult[1]) + " " + fresult[2]

    # запомним последние слова
    last_words = (fresult[1], fresult[2])

    for i in range(len_new_phr):
        cursor.execute('SELECT word1,word2,word3,place FROM triples WHERE word1 LIKE ? AND word2 LIKE ?', last_words)
        if i == len_new_phr-1:
            last_words = (fresult[1], fresult[2], "FIN")
            cursor.execute('SELECT word1,word2,word3,place FROM triples WHERE word1 LIKE ? AND word2 LIKE ? AND place LIKE ?', last_words)

        results = cursor.fetchall()
        if len(results) == 0:
            cursor.execute('SELECT word1,word2,word3,place FROM triples WHERE place LIKE ?', ["FIN"])
            results = cursor.fetchall()
        try:
            fresult = choice(results)
            new_phrase = new_phrase + " " + fresult[2]
            last_words = (fresult[1], fresult[2])
        except Exception:
            new_phrase = new_phrase + "."

    return new_phrase
