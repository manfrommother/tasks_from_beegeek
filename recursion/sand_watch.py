'''
Напишите программу с использованием рекурсивной функции, которая выводит изображение песочных часов, составленное из цифр 
1, 2, 3, и 4:
'''

def wand_satch(numb=1, repeat=16):
    if numb <= 4:
        print(f'{str(numb) * repeat: ^16}')
        wand_satch(numb + 1, repeat - 4)
    if numb <= 5:
        wand_satch(numb + 1, repeat - 4)
        print(f'{str(numb) * repeat: ^16}')
wand_satch()