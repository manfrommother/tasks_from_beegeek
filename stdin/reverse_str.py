'''
Напишите программу, которая принимает произвольное количество строк
и в каждой введенной строке располагает все символы в обратном порядке.

Формат входных данных
На вход программе подается произвольное количество строк.

Формат выходных данных
Программа должна вывести все введенные строки, 
предварительно расположив в каждой строке все символы в обратном порядке.
'''
import sys 


data = [line.rstrip()[::-1] for line in sys.stdin]
print(*data, sep='\n')