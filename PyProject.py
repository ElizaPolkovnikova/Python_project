# ----------------------------------- 1 ----------------------------------------
'''
Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '/':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'OK'
                else:
                    return f'Некорректный год'
            else:
                return f'Некорректный месяц'
        else:
            return f'Некорректный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('5 / 12 / 2022')
print(today)
print(Data.valid(11, 11, 2023))
print(today.valid(23, 13, 30))
print(Data.extract('12 / 07 / 1997'))
print(today.extract('02 / 11 / 2020'))
print(Data.valid(7, 10, 2000))


# ----------------------------------- 2 ----------------------------------------
'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве 
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class DivisionByZero:
    def __init__(self, dividend, divisor):
        self.divider = dividend
        self.denominator = divisor

    @staticmethod
    def divide_by_zero(dividend, divisor):
        try:
            result = dividend/divisor
        except:
            if divisor == 0:
                return f'На ноль делить нельзя!'
            else:
                return result
        return result


div_obj = DivisionByZero(1000, 1)
print(DivisionByZero.divide_by_zero(25, 0))
print(DivisionByZero.divide_by_zero(15, 0.2))
print(div_obj.divide_by_zero(1, 0))


# ----------------------------------- 3 ----------------------------------------
'''
Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у 
пользователя данные и заполнять список необходимо только числами. 
Класс-исключение должен контролировать типы данных элементов списка.
'''


class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter: '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Вводите только числа")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы завершили программу'
                else:
                    return f'Вы завершили программу'


try_except = Error(1)
print(try_except.my_input())


# --------------------------------- 4, 5, 6 --------------------------------------
'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — 
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, 
общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для 
каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём 
оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных 
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать 
любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем 
данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать 
строковый тип данных.
'''


class StoreOrgtech:
    def __init__(self, model, quantity, price):
        self.model = model
        self.quantity = quantity
        self.price = price
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {f'Инвентаризация. Модель техники: {self.model}, Количество, ед.: {self.quantity}, Цена: {self.price}'}


    def __str__(self):
        return f'Инвентаризация. Модель техники: {self.model}, ' \
               f'Количество, ед.: {self.quantity}, Цена: {self.price}'

    def inventory(self):
        while True:
            try:
                usr_tech_model = input('Введите модель техники: ')
                usr_quantity = int(input('Введите количество единиц: '))
                usr_price = int(input('Введите цену за единицу: '))
                usr_data_of_unit = {f'Тип техники: {usr_tech_model}, Количество, ед.: {usr_quantity}, Цена: {usr_price}'}
                self.my_unit.update(usr_data_of_unit)
                self.my_store.append(usr_data_of_unit)
                print(f'Текущий список: {self.my_store}')
            except TypeError:
                return f'Некорректный тип данных'

            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---> ')
            if q == 'Q' or q == 'q':
                self.my_store_full.append(self.my_store)
                print(f'Весь склад -\n {self.my_store_full}')
                return f'Выход'
            else:
                return StoreOrgtech.inventory(self)

class Printer(StoreOrgtech):
    def __init__(self, model, quantity, price, is_ink_jet):
        super().__init__(model, quantity, price)
        self.is_ink_jet = is_ink_jet

    def __str__(self):
        return f'{StoreOrgtech.__str__(self)}, Тип принтера: {self.is_ink_jet}'


class Skanner(StoreOrgtech):
    def __init__(self, model, quantity, price, sensor_type):
        super().__init__(model, quantity, price)
        self.sensor_type = sensor_type

    def __str__(self):
        return f'{StoreOrgtech.__str__(self)}, Тип датчика: {self.sensor_type}'

class Xerox(StoreOrgtech):
    def __init__(self, model, quantity, price, print_speed):
        super().__init__(model, quantity, price)
        self.print_speed = print_speed

    def __str__(self):
        return f'{StoreOrgtech.__str__(self)}, Скорость печати: {self.print_speed}'


unit_1 = Printer('Samsung', 2, 5000, 'Струйный')
unit_2 = Skanner('Honor', 4, 2000, 'sensor_type')
unit_3 = Xerox('Xerox', 1500, 1, '1000/sek')


print(unit_1) # Вывод инфо о позиции через ввод данных в программу
print(unit_2)
print(unit_3)
# print(unit_1.inventory()) # Вывод инфо о позиции через ввод данных от пользователя (input) и суммирование в список всех позиций
# print(unit_2.inventory())
# print(unit_3.inventory())


# ----------------------------------- 7 ----------------------------------------
'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». 
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. 
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение 
созданных экземпляров. Проверьте корректность полученного результата.
'''


class Cmplx:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, obj):
        self.sumax = self.x + obj.x
        self.sumay = self.y + obj.y
    def __mul__(self, obj):
        self.multx = self.x * obj.x - self.y * obj.y
        self.multy = self.y * obj.x + self.x * obj.y

x = float(input('x_1: '))
y = float(input('y_1: '))
a = Cmplx(x, y)
x = float(input('x_2: '))
y = float(input('y_2: '))
b = Cmplx(x, y)
a + b
a * b
print('Сумма:   %.2f+%.2fj' % (a.sumax, a.sumay))
print('Произведение: %.2f+%.2fj' % (a.multx, a.multy))
