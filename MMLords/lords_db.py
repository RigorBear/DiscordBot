import sqlite3



def create_db_lords():
    conn = sqlite3.connect("lords.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE lords (Id INTEGER PRIMARY KEY, type, basic_hp, basic_mp, skill, description, image_path)""")

def create_db_creatures():
    conn = sqlite3.connect("creatures.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE creatures (Id INTEGER PRIMARY KEY, name, type_list, fraction_list, card_cost, use_cost, hp, power, skill_list, level, description, image_path)""")

def create_db_magics():
    conn = sqlite3.connect("magics.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE magics (Id INTEGER PRIMARY KEY, name, effect, type, card_cost, use_cost description, image_path)""")


def create_db_status():
    conn = sqlite3.connect("status.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE status (Id INTEGER PRIMARY KEY, battle_info, first_user_info, second_user_info)""")

def create_db_users():
        conn = sqlite3.connect("users.db")  # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE status (Id INTEGER PRIMARY KEY, user, rating, level, resources, mods)""")

create_db_lords()
create_db_creatures()
create_db_magics()
create_db_status()
create_db_users()