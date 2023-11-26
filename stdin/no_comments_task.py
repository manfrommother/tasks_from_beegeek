import sys


for line in sys.stdin:
    if line.lstrip().rstrip().startswith('#'):
        continue
    else:
        print(line.rstrip(), sep='\n')