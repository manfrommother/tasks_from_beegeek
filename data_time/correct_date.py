from func_is_correct import is_correct
from datetime import date


while (test_word:=input())!="end":
    if is_correct(test_word) == True:
       print('Корректная')
    else:
        print('Некорректная')
    