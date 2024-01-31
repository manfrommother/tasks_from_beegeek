def my_print(func):
    def decor(*args, **kwargs):
        total_args = (str(i).upper() for i in args)
        total_kwargs = {k: kwargs[k].upper() for k in kwargs}
        func(*total_args, **total_kwargs)
        
    return decor

print = my_print(print)

print('hi', 'there', end='!')
