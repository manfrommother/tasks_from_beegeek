'''
Реализуйте функцию hash_function(), которая принимает один аргумент:

obj — произвольный объект
Функция должна вычислять хеш-значение объекта obj согласно следующему алгоритму:

вычисление значения выражения:
ord(obj[0]) * ord(obj[-1]) + ord(obj[1]) * ord(obj[-2]) + ord(obj[2]) * ord(obj[-3]) + ...
где obj — объект, преобразованный в строку с помощью функции str(). 
Обратите внимание, что суммироваться должны произведения первого и последнего элементов, 
второго и предпоследнего, и так далее до середины.
Если obj имеет нечетное количество символов, то серединный элемент должен прибавляться без перемножения
вычисление значения выражения:
ord(obj[0]) * 1 - ord(obj[1]) * 2 + ord(obj[2]) * 3 - ord(obj[3]) * 4 + ...
где obj — объект, преобразованный в строку с помощью функции str()
вычисление значения выражения:
(temp1 * temp2) % 123456791
где temp1 — значение, полученное в первом шаге, temp2 — значение, полученное во втором шаге
и возвращать значение, полученное в третьем шаге.
'''
def hash_function(obj):
    obj = str(obj)
    temp1 = temp2 = 0
    for i in range(len(obj) // 2):
        temp1 += ord(obj[i]) * ord(obj[-(i + 1)])
    if len(obj) % 2:
        temp1 += ord(obj[len(obj) // 2])
    for i, c in enumerate(obj, 1):
        temp2 += ord(c) * i * ((-1) ** (i + 1))
    return temp1 * temp2 % 123456791


        
