import sys

move = 1

for numb in sys.stdin:
    numb = int(numb)
    move += 1

if numb % 2 == 0:
    if move % 2 != 0:
        print('Дима')
    else:
        print('Анри')
else:
    if move % 2 != 0:
        print('Анри')
    else:
        print('Дима')
