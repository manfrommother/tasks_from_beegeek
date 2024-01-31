'''
Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в декорируемую функцию, являются положительными целыми числами.

Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:

TypeError, если аргумент не является целым числом
ValueError, если аргумент является целым числом, но отрицательным или равным нулю
'''

def takes_positive(func):
    def inner(*args, **kwargs):
        for i in args:
            if i <= 0:
                raise ValueError
            elif not isinstance(i, int):
                raise TypeError
        for key in kwargs:
            print(kwargs[key])
            if kwargs[key] <= 0:
                raise ValueError
            elif not isinstance(kwargs[key], int):
                raise TypeError
        return func(*args, **kwargs)
            
    return inner

@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
    
try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
except Exception as err:
    print(type(err))
                
