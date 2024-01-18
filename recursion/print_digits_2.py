'''

'''
def print_digits(numbers):
    numbers = str(numbers)
    if len(numbers) > 0:
        print_digits(numbers[:-1:])
        print(numbers[-1])

print_digits(1234)