import sqlite3

conn = sqlite3.connect("igbase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

def create_db(cursor):
    cursor.execute("""CREATE TABLE users (user_id, name, status, lastdate, rating, bot, discriminator, avatar)""")

def create_pairs_table(cursor):
    cursor.execute("""CREATE TABLE three_pix (Id INTEGER PRIMARY KEY, pix1, pix2, pix3)""")

def add_user(userdict: dict):
    user = [(userdict.get('id'), userdict.get('name'), 'online', '04.07.2020', 0, userdict.get('bot'),
             userdict.get('discriminator'), userdict.get('avatar'))]

    cursor.executemany("INSERT INTO users VALUES (?,?,?,?,?,?,?,?)", user)

    conn.commit()

create_db(cursor)
create_pairs_table(cursor)

user = {'id': 1231, 'name': 'Test', 'bot': 1, 'discriminator': 12123, 'avatar': 'kkks'}

add_user(user)

print(conn)