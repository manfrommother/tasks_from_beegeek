'''
Реализуйте класс Pet, описывающий домашнее животное. При создании экземпляра класс должен принимать один аргумент:

name — имя домашнего животного
Экземпляр класса Pet должен иметь один атрибут:

name — имя домашнего животного
Класс Pet должен иметь три метода класса:

first_pet() — метод, возвращающий самый первый созданный экземпляр класса Pet. 
Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
last_pet() — метод, возвращающий самый последний созданный экземпляр класса Pet. 
Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
num_of_pets() — метод, возвращающий количество созданных экземпляров класса Pet
'''
class Pet:

    name_lst = []

    def __init__(self, name):
        self.name_lst.append(self)
        self.name = name

    @classmethod
    def first_pet(cls):
        return cls.name_lst[0] if cls.name_lst else None
    
    @classmethod
    def last_pet(cls):
        return cls.name_lst[-1] if cls.name_lst else None
    
    @classmethod
    def num_of_pets(cls):
        return len(cls.name_lst)
    
