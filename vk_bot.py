import random
import vk_api
from course import getCourse
from wiki import get_wiki_article
from vk_api.longpoll import VkLongPoll, VkEventType

TOKEN = 'vk1.a.uiH5OICkMie9RXqW4mjdm7j_YrZ8fHWLr6Usp8cKpR25LtdyaqvuFExaDDeknJ1nvWIyrbOjCXvqBNXIy8wBW0WbMAxyO90m2mL0gYrnEZkKCWKrszJVM4rBPbX2uHIONqpJQYHleN2_ufPS5tNV8q2Yy3Sc-iCBDchD4gqRQdlgF4Uc32huzz4486vJKzx6gNrHAflplPGQslDk1OB7yQ'

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id


    random_id = random.randint(1, 10 ** 10)

    if msg == '-к':
        response = '{0} рублей за 1 доллар\n{1} рублей за 1 евро\n' '{2} рублей за 10 юаней\n{3} рублей за 1 фунт'.format(
            getCourse('R01235'), #0
            getCourse('R01239'), #1
            getCourse('R01375'), #2
            getCourse('R01036') #3
        )
        vk.messages.send(user_id=user_id, random_id=random_id, message=response)


    elif msg.startswith('-в'):
        article = msg[2:]
        response = get_wiki_article(article)

    else:
        response = 'Неизвестная команда'

    vk.messages.send(user_id=user_id, random_id=random_id, message=response)
