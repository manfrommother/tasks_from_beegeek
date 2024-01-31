class Person():

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return self.name + ' ' + self.surname
    
    def set_fullname(self, info):
        self.name, self.surname = info.split()

    fullname = property(fset=set_fullname, fget=get_fullname)

person = Person('Меган', 'Фокс')

person = Person('Меган', 'Фокс')

person.name = 'Стефани'
print(person.fullname)