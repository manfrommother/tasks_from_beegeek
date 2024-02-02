'''
Реализуйте декоратор returns, который принимает один аргумент:

datatype — тип данных
Декоратор должен проверять, что возвращаемое значение 
декорируемой функции принадлежит типу datatype. 
Если возвращаемое значение принадлежит какому-либо другому типу,
декоратор должен возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации 
декорируемой функции.
'''

import functools

def returns(datatype):
    def decorator(func):
        @ functools.wraps(func)
        def wrapper(*args, **kwargs):
            guess_data = func(*args, **kwargs)
            if isinstance(guess_data, datatype):
                return guess_data
            else:
                raise TypeError
        return wrapper
    return decorator

@returns(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]
print(append_this.__name__)
print(append_this.__doc__)
print(append_this([1, 2, 3], elem=4))