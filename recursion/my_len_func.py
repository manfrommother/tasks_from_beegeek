def my_len(number):
    if number < 10:
        return 1
    return 1 + my_len(number // 10)
    

print(my_len(int(input())))