from datetime import date


date_list = []

for _ in range(int(input())):
    date_list.append(date.fromisoformat(input()))

date_list = sorted(date_list)

for i in range(len(date_list)):
    print(date_list[i].strftime('%d/%m/%Y'))
    
