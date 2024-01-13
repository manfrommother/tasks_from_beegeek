import sys

value_list = [i.rstrip() for i in sys.stdin]

number_sum = 0
count_str = 0

for i in value_list:
    if '.' in i:
        try:
            i = float(i)
            number_sum += i
        except ValueError:
            count_str += 1
    else:
        try:
            i = int(i)
            number_sum += i
        except ValueError:
            count_str += 1
    
    
print(number_sum, count_str, sep='\n')
