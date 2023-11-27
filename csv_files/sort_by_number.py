import csv


number_row = int(input()) - 1
with open('deniro.csv', encoding='utf-8') as file_csv:
    file_list = list(csv.reader(file_csv))
    sort_list = sorted(file_list, key=lambda x: int(x[number_row]) if x[number_row].isdigit() else x[number_row])
    
    for row in sort_list:
        print(*row, sep=',')




