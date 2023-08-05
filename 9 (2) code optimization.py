# def func(a, b, *args, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
#
# func(1, 2, 5974, 'Привет', True, one=1, two=2)



# age = 18
#
# is_allow = True if age >= 18 else False
#
# print(is_allow)


#1
# val = None
# if val is None:
#     res = []
# else:
#     res = val

#2
# res = [] if val is None else val

#3
# res = val or res


# div_5_list = []
# for x in range(100):
#     if x % 5 == 0:
#         if x > 50:
#             div_5_list.append(x**3)
#         else:
#             div_5_list.append(x)
# print(div_5_list)

# div_5_list = [x**3 if x > 50 else x for x in range(100) if x % 5 == 0]
# print(div_5_list)


# a = {x:len(x) for x in ['orange', 'green', 'red', 'blue']}
# print(a)


# list = [x for x in range(250) if x % 30 == 0 and x % 31 == 0]
# print(list)


# a = (1, 2, 3)
# b = [1, 2, 3]
# print(a)



# some_dict = {
#     (1, 2, 3): 'Hello'
# }
#
# a = some_dict[(1, 2, 3)]
# print(a)

# some_tuple = (1, 2, 3)
# print(some_tuple, type(some_tuple))
# some_list = list(some_tuple)
# print(some_list, type(some_list))

# some_tuple = ([1, 2, 3], 'qwe')
# print(some_tuple)
# some_tuple[0].append(4)
# print(some_tuple)


a = (5, 3, 2, 1, 4)
b = tuple(sorted(a))
print(a)
print(b)








