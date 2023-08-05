# import random
#
# import requests
# from bs4 import BeautifulSoup
#
#
# response = requests.get('https://i-fakt.ru')
# response = response.content
# html = BeautifulSoup(response, 'html.parser')
# fact = random.choice(html.find_all(class_='p-2 clearfix'))
# print(fact.a.attrs['href'])
#--------------------------------------------------------------

# import random
# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get('https://kudago.com/spb/festival')
# response = response.content
# html = BeautifulSoup(response, 'html.parser')
# fest = random.choice(html.find_all(class_='post-title'))
# print(fest.text)
# print(fest.a.attrs['href'])
#------------------------------------------------------------

# import random
# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get('https://kudago.com/spb/concerts/?date=2022-12-15')
# response = response.content
# html = BeautifulSoup(response, 'html.parser')
# concerts = random.choice(html.find_all(class_='post-title'))
# print(concerts.text)
# print(concerts.a.attrs['href'])

#------------------------------------------------------------------------------------












