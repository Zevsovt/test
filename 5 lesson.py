####### import time
#
#
# class RunningCodeJudge:
#     def __init__(self):
#         self.start = None
#
#     def __enter__(self):
#         self.start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         t = time.time() - self.start
#         print(f'Время работы кода: {t} сек.')
#
#         if exc_type is TypeError:
#             return True
#
# with RunningCodeJudge() as t1:
#     my_list = [x for x in range(1, 100_000_000)]
#     my_list -= 's'


####### my_list = [1, 2, 3, 4, 5]
# list_ittrator = iter(my_list)
# print(next(list_ittrator))
# print(next(list_ittrator))
# print(next(list_ittrator))
# print(next(list_ittrator))
# print(next(list_ittrator))
#
# for i in list_ittrator:
#     print(i)

######### import random
#
# class RandomIter:
#     def __init__(self, limit):
#         self.limit = limit
#         self.__reload = limit
#
#     def __iter__(self):
#         self.limit = self.__reload
#         return self
#
#     def __next__(self):
#         if self.limit == 0:
#             raise StopIteration
#
#         self.limit -= 1
#         return random.randint(0, 100)
#
#
# rand_iter = RandomIter(10)
# print(iter(rand_iter))


class MyFile:
    def __init__(self):