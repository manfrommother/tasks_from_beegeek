'''

Тимур считает дату «интересной», если её год совпадает с годом его рождения, 
а сумма номера месяца и номера дня равна его возрасту. Год рождения Тимура — 1992 возраст — 29 лет.

Реализуйте функцию print_good_dates(), которая принимает один аргумент:

dates — список дат (тип date)
Функция должна выводить «интересные» даты в порядке возрастания,
 каждую на отдельной строке, 
 в формате  month_name DD, YYYY, где month_name — полное название месяца на английском. 

'''
from datetime import date


def print_good_dates(date_list):
    total_date_list = []

    for i in date_list:
        if i.year == 1992 and i.month + i.day == 29:
            total_date_list.append(i)
    
    for i in sorted(total_date_list):
        print(*i.strftime('%B %d, %Y'), end='\n', sep='')


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)


#более короткое решение:

'''
def print_good_dates(dates):
    for d in sorted(filter(lambda d: d.year == 1992 and d.month + d.day == 29, dates)):
        print(d.strftime('%B %d, %Y'))
'''
