"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
def print_false():
    print("Не верно")

def year_input():
    year = input('Введите год рождения А.С.Пушкина: ')
    return year

def date_input():
    date = input('В какой день июня родился А.С.Пушкин: ')
    return date

def check(comparable, input_function):
    result = input_function()
    while result != comparable:
        print_false()
        result = input_function()

check('1799', year_input)
check('6', date_input)

print('Верно')