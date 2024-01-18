'''
Реализуйте функцию triangle() с использованием рекурсии, которая принимает один аргумент:

h — натуральное число
Функция должна выводить звездный треугольник с высотой h в соответствии со следующим примером:

...
*****
****
***
**
*
'''

def triangle(h):
    if h > 0:
        print('*' * h)
        triangle(h - 1)

triangle(5)