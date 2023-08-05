
# class Singleton(object):
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls)
#             return cls.instance
#
# s = Singleton()
# print('Object created', s, id(s))
# s1 = Singleton()
# print('Object created', s1, id(s1))


# def repair_deco(func): #тут постоянно аргумент это func
#     def wrapper(a, b): #Тут аргументы которые получает наша функция
#         return func(a, b) - 1
#     return wrapper
#
# @repair_deco
# def wrong_func(a, b):
#     return a + b + 1
#
# print(f'2+2 = {wrong_func(2, 2)}')
# print(f'5+5 = {wrong_func(5, 5)}')

from datetime import datetime

def timeit(func):
    def wrapper(val):
        start = datetime.now()
        res = func(val)
        end = datetime.now()
        print(f'time: {end - start}')
        return res
    return wrapper


@timeit
def get_list1(val):
    return [x for x in range(val) if x % 2]

@timeit
def get_list_2(val):
    new_list = []
    for x in range(val):
        if x % 2:
            new_list.append(x)
    return new_list

val = 1000000
a = get_list1(val)
b = get_list_2(val)





