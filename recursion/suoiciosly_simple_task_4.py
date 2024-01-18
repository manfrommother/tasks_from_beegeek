def num(n = int(input())):
    if n != 0:
        num(int(input()))
    print(n)
num()  