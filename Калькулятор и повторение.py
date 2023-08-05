# first_var = 22  #тип данных int
# second_var = 3.14  #тип данных float

# print(first_var + second_var)
# print(first_var - second_var)
# print(first_var / second_var)
# print(first_var * second_var)
#
# print(type(second_var))

# third_var = 'Привет, мир' #Тип данных str
# # print(third_var)
# sub_string_hello = third_var[0:6]
# sub_string_word = third_var[8:11]
# print('M' + sub_string_word[1:] + '','' + 'п' + sub_string_hello[1:])


# try / expect
# try:
#     input_var_1 = int(input('Введите число 1'))
#     input_var_2 = int(input('Введите число 2'))
# except ValueError:
#     print('Вы ввели неверное значение')
# else:
#     result = input_var_1 + input_var_2
#     print(result)
#
#     if input_var_1 == input_var_2:
#         print('Числа равны')
# finally:
#     print('Неужели ты не видишь, что ты вводишь!!!')

# списки повторение
# home_list = ['Кухня', 'Ванная', "Гостинная", "Спальня", 'Комната']
# print(home_list)
# home_list[4] = 'детская'
# print(home_list)

# повторение функции
# for i in range (2, 7, 2 ):
#     print(i)


# def add(x, y):
#     return x + y
#
# x = int(input())
# y = int(input())
# print(add(x, y))


# def hello():
#     name = input('Как вас зовут ? ')
#     print('Приятно познакомиться', name)
#     hello()
# hello()


#Calculator v.xD

# def calculate():
#     print('Укажите интересующую вас операцию')
#     print('+ - сложение')
#     print('- - вычитание')
#     print('/ - деление')
#     print('* - умножение')
#
#     operation = input()
#
#     if operation == '+':
#         num1 = int(input())
#         num2 = int(input())
#         try:
#             res = num1 + num2
#         except ValueError:
#             print('Неверные значения')
#         else:
#             print(res)
#     if operation == '-':
#         num1 = int(input())
#         num2 = int(input())
#         try:
#             res = num1 - num2
#         except ValueError:
#              print('Неверные значения')
#         else:
#              print(res)
#     if operation == '*':
#         num1 = int(input())
#         num2 = int(input())
#         try:
#             res = num1 * num2
#         except ValueError:
#             print('Неверные значения')
#         else:
#             print(res)
#     if operation == '/':
#         num1 = int(input())
#         num2 = int(input())
#         try:
#             res = num1 / num2
#         except ValueError:
#             print('Неверные значения')
#         else:
#             print(res)
#     else:
#         print('Операция не найдена!')
#     print(' ')
#     calculate()
#
# calculate()

import math


# print("Введите коэффициенты для уравнения")
# print("ax^2 + bx + c = 0:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
#
# discr = b ** 2 - 4 * a * c
# print("Дискриминант D = %.2f" % discr)



















