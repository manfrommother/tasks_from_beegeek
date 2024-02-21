'''
Реализуйте класс BasicPlan, описывающий подписку базового уровня на некотором онлайн-сервисе. При создании экземпляра класс не должен принимать никаких аргументов.

Класс BasicPlan должен иметь семь атрибутов:

can_stream —  атрибут, имеющий значение True
can_download — атрибут, имеющий значение True
has_SD — атрибут, имеющий значение True
has_HD — атрибут, имеющий значение False
 has_UHD — атрибут, имеющий значение False
num_of_devices — атрибут, имеющий значение 1
price — атрибут, имеющий значение 8.99$
2. Также реализуйте класс SilverPlan, 
наследника класса BasicPlan, описывающий подписку 
среднего уровня на некотором онлайн-сервисе. 
Процесс создания экземпляра класса SilverPlan должен 
совпадать с процессом создания экземпляра класса BasicPlan.

Класс SilverPlan должен иметь семь атрибутов:

can_stream —  атрибут, имеющий значение True
can_download — атрибут, имеющий значение True
has_SD — атрибут, имеющий значение True
has_HD — атрибут, имеющий значение True
 has_UHD — атрибут, имеющий значение False
num_of_devices — атрибут, имеющий значение 2
price — атрибут, имеющий значение 12.99$
3. Наконец, реализуйте класс GoldPlan, 
наследника класса BasicPlan, описывающий 
подписку высокого уровня на некотором онлайн-сервисе. 
Процесс создания экземпляра класса GoldPlan должен совпадать 
с процессом создания экземпляра класса BasicPlan.

Класс GoldPlan должен иметь семь атрибутов:

can_stream —  атрибут, имеющий значение True
can_download — атрибут, имеющий значение True
has_SD — атрибут, имеющий значение True
has_HD — атрибут, имеющий значение True
 has_UHD — атрибут, имеющий значение True
num_of_devices — атрибут, имеющий значение 4
price — атрибут, имеющий значение 15.99$
'''

class BasicPlan:

        can_stream = True
        can_download = True
        has_SD = True
        has_HD = False
        has_UHD = False
        num_of_devices = 1
        price = f'8.99$'

class SilverPlan(BasicPlan):
        
        has_HD = True
        num_of_devices = 2
        price = f'12.99$'

class GoldPlan(BasicPlan):
        
        has_HD = True
        has_UHD = True
        num_of_devices = 4
        price = f'15.99$'



print(GoldPlan.can_stream)
print(GoldPlan.can_download)
print(GoldPlan.has_SD)
print(GoldPlan.has_HD)
print(GoldPlan.has_UHD)
print(GoldPlan.num_of_devices)
print(GoldPlan.price)