import requests
import json

url = 'https://swapi.dev/api/starships/'

response = requests.get(url)
star_wars_data = response.json()

starships = star_wars_data.get('results')
#
# for i in range(1, 6):
#     speed = 0
#     max_speed = starships[i].get('max_atmosphering_speed')
#     name = starships[i].get('name')
#     print(f"{name}'s max speed is {max_speed}")


# people_api = response.get('people')
# planets_api = response.get('planets')
# starships_api = response.get('results')

# def check_people(url):
#     #Вывод 5 людей
#     for i in range(1, 6):
#         response = requests.get(f'{url}/{i}').json()
#         print(response)
#
# check_people(people_api)
#
# def check_planets(url):
#     #Вывод пяти планет
#     for i in range(1, 6):
#         response = requests.get(f'{url}/{i}').json()
#         print(response)
#
# check_planets(planets_api)












