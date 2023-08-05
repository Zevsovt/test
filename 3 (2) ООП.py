# from tkinter import *
#
# window = Tk()
# window.geometry('800x600')
#
# canvas = Canvas(window, width=800, height=600, bg='white')
# canvas.pack()
#
# # canvas.create_rectangle(10, 180, 110, 270, fill='yellow', outline='green')
# # canvas.create_polygon(10, 180, 60, 120, 110, 180, fill='red', outline='black')
#
# class House:
#     def __init__(self, roof_color, wall_color):
#         self.roof_color = roof_color
#         self.wall_color = wall_color
#         self.height = 130
#         self.width = 140
#         self.roof = None
#         self.wall = None
#
#     def build_house(self, x, y):
#         h = self.height
#         w = self.width
#
#         self.roof = canvas.create_polygon(x, y, x+w, y, x + w/2, h-100, fill=self.roof_color)
#         self.wall = canvas.create_rectangle(x+20, y, x+120, y+100, fill=self.wall_color, outline='')
#
# house_1 = House('green', 'red')
# house_1.build_house(20, 50)
#
# house_2 = House('black', 'blue')
# house_2.build_house(180, 50)
#
# window.mainloop()



from tkinter import *
window = Tk()
window.geometry('800x600')
window.title('Рисовалка')

canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()

class Figure:
    def __init__(self, side_color, centre_color):
        self.side_color = side_color
        self.centre_color = centre_color
        self.centre = None
        self.side = None
    def build_figure(self):
        self.centre = canvas.create_rectangle(150, 320, 250, 410, fill=self.centre_color)
        self.side = canvas.create_polygon(150, 320, 200, 230, 250, 320, fill=self.side_color)
        self.side = canvas.create_polygon(150, 410, 150, 320, 75, 360, fill=self.side_color)
        self.side = canvas.create_polygon(250, 410, 250, 320, 330, 360, fill=self.side_color)
        self.side = canvas.create_polygon(150, 410, 200, 490, 250, 410, fill=self.side_color)

figure_1 = Figure('red', 'blue')
figure_1.build_figure()

window.mainloop()





# import random
#
# class Warrior():
#     def __init__(self, name, health):
#         self.health = health
#         self.name = name
#
#     def fight(self):
#         res = random.randint(1, 2)
#         if res == 1:
#             self.health -= 20
#         else:
#             print('не попал !')
#
# war_1 = Warrior('Воин 1', 100)
# war_2 = Warrior('Воин 2', 100)
#
# while True:
#     question = input(f'Какой воин атакует, {war_1.name} / 1 или {war_2.name} / 2 ? ')
#     if question == str(1):
#         print(f'{war_1.name} атакует {war_2.name} ')
#         war_2.fight()
#         print(f'У противника осталось здоровья - {war_2.health}\n')
#     elif question == str(2):
#         print(f'{war_2.name} аттакует {war_1.name}')
#         war_1.fight()
#         print(f'У противника осталось здоровья - {war_1.health}\n')
#
#     if war_1.health <= 0:
#         print(f'Игра окончена ! {war_2.name} победил')
#         break
#     elif war_2.health <= 0:
#         print(f'Игра окончена ! {war_1.name} победил')
#         break







