import sys
from statistics import fmean

student_list = [int(person.rstrip()) for person in sys.stdin]
if len(student_list) == 0:
    print('нет учеников')
else:
    print(f'Рост самого низкого ученика: {min(student_list)}')
    print(f'Рост самого высокого ученика: {max(student_list)}')
    print(f'Средний рост: {fmean(student_list)}')