import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
# # date = 'date_req=02/03/2002'
today = datetime.today()
today = today.strftime('%d/%m/%Y')
payload = {'date_req' : today}
response = requests.get(url, params=payload)
xml = BeautifulSoup(response.content, 'lxml')

def getCourse(id):
    return xml.find('valute', {'id': id}).value.text
#
# print(getCourse('R01235'), 'рублей за 1 доллар')
# print(getCourse('R01239'), 'рублей за 1 евро')
# print(getCourse('R01215'), 'рублей за 1 крону')
# print(getCourse('R01335'), 'рублей за 1 тенге')


# my_file = open('file.txt', 'w')
# my_file.write('I am a student')
# my_file.close()
#
# my_file = open('file.txt', 'r')
# my_text = my_file.read()
# print(my_text)
# my_file.close()


valute_from = 'EUR'
valute_to = 'USD'
amount = int(input('Введите сколько валюты нужно конвентировать: '))

def course(valute_from, valute_to, amount):
    valutes = {
        'RUR': 1.0,
        'USD': 74.7588,
        'EUR': 79.6104,
    }
    if valute_from == 'RUR':
        return amount / valutes[valute_to]
    else:
        return amount / valutes[valute_from] * valutes[valute_to]

print('Результат:', course(valute_from, valute_to, amount))




