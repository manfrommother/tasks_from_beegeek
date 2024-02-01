import functools

def repeat(repeat=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, repeat + 1):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator



@repeat(3)
def say_beegeek():
    '''documentation'''
    print('beegeek')
    
say_beegeek()