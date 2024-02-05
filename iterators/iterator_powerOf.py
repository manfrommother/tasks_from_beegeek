'''
Реализуйте класс PowerOf, порождающий итераторы, конструктор которого принимает один аргумент:

number — ненулевое число
Итератор класса PowerOf должен генерировать бесконечную последовательность целых неотрицательных степеней 
числа number в порядке возрастания, начиная с нулевой степени.
'''

class PowerOf:

    def __init__(self, number):
        self.number = number
        self.degree = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.degree += 1
        return self.number ** self.degree
