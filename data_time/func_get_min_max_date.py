'''
Условие довольно долгое, поэтому напишу его своим языком. Надо написать функцию,
в которую передается список, функция должна вернуть кортеж из минимальной и максимальной даты
'''
from datetime import date


def get_min_max_date(dates):

    if len(dates) == 0:
        return ()
    
    return min(dates), max(dates)