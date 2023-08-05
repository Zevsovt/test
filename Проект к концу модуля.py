from tkinter import *
import random
import requests
from bs4 import BeautifulSoup
from icrawler.builtin import GoogleImageCrawler

window = Tk()
window.geometry('1000x700')
window.title('Самая полезная программа в мире')

label_title = Label(text='Выбери одну из кнопок', font=('Arial', 24), fg='yellow', bg='black')
label_title.place(width=1000, height=65, x=0, y=0)

def Kinopoisk():
    response = requests.get('https://www.film.ru/compilation/100-velichayshih-filmov-po-versii-chitateley-empire')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    kino = random.choice(html.find_all(class_="film_list"))
    print(kino.text)
    print(kino.a.attrs['href'])


def Capibara():
    #пользователю необходимо указать путь сохранения фотографий
    google_crawler = GoogleImageCrawler(storage={'root_dir': 'C:/Users/zevso/OneDrive/Desktop/123'})

    print('Сколько фотографий капибар вам нужно?')
    quantity = int(input())

    print('Напишите КАПИБАРА для проверки что вы не робот')
    name = str(input())

    google_crawler.crawl(keyword=name, max_num=quantity)


b1 = Button(text='Рандомный фильм', font=('Arial', 17), fg='yellow', bg='black', command=Kinopoisk)
b1.place(x=140,y=210)

b2= Button(text='Фотография прекрасной капибары', font=('Arial', 17), fg='yellow', bg='black', command=Capibara)
b2.place(x=550,y=210)

window.mainloop()





