import numpy as np
from PIL import Image, ImageDraw, ImageFont
import discord
import textwrap
import requests
from io import BytesIO

# создадим белое изображение
# или можно считать изобрежние с помощью cv2.imread("path_to_file")

# для простоты и совместимости возьмем пустое изображение из первого примера
# Чтобы не использовать opencv, а только PIL используйте функцию Image.open()
def put_text_pil(txt: str):
    try:
        print(txt[0])
        mnum = int(txt[0])

    except Exception:
        return False
    if mnum < 1:
        return False
    if mnum > 10:
        return False
    txt = txt[2:]


    font_size = 40
    font = ImageFont.truetype('impact.ttf', size=30)

    imag = Image.open('maestro_pics/maestro'+str(mnum)+'.png')


    # здесь узнаем размеры сгенерированного блока текста

    y_pos = 300
    draw = ImageDraw.Draw(imag)
    w, h = draw.textsize(txt, font=font)

    # теперь можно центрировать текст
    for line in textwrap.wrap(txt, width=20):
        w, h = draw.textsize(line, font=font)
        draw.text((int((imag.size[1] - w)/2), y_pos), line, fill='white', font=font, spacing = 4, align = 'center',
        stroke_width=4, stroke_fill='black')
        y_pos += font.getsize(line)[1]

    imag.save('temp/img001.png')
    file = discord.File('temp/img001.png', filename='temp/img001.png')

    return file

def get_mem(url_pic, phrase):

    txt = phrase

    response = requests.get(url_pic)
    imag = Image.open(BytesIO(response.content))
    font_size = imag.size[0] // 20
    font = ImageFont.truetype('impact.ttf', size=font_size)
    # здесь узнаем размеры сгенерированного блока текста


    draw = ImageDraw.Draw(imag)

    text_w = textwrap.wrap(txt, width=(imag.size[0]*0.05))
    y_pos = imag.size[1] * 0.9 - len(text_w)*font_size

    # теперь можно центрировать текст
    for line in text_w:
        w, h = draw.textsize(line, font=font)
        draw.text(((imag.size[0] - w)/2, y_pos), line, fill='white', font=font, spacing = 4, align = 'center',
        stroke_width=4, stroke_fill='black')
        y_pos += font.getsize(line)[1]

    imag.save('temp/mem.png')
    file = discord.File('temp/mem.png', filename='temp/mem.png')

    return file
