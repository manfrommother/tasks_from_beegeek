'''
Реализуйте декоратор strip_range, который принимает три аргумента в следующем порядке:

start — неотрицательное целое число
end — неотрицательное целое число
char — одиночный символ, по умолчанию равный точке .
Декоратор должен изменять возвращаемое значение декорируемой функции, 
заменяя все символы в диапазоне индексов от start (включительно) 
до end (не включительно) на символ char.

Также декоратор должен сохранять имя и строку документации декорируемой функции.
'''

import functools

def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total = func(*args, **kwargs)
            total_str = ''
            try:
                for i in range(len(total)):
                    if i < start or i >= end:
                        total_str += total[i]
                    elif i >= start and i < end:
                        total_str += char
                return total_str
            except IndexError:
                for i in range(len(total)):
                    if i < start or i >= len(total) - 1:
                        total_str += total[i]
                    elif i >= start and i < len(total) - 1:
                        total_str += char
                return total_str
        return wrapper
    return decorator


                     
