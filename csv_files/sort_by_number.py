'''
Вам доступен файл deniro.csv, каждый столбец которого содержит либо только числа,
 либо строковые значения:

Machete,2010,72
Marvin's Room,1996,80
Raging Bull,1980,97
...
Напишите программу, которая сортирует содержимое данного файла по указанному столбцу. 
Причем данные должны быть отсортированы в порядке возрастания чисел, если столбец содержит числа, 
и в лексикографическом порядке слов, если столбец содержит слова.

Формат входных данных
На вход программе подается натуральное число — номер столбца файла deniro.csv.
'''


import csv


number_row = int(input()) - 1
with open('deniro.csv', encoding='utf-8') as file_csv:
    file_list = list(csv.reader(file_csv))
    sort_list = sorted(file_list, key=lambda x: int(x[number_row]) if x[number_row].isdigit() else x[number_row])
    
    for row in sort_list:
        print(*row, sep=',')




