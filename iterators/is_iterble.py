'''
Реализуйте функцию is_iterable(), которая принимает один аргумент:

obj — произвольный объект
Функция должна возвращать True, 
если объект obj является итерируемым объектом, 
или False в противном случае.
'''

def is_iterable(obj):
    try:
        value = iter(obj)
        return True
    except:
        return False
    

print(is_iterable('18731'))