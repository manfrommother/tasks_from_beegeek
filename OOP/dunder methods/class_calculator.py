class Calculator:

    def __init__(self):
        pass

    def __call__(self, a, b, operator):
        if b == 0 and operator == '/':
            raise ValueError('Деление на ноль невозможно')
        total_str = f'{a} {operator} {b}'
        return eval(total_str)
    
calculator = Calculator()

print(calculator(10, 5, '+'))
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*'))
print(calculator(10, 0, '/'))
    


