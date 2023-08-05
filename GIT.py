# посчитать кол-во отдельных символов
# aabb a - 2, b - 2

#  N ** 2


from time import time

# def stringcounter(data):
#     start = time()
#     for sym in data:
#         count = 0
#         for sym_2 in data:
#             if sym == sym_2:
#                 count += 1
#         print(sym, count)
#     print(time() - start)
#
# stringcounter('abcd')

# N * N

# def stringcounter(data):
#     start = time()
#
#     for sym in set(data): # let(set(data)) - N
#         count = 0
#         for sym_2 in data:  # len(data) - M
#             if sym == sym_2:
#                 count += 1
#         print(sym, count)
#     print( time() - start)
#
# stringcounter('abcdaaadadadabc')


# set - множество, тип данных в котором только уникальные значения, неуподрядорченные

# f = set()
# f = {1, 1, 2, 3}
# print(f)





# N

# def stringcounter(data):
#     start = time()
#     sym_count = {} # dict
#     for sym in data:
#         sym_count[sym] = sym_count.get(sym, 0) + 1
#
#      for s,c in sym_count.itmes():
#
#         print(s, c)
#
#     print( time() - start )
#
# stringcounter('abcddadavevbevsdadwewd')




