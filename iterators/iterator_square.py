'''
Реализуйте класс Square, порождающий итераторы, конструктор которого принимает один аргумент:

n — натуральное число,
Итератор класса Square должен генерировать последовательность из n чисел,
каждое из которых является квадратом очередного натурального числа, 
а затем возбуждать исключение StopIteration.
'''

class Square:

    def __init__(self, numb):
        self.numb = numb
        self.counter = 0
        self.n = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter != self.numb:
            self.counter += 1
            return self.counter ** 2
        else:
            raise StopIteration
        

squares = Square(10)

print(list(squares))
        
