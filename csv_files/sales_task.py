import csv


with open('sales.csv', encoding='utf-8') as file:
    data = file.read()
    new_list = [r.split(';') for r in data.splitlines()]
    del new_list[0]
    for rows in new_list:
        if int(rows[1]) > int(rows[2]):
            print(*rows[0], sep='')
    