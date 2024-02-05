'''
Реализуйте функцию random_numbers(), которая принимает два аргумента:

left — целое число
right — целое число
Функция должна возвращать итератор, 
генерирующий бесконечную последовательность случайных целых чисел 
в диапазоне от left до right включительно.
'''

from random import randint

def random_numbers(left, right):
    return iter(lambda: randint(left, right), -1)

iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))