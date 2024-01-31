'''
Реализуйте декоратор sandwich, который выводит тексты:

---- Верхний ломтик хлеба ----
---- Нижний ломтик хлеба ----
до и после вызова декорируемой функции соответственно.
'''

def sandwich(func):
    def bread(*args, **kwargs):
        print(f'---- Верхний ломтик хлеба ----')
        total = func(*args, **kwargs)
        print(f'---- Нижний ломтик хлеба ----')
        return total
        
    return bread

@sandwich
def beegeek():
    return 'beegeek'
    
print(beegeek())