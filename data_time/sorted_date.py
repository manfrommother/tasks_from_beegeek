'''
Напишите программу, которая принимает на вход последовательность дат и выводит их в порядке неубывания.

Формат входных данных
На вход программе подается натуральное число n, а затем  n корректных дат в ISO формате (YYYY-MM-DD), 
каждая на отдельной строке.

Формат выходных данных
Программа должна вывести введенные даты в порядке неубывания, каждую на отдельной строке, в формате DD/MM/YYYY.
'''
from datetime import date


date_list = []

for _ in range(int(input())):
    date_list.append(date.fromisoformat(input()))

date_list = sorted(date_list)

for i in range(len(date_list)):
    print(date_list[i].strftime('%d/%m/%Y'))


# и второе, более емкое решение 

'''
dates = [date.fromisoformat(input()) for _ in range(int(input()))]

for d in sorted(dates):
    print(d.strftime('%d/%m/%Y'))

'''
    
