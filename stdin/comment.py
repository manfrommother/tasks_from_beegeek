import sys

code = [lines.rstrip().lstrip() for lines in sys.stdin]
print(len(list(filter(lambda x: x.startswith('#'), code))))