'''
Реализуйте функцию is_iterator(), которая принимает один аргумент:

obj — произвольный объект
Функция должна возвращать True, 
если объект obj является итератором, или False в противном случае. 
'''


def is_iterator(obj):
    try:
        next(obj)
        return True
    except:
        return False
    

print(is_iterator([1, 2, 3, 4, 5]))