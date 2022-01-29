import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from tokens import bot_token

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

token = bot_token.VK_TOKEN

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:

            request = event.text

            if request == ''

