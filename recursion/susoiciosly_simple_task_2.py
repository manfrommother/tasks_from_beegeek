def from_zero(num=1):
    if num < 101:
        print(num)
        from_zero(num + 1)
    

from_zero()