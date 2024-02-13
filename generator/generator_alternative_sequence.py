'''
Реализуйте генераторную функцию alternating_sequence(), которая принимает один аргумент:

count — натуральное число, по умолчанию имеет значение None
Если count имеет значение None, функция должна возвращать генератор, 
порождающий бесконечный знакочередующийся ряд натуральных чисел.

Если count имеет в качестве значения натуральное число, 
функция должна возвращать генератор, порождающий первые count чисел знакочередующегося ряда
натуральных чисел, а затем возбуждающий исключение StopIteration.
'''


def alternating_sequence(count=None):
    plus = 1
    number = 1
    if count != None:
        for num in range(1, count + 1):
            if plus % 2 == 0:
                plus += 1
                yield num * -1 
            else:
                plus += 1
                yield num * 1
    else:
        if plus % 2 == 0:
            plus += 1
            yield number * -1
            number += 1
        else:
            plus += 1
            yield number
            number += 1

generator = alternating_sequence()

print(next(generator))
print(next(generator))

