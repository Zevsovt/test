# class Year:
#     def __init__(self, days, season):
#         self.__days = days
#         self.__season = season
#
#     @property
#     def days(self):
#         return self.__days
#
#     @days.setter
#     def days(self, days):
#         self.__days = days
#
#     @property
#     def season(self):
#         return self.__season
#
#     @season.setter
#     def season(self, season):
#         self.__season = season
#
# year = Year('365', 'Зима')
# print(year.season)
# print(year.days)
# year.days = 366
# year.season = 'Лето'
# print(year.season)
# print(year.days)

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age <= 0:
#             raise ValueError('Вы еще не родились')
#
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#
#
# person = Person('Иван', 40)
# print(person.name)
# print(person.age)
# person.name = 'Данил'
# person.age = 15
# print(person.name)
# print(person.age)
# del person.age
# del person.name




from pprint import pprint

# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         if value.strip() == '':
#             raise ValueError('name cannot be empty')
#         self._name = value
#
#     @name.deleter
#     def name(self):
#         del self._name
#
# pprint(Person.__dict__)
#
# person = Person('John')
# pprint(person.__dict__)
# del person.name






