from datetime import date


def print_good_dates(date_list):
    total_date_list = []

    for i in date_list:
        if i.year == 1992 and i.month + i.day == 29:
            total_date_list.append(i)
    
    for i in sorted(total_date_list):
        print(*i.strftime('%B %d, %Y'), end='\n', sep='')


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)
