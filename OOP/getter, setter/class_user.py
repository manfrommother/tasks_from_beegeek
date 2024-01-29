'''
Реализуйте класс User, описывающий интернет-пользователя. 
При создании экземпляра класс должен принимать два аргумента в следующем порядке:

name — имя пользователя. Если name не является непустой строкой, состоящей только из букв,
 должно быть возбуждено исключение ValueError с текстом:
Некорректное имя
age — возраст пользователя. Если age не является целым числом, принадлежащим отрезку [0; 110], 
должно быть возбуждено исключение ValueError с текстом:
Некорректный возраст
Экземпляр класса User должен иметь два атрибута:

_name — имя пользователя
_age — возраст пользователя
Класс User должен иметь четыре метода экземпляра:

get_name() — метод, возвращающий имя пользователя
set_name() — метод, принимающий в качестве аргумента значение new_name и изменяющий имя пользователя на new_name. Если new_name не является непустой строкой, состоящей только из букв, должно быть возбуждено исключение ValueError с текстом:
Некорректное имя
get_age() — метод, возвращающий возраст пользователя
set_age() — метод, принимающий в качестве аргумента значение new_age и изменяющий возраст пользователя на new_age. Если new_age не является целым числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение ValueError с текстом:
Некорректный возраст
'''

class User():

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def set_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')

    def set_age(self, age):
        if isinstance(age,(int)) and age < 110 and age > 0:
            self._age = age
        else:
            raise ValueError('Некорректный возраст')
        
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
        

user = User('Меган', 37)

invalid_ages = ('ten', [], '', [True], -1, 111, 136, -50, 18.5)
for age in invalid_ages:
    try:
        user.set_age(age)
    except ValueError as e:
        print(e)
