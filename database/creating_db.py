import sqlite3

conn = sqlite3.connect("discbase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

def create_db(cursor):
    cursor.execute("""CREATE TABLE users (user_id, name, status, lastdate, rating, bot, discriminator, avatar)""")

def create_phrases_table(cursor):
    cursor.execute("""CREATE TABLE phrases (Id INTEGER PRIMARY KEY,phrase, date)""")

def add_user(userdict: dict):
    user = [(userdict.get('id'), userdict.get('name'), 'online', '04.07.2020',0,userdict.get('bot'),
             userdict.get('discriminator'), userdict.get('avatar'))]

    cursor.executemany("INSERT INTO users VALUES (?,?,?,?,?,?,?,?)", user)

    conn.commit()

create_db(cursor)
create_phrases_table(cursor)

user = {'id': 1231, 'name': 'Test', 'bot': 1, 'discriminator': 12123, 'avatar': 'kkks'}

add_user(user)

print(conn)
