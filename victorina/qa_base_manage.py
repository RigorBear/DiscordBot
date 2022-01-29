import sqlite3

conn = sqlite3.connect("qa_base.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

def create_users(cursor):
    cursor.execute("""CREATE TABLE users (user_id, name, status, rating)""")

def create_qa_pairs(cursor):
    cursor.execute("""CREATE TABLE qa_pairs (Id INTEGER PRIMARY KEY, question, answer)""")

def add_null_user(cursor):
    cursor.execute("INSERT INTO users (user_id, name, status, rating) VALUES (?,?,?,?)", ("000000075260007488", "Test", 'начинающий', 10))
create_users(cursor)
create_qa_pairs(cursor)

add_null_user(cursor)
