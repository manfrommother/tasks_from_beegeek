import sys 


data = [line.rstrip()[::-1] for line in sys.stdin]
print(*data, sep='\n')