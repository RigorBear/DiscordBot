import sqlite3

def create_db_content():
    conn = sqlite3.connect("content.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE classes (Id INTEGER PRIMARY KEY, name, start_level, basic_class, skill, description, min_damage, max_damage, image_path)""")
    cursor.execute("""CREATE TABLE travel_messages (Id INTEGER PRIMARY KEY, text, event_type, image_path)""")
    cursor.execute("""CREATE TABLE enemy_types (Id INTEGER PRIMARY KEY, name, skill, level, basic_exp, min_damage, max_damage, image_path)""")
    cursor.execute("""CREATE TABLE pre_mods (Id INTEGER PRIMARY KEY, name, skill, exp_mod, image_path)""")
    cursor.execute("""CREATE TABLE post_mods (Id INTEGER PRIMARY KEY, name, skill, exp_mod, image_path)""")


def create_db_users():
        conn = sqlite3.connect("users.db")  # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE users (Id INTEGER PRIMARY KEY, user, rating, level, class, gold, team, channel, max_hp, hp, min_damage, max_damage, abilities)""")


def create_db_names():
    conn = sqlite3.connect("names.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE first_names (Id INTEGER PRIMARY KEY, part1, part2, part3, part4, enemy_type)""")
    cursor.execute(
        """CREATE TABLE second_names (Id INTEGER PRIMARY KEY, part1, part2, part3, part4, enemy_type)""")

def create_db_logs():
    conn = sqlite3.connect("logs.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE main_log (Id INTEGER PRIMARY KEY, channel, message)""")
    cursor.execute(
        """CREATE TABLE monsters (Id INTEGER PRIMARY KEY, name, hp, damage, skills, channel, date, status, description)""")

create_db_content()
create_db_users()
