from datetime import date


'''
Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.

Формат входных данных
На вход программе подаются две корректные даты в ISO формате (YYYY-MM-DD), каждая на отдельной строке.

Формат выходных данных
Программа должна выбрать из двух введенных дат меньшую и вывести ее в формате DD-MM (YYYY).
'''

#вариант с более читаемым кодом

'''year, month, day = input().split('-')
year1, month1, day1 = input().split('-')

my_date = date(int(year), int(month), int(day))
my_date1 = date(int(year1), int(month1), int(day1))

print(min(my_date, my_date1).strftime('%d-%m (%Y)'))
'''

#Второй вариант решения в одну строку

print(min(date.fromisoformat(input()), date.fromisoformat(input())).strftime('%d-%m (%Y)'))