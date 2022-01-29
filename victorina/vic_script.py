import sqlite3
from datetime import datetime
from random import randint
from random import choice

def question():

    conn = sqlite3.connect("victorina/qa_base.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM qa_pairs')
    count_table = cursor.fetchone()

    id_qa = randint(1,  count_table[0])

    cursor.execute('SELECT question,answer FROM qa_pairs WHERE Id=?', [id_qa])

    fresult = cursor.fetchone()

    print(id_qa, fresult[0])
    qa_struct = (id_qa, fresult[0], fresult[1])

    return qa_struct


def answer_check(text, id_qa, player):

    conn = sqlite3.connect("victorina/qa_base.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    cursor.execute('SELECT question,answer FROM qa_pairs WHERE Id=?', [id_qa])

    fresult = cursor.fetchone()



    presult = get_user(player, cursor)

    rating = presult[3]

    if text == fresult[1]:
        rating = rating + randint(1, len(fresult[0]))
        result = str(presult[1]) + " ответил верно! Текущий рейтинг: " + str(rating)
        answered = True
    else:
        rating = rating - randint(1, len(fresult[1]))
        result = "Ответ неверный! Ваш текущий рейтинг: " + str(rating)
        answered = False

    cursor = conn.cursor()
    assert isinstance(cursor, object)
    cursor.execute('UPDATE users SET rating=? WHERE user_id=?', (rating, str(player[0])))
    conn.commit()
    conn.close()

    full_result = (result, answered, fresult[0])

    return full_result

def get_user(player, cursor):

    cursor.execute('SELECT COUNT(*) FROM users WHERE user_id=?', [str(player[0])])
    count_find = cursor.fetchone()

    if count_find[0] == 0:
        cursor.execute("INSERT INTO users (user_id, name, status, rating) VALUES (?,?,?,?)", (str(player[0]), player[1], 'начинающий', 10))

    cursor.execute('SELECT user_id, name, status, rating FROM users WHERE user_id=?',  [str(player[0])])

    presult = cursor.fetchone()

    return presult