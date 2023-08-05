# from tkinter import  *
# window = Tk()
# window.geometry('900x300')
# window.title('Dangerous')
# window.config(bg='black')
#
# window.resizable(width=False, height=False)
# text = Label(text='Ваш компьютер заражен!!!', fg='green',
#              bg='black', font=('Courier New', 34))
# text.place(x=100, y=100, width=700, height=100)
# count_text = Label(text="6", fg='green', bg='black',
#                    font=('Courier New', 38))
#
# def count_start():
#     if int(count_text['text']) > 0:
#         count_text['text'] = int(count_text['text']) - 1
#         count_text.place(x=250, y=25, width=400, height=100)
#         window.after(1000, on_close)
#     else:
#         count_text['text'] = 0
#         width = window.winfo_screenwidth()
#         height = window.winfo_screenwidth()
#         window.geometry(str(width)+'x'+str(height))
#         photo = PhotoImage(file='68tz.gif')
#         label = Label(image=photo, bg='black')
#         label.image = photo
#         label.place(width=width, height=height, x=0, y=0)
#
# def on_close():
#     count_start()
#
# window.protocol("WM_DELETE_WINDOW", on_close)
#
# window.mainloop()

# Скачать pyinstaller
# Заходим в терминал и прописываем команду:
# pyinstaller -F -i "icon.png" virus.py

#----------------------------------------------------------------------------------------------

# Лотерея
# from tkinter import *
#
# window = Tk()
# window.geometry('700x600')
# window.title('Лотерея')
#
# window.resizable(width=False, height=False)
#
# def click_button():
#     text.config(text = 'Чтобы забрать выйгрыш необходимо внести 1000 руб', font=('Arial', 18))
#     b.destroy()
#
#
# text = Label(text='ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!', fg='red', bg='black', font=('Courier New', 25))
# text.place(x=20, y=50, width=700, height=100)
#
# b = Button(text='ПОЛУЧИТЬ ВЫЙГРЫШ!', font=('Arial', 18), fg='black', command=click_button)
# b.place(x=200, y=200,)
#
# def on_close():
#     pass
#
# window.protocol("WM_DELETE_WINDOW", on_close)
#
# window.mainloop()

#----------------------------------------------------------------------------------


#Собачьи бега

# n = int(input())
# dogs_list = list()
# for i in range(n):
#     dogs_list.append(int(input()))
#     print(dogs_list)
#     min_dogs = min(dogs_list)
#     mi = dogs_list.index(min_dogs)
#     max_dogs = max(dogs_list)
#     ma = dogs_list.index(max_dogs)
#     dogs_list[mi] = ma
#     dogs_list[ma] = mi
#     print(dogs_list)

#-----------------------------------------------------------------------------------------------------



