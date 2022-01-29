import sqlite3
import content_wor

def add_user(user, gclass, channel):

    # подкючаемся к базе
    conn = sqlite3.connect("users.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    new_user = [user, 0, 1, gclass, 0, "", channel, ]

    try:
        cursor.execute("INSERT INTO classes (user, rating, level, class, gold, team, channel, max_hp, hp, min_damage, max_damage, abilities) VALUES (?,?,?,?,?,?,?,?)", lst)
        conn.commit()
        return lord_info(lst[0])
    except:
        return 'Неверно указан класс!'