import sqlite3



def parse_to_base(file):

    conn = sqlite3.connect("qa_base.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    file = open(file)
    for line in file.readlines():
        pair = line.split("|")
        if len(pair) < 2:
            print(line + " не является парой вопрос-ответ")
            continue

        question = pair[0]
        answer = pair[1]
        if len(answer.split()) > 1:
            print(answer + " - ответ из более чем одного слова будет пропущен!")
            continue

        answer = answer.rstrip()
        strlen = len(answer)

        if strlen < 5:
            smbl = "ы"
        else:
            smbl = ""
        question = question[:-1] + "?"
        question = question  + " (" + str(strlen) + " букв" + smbl +  ")"


        cursor.execute("INSERT INTO qa_pairs (question, answer) VALUES (?,?)", (question, answer.lower()))
        conn.commit()



parse_to_base('victorina3.txt')