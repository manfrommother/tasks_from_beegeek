def do_twice(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    
    return inner

@do_twice
def beegeek(a, b, sep):
    print(a + b + sep)
    
beegeek(1, 2, sep=10)