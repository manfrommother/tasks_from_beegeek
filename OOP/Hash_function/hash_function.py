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
    start = 0
    end = len(obj) - 1
    first_step = 0
    second_step = 0

    while start < end:
        first_step += ord(obj[start]) * ord(obj[end])
        start += 1
        end -= 1
    if len(obj) % 2 != 0:
        first_step += ord(obj[len(obj) // 2])
    

    counter = 1
    for i in obj:
        if counter % 2 != 0:
            second_step += ord(i) * counter
            counter += 1
        else:
            second_step -= ord(i) * counter
            counter += 1

    return (first_step * second_step) % 123456791
 

print(hash_function(12345))

        