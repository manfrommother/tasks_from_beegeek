months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

try:
    months_number = int(input())
    print(months[months_number])
except KeyError:
    print('Введено число из недопустимого диапазона')
except ValueError:
    print('Введено некорректное значение')
