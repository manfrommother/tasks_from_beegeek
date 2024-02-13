'''
Реализуйте класс Negator. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Negator должен иметь один статический метод:

neg() — метод, принимающий в качестве аргумента объект и возвращающий его противоположное значение. 
Если методу передается целое или вещественное число, он должен возвращать это число, взятое с противоположным знаком. 
Если методу в качестве аргумента передается булево значение, он должен возвращать булево значение, противоположное переданному. 
Если переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:
Аргумент переданного типа не поддерживается
'''
from functools import singledispatch


class Negator:

    @singledispatch
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _from_digit(data: int|float) -> int|float:
        return -data
    
    @neg.register(bool)
    @staticmethod
    def _from_bool(data):
        return not data
    

print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))


    