'''
Как известно, во время итерации по словарю мы получаем ключи, а не значения или пары ключ-значение.

Приведенный ниже код:

info = {'name': 'Timur', 'age': 29, 'gender': 'Male'}

print(*info)
выводит:

name age gender
Реализуйте класс DictItemsIterator, порождающий итераторы, конструктор которого принимает один аргумент:

data — словарь
Итератор класса DictItemsIterator должен генерировать последовательность кортежей, 
представляющих собой пары ключ-значение словаря data, а затем возбуждать исключение StopIteration.
'''

class DictItemsIterator:

    def __init__(self, data):
        self.data = data
        self.dict_keys = [*self.data]
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data) - 1:
            self.index += 1
            return (self.dict_keys[self.index], self.data[self.dict_keys[self.index]])
        else:
            raise StopIteration
    

data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

pairs = DictItemsIterator(data)

print(*pairs)