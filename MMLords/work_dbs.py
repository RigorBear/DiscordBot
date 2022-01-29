import sqlite3


def add_lord(texts):

    # подкючаемся к базе
    conn = sqlite3.connect("MMLords/lords.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    lst = texts.split("/")

    try:
        cursor.execute("INSERT INTO lords (type, basic_hp, basic_mp, skill, description, image_path) VALUES (?,?,?,?,?,?)", lst)
        conn.commit()
        return lord_info(lst[0])
    except:
        return 'Неверно заполнены параметры!'

def lord_info(type):

    # подкючаемся к базе
    conn = sqlite3.connect("MMLords/lords.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM lords WHERE type LIKE ?', [type])
    fresult = cursor.fetchone()

    if fresult[0] != 0:
        result = 'Тип: ' + type \
                 + '\n-------------------------------' \
                 + '\n❤ Базовое здоровье: ' + fresult[1] \
                 + '\n🔮 Базовая мана: ' + fresult[2]  \
                 + '\n🎓 Навык: ' + fresult[3] \
                 + '\n📜 Описание: ' + fresult[4]




