'''
Класс Person
Вам доступен класс Person, описывающий человека. При создании экземпляра класс принимает два аргумента в следующем порядке:

name — имя человека
surname — фамилия человека
Экземпляр класса Person имеет два атрибута:

name — имя человека
surname — фамилия человека
Класс Person имеет одно свойство:

fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки:
<имя> <фамилия>
Реализуйте свойство fullname класса Person с помощью декоратора @property
'''

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'
    
    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()


