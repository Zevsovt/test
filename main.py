from vk_bot import *
from course import *


token = 'vk1.a.uiH5OICkMie9RXqW4mjdm7j_YrZ8fHWLr6Usp8cKpR25LtdyaqvuFExaDDeknJ1nvWIyrbOjCXvqBNXIy8wBW0WbMAxyO90m2mL0gYrnEZkKCWKrszJVM4rBPbX2uHIONqpJQYHleN2_ufPS5tNV8q2Yy3Sc-iCBDchD4gqRQdlgF4Uc32huzz4486vJKzx6gNrHAflplPGQslDk1OB7yQ'


vk = vk_api.VkApi(token=token)

vk._auth_token()

messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})

print(messages['items'][0]['last_message']['from_id'])
print(messages['items'][0]['last_message']['text'])
print(messages['items'][0]['last_message']['id'])


def get_largest_planet():
    api_url = "https://swapi.dev/api/planets"
    response = requests.get(api_url)
    data = response.json()
    largest = data["results"][0]
    for planet in data["results"]:
        if int(planet["diameter"]) > int(largest["diameter"]):
            largest = planet
    return largest["name"]


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        random_id = random.randint(1, 9999999)
        if msg == "планеты":
            response = f'Самая большая планета - {get_largest_planet()}'
        else:
            response = "Неизвестная команда. Вот что я умею: планеты: выдать планету с максимальным диаметром"
        vk.messages.send(peer_id=user_id, random_id=random_id, message=response)

def get_largest_ship():
    api_url = "https://swapi.dev/api/planets"
    response = requests.get(api_url)
    data = response.json()
    max = data["results"][0]
    for ship in data["results"]:
        if int(ship["max_atmosphering_speed"]) > int(max["max_atmosphering_speed"]):
            max = ship

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        random_id = random.randint(1, 9999999)
        if msg == "корабли":
            response = f'Самый быстрый корабль - {get_largest_ship()}'
        else:
            response = "Неизвестная команда. Вот что я умею: корабли: выдать корабль с максимальной скоростью"
        vk.messages.send(peer_id=user_id, random_id=random_id, message=response)



while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    if messages['count'] >= 1:
        print(messages)
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']
        message_text = messages['items'][0]['last_message']['text']
        if message_text.lower() == 'курс':
            vk.method( 'messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': getCourse('R01235')})
        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'неизвестная команда'})

        if message_text.lower() == 'планеты':
            vk.method( 'messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': get_largest_planet})
        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'неизвестная команда'})

        if message_text.lower() == 'корабли':
            vk.method( 'messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': get_largest_ship})
        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'неизвестная команда'})










