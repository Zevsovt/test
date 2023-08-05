# class Item:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     def __add__(self, other):
#         if isinstance(other, Item):
#             return self.price + other.price
#
#         elif isinstance(other, int):
#             return self.price + other
#
#     def __sub__(self, other):
#         if isinstance(other, Item):
#             return self.price - other.price
#
#         elif isinstance(other, int):
#             return self.price - other
#
#     def __mul__(self, other):
#         if isinstance(other, Item):
#             return self.weight * other.weight
#
#         elif isinstance(other, float):
#             return self.weight * other
#
#     def __truediv__(self, other):
#         if isinstance(other, Item):
#             return self.weight / other.weight
#
#         elif isinstance(other, float):
#             return self.weight / other
#
#
# item_1 = Item('Видеокарта', 15_000, 0.8)
# item_2 = Item('Процессор', 12_000, 0.3)
#
# total_price = item_1 + 1000
# total_price_2 = item_2 - 5000
# total_weight = item_1 * 0.3
# total_weight_2 = item_2 / 0.5
#
#
# print(total_price)
# print(total_price_2)
# print(total_weight)
# print(total_weight_2)





############################################################




from tkinter import *
from random import randint

window = Tk()
window.geometry('600x600')

class Clay:
    image = PhotoImage(file=r'elements/free-icon-pottery-7942410.png').subsample(4, 4)

class Dust:
    image = PhotoImage(file=r'elements/free-icon-dust-2396941.png').subsample(4, 4)

class Aroma:
    image = PhotoImage(file=r'elements/aroma.png').subsample(4, 4)

class Fire:
    image = PhotoImage(file=r'elements/free-icon-fire-9509865.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay
        elif isinstance(other, Water):
            return Aroma

class Water:
    image = PhotoImage(file=r'elements/free-icon-water-drop-4246703.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Aroma


class Wind:
    image = PhotoImage(file=r'elements/wind.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Dust

class Earth:
    image = PhotoImage(file=r'elements/ground.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay

        elif isinstance(other, Wind):
            return Dust


canvas = Canvas(window, width=600, height=600)
canvas.pack()

elements = [Earth(), Fire(), Water(), Wind()]

for elem in elements:
    canvas.create_image(randint(50, 550), randint(50, 550), image=elem.image)

def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)

    if len(images_id) == 2:
        elem_id_1, elem_id_2 = images_id[0], images_id[1]
        element_1 = elements[elem_id_1 - 1]
        element_2 = elements[elem_id_2 - 1]

        new_element = element_1 + element_2
        if new_element:
            if new_element not in elements:
                canvas.create_image(event.x, event.y, image=new_element.image)
                elements.append(new_element)


    canvas.coords(images_id, event.x, event.y)

window.bind('<B1-Motion>', move)

window.mainloop()