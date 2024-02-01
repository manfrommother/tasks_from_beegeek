'''
Реализуйте декоратор prefix, который принимает два аргумента в следующем порядке:

string — произвольная строка
to_the_end — булево значение, по умолчанию равное False
Декоратор должен добавлять строку string к возвращаемому значению декорируемой функции. 
Если to_the_end имеет значение True, строка string добавляется в конец, если False — в начало.

Также декоратор должен сохранять имя и строку документации декорируемой функции.
'''


import functools

def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not to_the_end:
                return str(string) + func(*args, **kwargs)
            else:
                return func(*args, **kwargs) + str(string)
        return wrapper
    return decorator


@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'
       
print(get_bonus())

