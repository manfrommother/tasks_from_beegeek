import csv
d = {}
with open('salary_data.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=';'))
    for key, value in rows[1:]:
        d[key] = d.get(key, []) + [int(value)]

    d_sort = sorted(d, key=lambda x: (sum(d[x]) / len(d[x]), x))
    print(*d_sort, sep='\n')