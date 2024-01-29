'''
Реализуйте класс HourClock, описывающий часы с одной лишь часовой стрелкой.
 При создании экземпляра класс должен принимать один аргумент:

hours — количество часов. Если hours не является целым числом, 
принадлежащим диапазону [1; 12], должно быть возбуждено исключение ValueError с текстом:
Некорректное время
Класс HourClock должен иметь одно свойство:

hours — свойство, доступное для чтения и записи, возвращающее текущее количество часов.
При изменении свойство должно проверять, что новое значение является целым числом, 
принадлежащим диапазону [1; 12], в противном случае должно быть возбуждено исключение ValueError с текстом:
Некорректное время
'''

class HourClock():

    def __init__(self, hours):
        self.hours = hours

    def set_hours(self, hours):
        if isinstance(hours, int) and hours >= 1 and hours <= 12:
            self._hours = hours
        else:
            raise ValueError('Некорректное время')
        
    def get_hours(self):
        return self._hours
    
    hours = property(fget=get_hours, fset=set_hours)


time = HourClock(1)

print(time.hours)
for _ in range(11):
    time.hours += 1
    print(time.hours)