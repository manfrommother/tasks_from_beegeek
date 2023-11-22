'''
Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:

start — начальная дата, тип date
end — конечная дата, тип date
Функция должна возвращать количество суббот между датами start и end включительно.

Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется, что первая дата меньше второй.
'''
from datetime import date


def saturdays_between_two_dates(start, end):
    start, end = sorted((start, end))

    return len([date.fromordinal(day).weekday() for day in range(start.toordinal(), end.toordinal() + 1) if date.fromordinal(day).weekday() == 5])

date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))