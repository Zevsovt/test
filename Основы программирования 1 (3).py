# salary = int(input('Введите з/п сотрудника: '))
# name = input('Как вас зовут ?')
#
# # print('y' + name + ' зарплата в год составляет' + salary * 12 + 'руб')
#
# print(f'y {name} зарплата в год составляет {salary * 12} руб')



# emoloyee = {'name': 'Данил',
#             'salary': 200_000_000}
#
# print(f'y {emoloyee["name"]} зарплата в год составляет {emoloyee["salary"] * 12} руб.')
# print(f'y {emoloyee.get("name")} зарплата в год составляет {emoloyee.get("salary") * 12} руб.')


# employee_list = [
# #     {
# #         "name": 'Артем',
# #         'salary': 400_000
# #     },
# #     {
# #         'name': 'Анна',
# #         'salary': 650_000
# #     },
# #     {
# #         'name': 'Олег',
# #         'salary': 1_000_000
# #     }
# # ]
# #
# # for employee in employee_list:
# #     print(f'Имя: {employee["name"]}, зарплата: {employee["salary"]}')
# #
# # for employee in employee_list:
# #     if employee["name"] == 'Олег':
# #         employee_list.remove(employee)
# #         break
# #
# # for employee in employee_list:
# #     print(f'Имя: {employee["name"]}, зарплата: {employee["salary"]}')
# #
# # new_employee = {
# #     'name': 'Ролан',
# #     'salary': 100_000
# # }
# #
# # employee_list.append(new_employee)
# # for employee in employee_list:
# #     print(f'Имя: {employee["name"]}, зарплата: {employee["salary"]}')
# #
# # print(len(employee_list))


# class Employee:
#     def __init__(self, name, salary, on_vacation):
#         self.name = name
#         self.salary = salary
#         self.on_vacation = on_vacation
#         self.on_work = True
#
# employees = [
#     Employee('Данил', 20_000, False),
#     Employee('Олег', 25_000, False),
#     Employee('Катя', 59_000, False),
#     Employee('Никита', 5_000, False)
# ]
#
#
# for employee in employees:
#     if employee.name == 'Катя':
#         employee.on_work = False
#     print(f'Имя: {employee.name}, зарплата: {employee.salary}'
#           f' Отпуск: {employee.on_vacation}, STATUS WORK: {employee.on_work}')


class Employee:
    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.on_work = True
        self.is_good_employee = is_good_employee

employees = [
    Employee('Иван', 35_000, False, True),
    Employee('Олег', 38_000, False, True),
    Employee('Михаил', 45_000, False, True),
    Employee('Вадим', 31_000, False, False),
    Employee('Максим', 27_000, False, True)
]

for employee in employees:
    if employee.is_good_employee == False:
        employee.on_work = False
    print(f'Имя: {employee.name}, зарплата: {employee.salary}'
          f'Отпуск: {employee.on_vacation}, статус работы: {employee.on_work}')





