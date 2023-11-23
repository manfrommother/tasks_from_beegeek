'''
Реализуйте функцию is_correct(), которая принимает три аргумента в следующем порядке:

day — натуральное число, день
month — натуральное число, месяц
year — натуральное число, год
Функция должна возвращать True, если дата с компонентами day, month и year является корректной, 
или False в противном случае.
'''

from datetime import date


def is_correct(user_date):
    user_date = [int(i) for i in user_date.split('.')]
    user_date[0], user_date[2] = user_date[2], user_date[0]
    try:
        date(*user_date)
        return True
    except:
        return False

    

print(is_correct('29.02.2017'))