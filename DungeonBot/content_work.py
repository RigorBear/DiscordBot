import sqlite3


def add_class(texts):

    # подкючаемся к базе
    conn = sqlite3.connect("content.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    lst = texts.split("/")

    try:
        cursor.execute("INSERT INTO classes (name, start_level, basic_class, skill, description, min_damage, max_damage, image_path) VALUES (?,?,?,?,?,?,?,?)", lst)
        conn.commit()
        return lord_info(lst[0])
    except:
        return 'Неверно заполнены параметры!'

def class_info(name):

    # подкючаемся к базе
    conn = sqlite3.connect("content.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM classes WHERE name LIKE ?', [name])
    fresult = cursor.fetchone()

    if fresult[0] != 0:
        result = 'Тип: ' + name \
                 + '\n-------------------------------' \
                 + '\n🎆 Доступен на уровне: ' + fresult[1] \
                 + '\n👑 Основной класс: ' + fresult[2]  \
                 + '\n🎓 Навык: ' + fresult[3] \
                 + '\n📜 Описание: ' + fresult[4]

    return result

def add_travel_message(texts):

    # подкючаемся к базе
    conn = sqlite3.connect("content.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    lst = texts.split("/")

    try:
        cursor.execute("INSERT INTO event_texts (text, event_type, image_path) VALUES (?,?,?)", lst)
        conn.commit()
        return lord_info(lst[0])
    except:
        return 'Неверно заполнены параметры!'