class Numbers():

    def __init__(self):
        self.numbers_list = []

    def add_number(self, number):
        self.numbers_list.append(number)

    def get_even(self):
        return [i for i in self.numbers_list if i % 2 == 0]
    
    def get_odd(self):
        return [i for i in self.numbers_list if i % 2 != 0]
    

numbers = Numbers()

numbers.add_number(3)
numbers.add_number(2)
numbers.add_number(1)
numbers.add_number(4)

print(numbers.get_even())
print(numbers.get_odd())