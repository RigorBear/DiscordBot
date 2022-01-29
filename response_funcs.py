from random import choice
from random import randint
from database import markov_chains

import config
import weather
import bvid
import ozstat
import press_f
import maestro
import deep_img

def bot_info():
    answer = "Привет! Я СукаБот. Могу рассказать какая сейчас \
                погода в интересующем вас городе. Если спросите меня Кто, я вам отвечу. Ещё ты можешь\
                попросить у меня рандомное видео с youtube.Больше я нихуя не умею."

    result = [answer, None]

    return result

def get_weather(mess):
    city = mess.replace("Погода ", "")
    w_st = weather.weather_status(city)

    result = [w_st, None]

    return result

def who_is(mess):
    phrase = mess.replace("Кто ", "")
    phrase = phrase.replace("?", "")
    user = choice(message.channel.guild.members)
    start_phrase = ['', 'Конечно же, ', 'Несомненно, ', 'Сто пудов, ', 'Невероятно, но ', 'Да, ']
    phrase = choice(start_phrase) + user.mention + " " + phrase

    result = [phrase, None]

    return result

def youtube_search(mess):
    search_word = mess.replace("Сука ютуб ", "")
    id_yt = bvid.youtube_search(search_word)

    result = [id_yt, None]

    return result

def lna_status(mess):
    nick = mess.replace("Жиза ", "")
    lna_stat = ozstat.LNA(nick)

    result = [lna_stat, None]

    return result

def mc_answer(mess):
    pon_phr = mess.replace("Понас ", "")
    phr = markov_chains.create_phrase(pon_phr)

    result = [phr, None]

    return result

def press_f():
    file = press_f.rand_pic_f()

    result = ["", file]

    return result

def maestro_pic(mess):
    maes = mess.replace("Маэстро ", "")
    file = maestro.put_text_pil(maes)

    result = ["", file]

    return result

def deep_ai_pic(mess):

    deep_mess = mess.replace("Deep ", "")
    deep_img.create_img(deep_mess)
    file = discord.File('deep_img/dimg.jpg', filename='deep_img/dimg.jpg')

    result = ["", file]

    return result


