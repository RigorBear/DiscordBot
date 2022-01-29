import sqlite3
from datetime import datetime
from random import randint
from random import choice
from random import randrange
import re

random_fins = [', понимаешь?', '.', ', улавливаешь?', ', ок?', ', ага.', ', сука!', ' блять.', '. Такая хуйня...', '..',
               '...']

endstr = ['...', '.', '!', '?', '...\n', '.\n', '!\n', '?\n']

def add_phrases(phrase) -> object:

    # подключаемся к базе
    conn = sqlite3.connect("database/mcbase2.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    # разобъём входную фразу на слова
    lst = phrase.split()

    for i in range(len(lst) - 1):
        if i == 0:
            place = "START"
        elif i+2 == len(lst) - 1:
            place = "FIN"
        else:
            place = "MID"

        word1 = lst[i]

        if i+1 <= len(lst) - 1:
            word2 = lst[i+1]
        else:
            word2 = ''
            place = "FIN"

        if i+2 <= len(lst) - 1:
            word3 = lst[i+2]
            word3_clean = clean_phrase(word3)
            if word3_clean == '':
                place = "MID"
            elif any(word3_clean[len(word3_clean)-1] in e for e in endstr):
                place = "FIN"

        else:
            word3 = ''
            place = "FIN"


        triple = (word1, word2, word3, place)

        # определим есть ли в базе это слово
        cursor.execute('SELECT COUNT(*) FROM triples WHERE word1 LIKE ? AND word2 LIKE ? AND word3 LIKE ? AND place LIKE ?', triple)
        count_find = cursor.fetchone()
        if count_find[0] == 0:
            cursor.execute("INSERT INTO triples (word1, word2, word3, place) VALUES (?,?,?,?)", triple)
            conn.commit()


def create_phrase(user_phr, maxlen):

    # подкючаемся к базе
    conn = sqlite3.connect("database/mcbase2.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    # найдём общее количество записей в таблице фраз, для того чтобы определить зону поиска
    cursor.execute('SELECT COUNT(*) FROM triples')
    count_table = cursor.fetchone()

    len_new_phr = randint(1, maxlen)    # длина генерируемого ответа

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

    i = 0

    while i <= len_new_phr:
        cursor.execute('SELECT word1,word2,word3,place FROM triples WHERE word1 LIKE ? AND word2 LIKE ?', last_words)
        #if i == len_new_phr-1:
        #   last_words = (fresult[1], fresult[2], "FIN")
        #    cursor.execute('SELECT word1,word2,word3,place FROM triples WHERE word1 LIKE ? AND word2 LIKE ? AND place LIKE ?', last_words)


        results = cursor.fetchall()
        #if len(results) == 0:
        #    cursor.execute('SELECT word1,word2,word3,place FROM triples WHERE place LIKE ?', ["FIN"])
        #    results = cursor.fetchall()
        try:
            fresult = choice(results)
            new_phrase = new_phrase + " " + fresult[2]
            last_words = (fresult[1], fresult[2])
        except Exception:
            new_phrase = new_phrase + choice(random_fins)
            return new_phrase

        if i == len_new_phr and fresult[3] != "FIN":
            len_new_phr = len_new_phr + 1

        i = i + 1

    return new_phrase

def create_poem(user_phr):

    # подкючаемся к базе
    conn = sqlite3.connect("database/mcbase2.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    # найдём общее количество записей в таблице фраз, для того чтобы определить зону поиска
    cursor.execute('SELECT COUNT(*) FROM triples')
    count_table = cursor.fetchone()

    len_new_phr = randrange(3, 15, 2)    # длина генерируемого ответа

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
    #rand_use_fword = randint(0, 10)

    # Если условия соблюдены, первую пару слов берём случайно из results
    # Иначе берём просто случайную тройку слов из базы
    if finded == True:
        fresult = choice(results)
    else:
        int_id = (randint(1, count_table[0]))
        cursor.execute('SELECT word1,word2,word3 FROM triples WHERE Id=?', [int_id])
        fresult = cursor.fetchone()

    new_phrase = str(fresult[0]) + " " + str(fresult[1]) + " " + fresult[2]
    last_phrase = fresult
    # запомним окончание последнего слова
    word_fin = str(fresult[2])
    word_fin = word_fin.replace('-', '')
    word_fin = word_fin.replace('?', '')
    word_fin = word_fin.replace('.', '')
    word_fin = word_fin.replace(',', '')
    word_fin = '%' + word_fin[-3:]
    last_words = (word_fin, word_fin)

    rifm = False
    i = len_new_phr
    print(len_new_phr)
    error_itr = 0
    while i > 0:
        print('_')
        if rifm == False:
            cursor.execute('SELECT word1,word2,word3,place FROM triples WHERE word3 LIKE ? OR word3 LIKE ?', last_words) # OR word2 LIKE ?
            results = cursor.fetchall()

            try:
                fresult = choice(results)

                if fresult != last_phrase and fresult[2] != last_phrase[2]:
                    new_phrase = new_phrase + '\n' + fresult[0] + " " + fresult[1] + " " + fresult[2]
                    rifm = True
                    i = i - 1
                else:
                    error_itr = error_itr + 1
                    print('Пропуск ' + str(i))
                    if error_itr == 2:
                        rifm = True
                    if error_itr == 3:
                        new_phrase = 'Иди нахуй со своими стихами'
                        break
            except Exception:
                new_phrase = new_phrase + "."

        elif rifm == True:
            int_id = (randint(1, count_table[0]))
            cursor.execute('SELECT word1,word2,word3 FROM triples WHERE Id=?', [int_id])
            fresult = cursor.fetchone()

            try:
                new_phrase = new_phrase + '\n' + fresult[0] + " " + fresult[1] + " " + fresult[2]
                last_phrase = fresult
                rifm = False
                i = i-1
            except Exception:
                new_phrase = new_phrase + "."

        word_fin = str(fresult[2])
        word_fin = word_fin.replace('-', '')
        word_fin = word_fin.replace('?', '')
        word_fin = word_fin.replace('.', '')
        word_fin = word_fin.replace(',', '')
        word_fin = '%' + word_fin[-3:]
        last_words = (word_fin, word_fin)
        last_phrase = fresult

    return new_phrase

def clean_phrase(text):
    clean_text = re.sub('[^\x00-\x7Fа-яА-Я]', '', text)
    return clean_text