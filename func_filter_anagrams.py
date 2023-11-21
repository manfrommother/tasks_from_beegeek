# Анаграммы — это слова, которые состоят из одинаковых букв. Например:

#адаптер — петарда
#адресочек — середочка
#азбука — базука
#аистенок — осетинка
#Реализуйте функцию filter_anagrams(), которая принимает два аргумента в следующем порядке:

#word — слово в нижнем регистре
#words — список слов в нижнем регистре
#Функция должна возвращать список, элементами которого являются слова из списка words, которые представляют анаграмму слова word. Если список words пуст или не содержит анаграмм, функция должна вернуть пустой список.

#Примечание 1. Слова в возвращаемом функцией списке должны располагаться в своем исходном порядке. 

#Примечание 2. Считайте, что слово является анаграммой самого себя.


def filter_anagrams(word='', *args):
    total = []
    ord_sum= sum([ord(i) for i in word])
    for k in range(len(args[0])):
        guess = sum(ord(i) for i in args[0][k])
        if ord_sum == guess:
            total.append(args[0][k])
            

    return total

    


print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))











#Хочу спать сильно-сильно

