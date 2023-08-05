# pprint - pretty print
from pprint import pprint
from typing import Iterator
#
#
# goods = [
#     {
#         "name": 'Iphone 14',
#         'brand': 'Apple',
#         'price': 1200
#     },
#     {
#         'name': 'Samsung Galaxy A53',
#         'brand': 'Samsung',
#         'price': 500
#     },
#     {
#         'name': 'Xiaomi Mi 8',
#         'brand': 'Xiaomi',
#         'price': 300
#     }
# ]
#
#
#
# if __name__ == '__main__':
#
#     def item_price(item):
#         return item['price']
#
#
# pprint(sorted(goods, key=lambda item: item['price']))
#
# apple_list = list(filter(lambda item: item['brand'] == 'Apple', goods))
# pprint(apple_list)
#
# numbers_list = ['1', '2', '3', '4', '5']
# numbers_list = list(map(int, numbers_list))
# print(numbers_list)
#
#
# names_list = ['Данил', 'Никита', 'Настя', 'Катя']
# surnames_list = ['Петров', 'Иванов', 'Даниловна', 'Никитовна']
#
# full_names_list = list(map(lambda name, surname: f'{name} {surname}',
#                       names_list, surnames_list))
# print(full_names_list)
#
#
# #enumerate
#
# # 'key': 'value'
#
# #range(len(goods))
#
#
# indexed_goods = []
#
# for i, item in enumerate(goods):
#     indexed_goods.append({i: item})
#
# pprint(indexed_goods)
#
# # Функция enumerate возвращает кортеж вида  (индекс, элемент)
#
#
#
#
# names_list = ['Данил', 'Никита', 'Настя', 'Катя']
# surnames_list = ['Петров', 'Иванов', 'Даниловна', 'Никитовна']
# patronimic_list = ['Данилович', 'Никитич', 'Ивановна', 'Даниловна']
#
# for name, surname, patronimic in zip(names_list, surnames_list, patronimic_list):
#     print(name, surname, patronimic)



# class Item:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
#
#     def __repr__(self):
#         return self.brand
#
# items_list = [
#     Item(1000, 'Apple'),
#     Item(1200, 'Apple'),
#     Item(900, 'Samsung'),
#     Item(700, 'Samsung'),
#     Item(660, 'Xiaomi'),
#
#
# ]
#
# samsung_list = list(filter(lambda item: item.brand == "Samsung", items_list))
# print(samsung_list)


names_list = ['данил', 'артём', 'никита', 'влад']
print([names.capitalize() for names in names_list])














