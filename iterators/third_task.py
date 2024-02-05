'''
Дополните приведенный ниже код, ч
тобы в переменной infinite_love содержался итератор, 
бесконечно генерирующий единственное значение 
строку i love beegeek!.
'''

infinite_love = iter(lambda:'ent', False)

print(next(infinite_love))
print(next(infinite_love))
print(next(infinite_love))