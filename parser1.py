import random
import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType



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
