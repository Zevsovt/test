from datetime import datetime
import requests
from bs4 import BeautifulSoup
from tkinter import *



# root = Tk()
# root.geometry('500x500+200+200')
# root.title('Банк')
# count = 0
#
# def changeLabel():
#     global count
#     count += 1
#     lab['text'] = count
#
#
# lab = Label(root, text='Текст', bg='#FF6666', fg='gold', font='16')
# lab.place(x=100, y=100)
#
# btn = Button(text="Кнопка", background='#555', foreground='#ccc', font='16', command=changeLabel)
# btn.place(x=200, y=200)
#
# root.mainloop()


###### gw start


window = Tk()
window.geometry('400x350+300+300')
window.title('Курс валют')
window.resizable(width=False, height=False)

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'

today = datetime.today()
today = today.strftime('%d/%m/%Y')
payload = {'date_req' : today}

response = requests.get(url, params=payload)
xml = BeautifulSoup(response.content, 'lxml')

def getCourse(id):
    return xml.find('valute', {'id': id}).value.text

img_logo = PhotoImage(file='logo.png')
logo = Label(window, image=img_logo)
logo.place(x=0, y=0)

lab = Label(window, text='Курс валют \n MAXIMUM Банк', fg='orange', font='Arial 22', bg='black')
lab.place(y=25, x=150)

course_info = Label(window, text='Курс на: ' + today.replace('/', '.'),
                    font='Arial 18', bg='yellow')
course_info.place(y=150, x=90)

usd_course = Label(window, text='$' + getCourse('R01235'), font='Ariel 16', fg='green')
usd_course.place(y=190, x=100)

eur_course = Label(window, text='€' + getCourse('R01239'), font='Ariel 16', fg='green')
eur_course.place(y=230, x=100)

cny_course = Label(window, text='¥' + getCourse('R01375'), font='Ariel 16', fg='green')
cny_course.place(y=270, x=100)


window.mainloop()






# today = datetime.today()
# today = today
#
# payload = {'date_req': today}
#
# response = requests.get(url, params=payload)
#
# xml = BeautifulSoup(response.content, 'lxml')
#
# def getCourse(id):
#     return xml.find('valute', {'id': id}).value.text
#
# img_logo = PhotoImage(file='logo.png')
# logo = Label(window, image=img_logo)
# logo.place(x=0, y=0)
#
# lab = Label(window, text='Курс валют \n MAXIMUM Банк', fg='black',
#             font='Arial 22')
# lab.place(y=25, x=150)
#
# course_info = Label(window, text='Курс на:' + today.replace('/', '.'),
#                     font='Arial 18')
# course_info.place(y=150, x=90)
#
# usd_course = Label(window, text='$' + getCourse('R01235'), font='Ariel 16')
# usd_course.place(y=190, x=100)
#
# eur_course = Label(window, text='€' + getCourse('R01239'), font='Ariel 16')
# eur_course.place(y=230, x=100)


