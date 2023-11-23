from datetime import date


# year = date.fromisoformat(input())
'''year, month, day = input().split('-')
year1, month1, day1 = input().split('-')

my_date = date(int(year), int(month), int(day))
my_date1 = date(int(year1), int(month1), int(day1))

print(min(my_date, my_date1).strftime('%d-%m (%Y)'))
'''

print(min(date.fromisoformat(input()), date.fromisoformat(input())).strftime('%d-%m (%Y)'))