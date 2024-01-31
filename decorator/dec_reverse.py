def reverse_args(func):
    def inner(*args, **kwargs):
        total_args = list(args)
        total_args = total_args[::-1]
        return func(*total_args, **kwargs)
    
    return inner

@reverse_args
def power(a, n):
    return a ** n
    
print(power(2, 3))
