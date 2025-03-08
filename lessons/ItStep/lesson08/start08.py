# Задача 1: Капсулированный термометр.
#
# Создай класс Thermometer, который:
#   •Имеет приватное поле _temperature (градусы Цельсия).
#   •Метод set_temperature(value), который устанавливает температуру, но не ниже -273.15°C.
#   •Метод get_temperature(), который возвращает текущую температуру.

class Thermometer:
    def __init__(self):
        self.__temperature = 0

    def set_temperature(self, value):
        if value >= -273.15:
            self.__temperature = value
        else:
            print("Temperatura nie moget byt' men\'sze -273.15")

    def get_temperature(self):
        return self.__temperature


#
# thermo = Thermometer()
# thermo.set_temperature(25)
# print(thermo.get_temperature())  # 25
# thermo.set_temperature(-300)
#
#
# print()
# print()

# Задача 3: Счетчик просмотров.
#
# Создай класс Video, который:
#   •Имеет приватное поле _views, содержащее количество просмотров.
#   •Метод watch(), который увеличивает счетчик на 1.
#   •Метод get_views(), который возвращает количество просмотров.

class Video:
    def __init__(self):
        self.__views = 0

    def watch(self):
        self.__views += 1

    def get_views(self):
        return self.__views


#
# video = Video()
# video.watch()
# video.watch()
# video.watch()
# print(video.get_views())  # 2


# Задача 2: Транспорт
#
# Создай базовый класс Transport, который:
#   •Имеет атрибут speed (скорость).
#   •Метод move(), который выводит "Транспорт движется со скоростью X км/ч".
#
# Создай подклассы:
#   •Car, который в move() добавляет " Машина едет по дороге.".
#   •Bicycle, который в move() добавляет " Велосипед движется по велодорожке.".
#   •Airplane, который в move() добавляет " Самолет летит в небе.".

# class Transport:
#     def __init__(self, speed):
#         self.speed = speed
#
#     def move(self):
#         print(f"Транспорт движется со скоростью {self.speed} км/ч.")
#
#
# class Car(Transport):
#     def move(self):
#         super().move()
#         print(f"Машина едет по дороге.")
#
#
# class Bicycle(Transport):
#     def move(self):
#         super().move()
#         print(f"Велосипед движется по велодорожке.")
#
#
# class Airplane(Transport):
#     def move(self):
#         super().move()
#         print(f"Самолет летит в небе.")


# car = Car(60)
# car.move()  # Транспорт движется со скоростью 60 км/ч. Машина едет по дороге.
#
# bike = Bicycle(20)
# bike.move()  # Транспорт движется со скоростью 20 км/ч. Велосипед движется по велодорожке.
#
# plane = Airplane(900)
# plane.move()  # Транспорт движется со скоростью 900 км/ч. Самолет летит в небе.


# Задача 3: Персонал
#
# Создай базовый класс Employee, который:
#   •Имеет атрибут name (имя).
#   •Метод work(), который выводит "Сотрудник работает".
#
# Создай подклассы:
#   •Doctor, который переопределяет work(), чтобы выводить "Доктор лечит пациентов.".
#   •Teacher, который переопределяет work(), чтобы выводить "Учитель объясняет урок.".

# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#     def work(self):
#         print("Сотрудник работает.")
#
#
# class Doctor(Employee):
#     def work(self):
#         print("Доктор лечит пациентов.")
#
#
# class Teacher(Employee):
#     def work(self):
#         print("Учитель объясняет урок.")


# doc = Doctor("Анна")
# doc.work()  # Доктор лечит пациентов.
#
# teacher = Teacher("Иван")
# teacher.work()  # Учитель объясняет урок.

# Задача 1: Система оплаты сотрудников
#
# Создай базовый класс Employee, который:
#   •  Имеет атрибуты name (имя) и salary (ставка).
#   •  Имеет метод calculate_pay(), который возвращает зарплату.
#
# Создай подклассы:
#   •  HourlyEmployee – у него есть hours_worked, а зарплата считается как salary * hours_worked.
#   •  SalariedEmployee – у него фиксированная зарплата (просто salary).
#   •  Manager – у него зарплата salary + bonus (дополнительный бонус).

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def calculate_pay(self):
#         return self.salary
#
#
# class HourlyEmployee(Employee):
#     def __init__(self, name, salary, hours_worked):
#         super().__init__(name, salary)
#         self.hours_worked = hours_worked
#
#     def calculate_pay(self):
#         return self.salary * self.hours_worked
#
# class SalariedEmployee(Employee):
#     pass
#
# class Manager(Employee):
#     def __init__(self, name, salary, bonus):
#         super().__init__(name, salary)
#         self.bonus = bonus
#
#     def calculate_pay(self):
#         return self.salary + self.bonus
#
#
#
# emp1 = HourlyEmployee("Анна", 15, 160)  # 15 у.е. в час, 160 часов
# print(emp1.calculate_pay())  # 2400
#
# emp2 = SalariedEmployee("Иван", 5000)  # Фикс 5000
# print(emp2.calculate_pay())  # 5000
#
# emp3 = Manager("Олег", 7000, 2000)  # 7000 + бонус 2000
# print(emp3.calculate_pay())  # 9000

# Задача 2: Управление пользователями и правами
#
# Создай базовый класс User, который:
#   •  Имеет атрибуты username и role (по умолчанию "user").
#   •  Имеет метод get_permissions(), который возвращает ["read"] для обычного пользователя.
#
# Создай подклассы:
#   •  AdminUser, у которого role = "admin" и права ["read", "write", "delete"].
#   •  ModeratorUser, у которого role = "moderator" и права ["read", "write"].

class User:
    def __init__(self, name):
        self.name = name
        self.role = "user"

    def get_permissions(self):
        return ["read"]


class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.role = "admin"

    def get_permissions(self):
        return ["read", "write", "delete"]


class ModeratorUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.role = "moderator"

    def get_permissions(self):
        return ["read", "write"]


# user = User("artur")
# print(user.get_permissions())  # ['read']
#
# admin = AdminUser("root")
# print(admin.get_permissions())  # ['read', 'write', 'delete']
#
# mod = ModeratorUser("mod123")
# print(mod.get_permissions())  # ['read', 'write']


# Задача 1: Полиморфная система заказов.
#
# Создай базовый класс Order, который:
#   •Имеет атрибут order_id и метод calculate_total(), который возвращает 0.
#
# Создай подклассы:
#   •PhysicalOrder – у него есть список товаров (items) и метод calculate_total(), который считает сумму цен всех товаров.
#   •DigitalOrder – у него фиксированная цена (price).
#   •SubscriptionOrder – у него есть цена за месяц (price_per_month) и количество месяцев (months).

class Order:
    def __init__(self, order_id):
        self.order_id = order_id

    def calculate_total(self):
        return 0


class PhysicalOrder(Order):
    def __init__(self, order_id, items):
        super().__init__(order_id)
        self.items = items

    def calculate_total(self):
        return sum(self.items)


class DigitalOrder(Order):
    def __init__(self, order_id, price):
        super().__init__(order_id)
        self.price = price

    def calculate_total(self):
        return self.price


class SubscriptionOrder(Order):
    def __init__(self, order_id, price_per_month, month):
        super().__init__(order_id)
        self.price_per_month = price_per_month
        self.month = month

    def calculate_total(self):
        return self.price_per_month * self.month


# order1 = PhysicalOrder(101, [100, 200, 300])
# print(order1.calculate_total())  # 600
#
# order2 = DigitalOrder(102, 500)
# print(order2.calculate_total())  # 500
#
# order3 = SubscriptionOrder(103, 50, 6)
# print(order3.calculate_total())  # 300


# Задача 2: Фигуры с расчетами площади и периметра
#
# Создай базовый класс Shape, который:
#   •  Имеет методы area() и perimeter(), которые возвращают 0.
#
# Создай подклассы:
#   •  Rectangle – принимает width и height и считает area = width * height, perimeter = 2 * (width + height).
#   •  Circle – принимает radius и считает area = π * r², perimeter = 2 * π * r.
#   •  Triangle – принимает три стороны a, b, c и использует формулу Герона для площади.

import math


class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# rect = Rectangle(10, 5)
# print(rect.area())  # 50
# print(rect.perimeter())  # 30
#
# circle = Circle(7)
# print(circle.area())  # 153.94
# print(circle.perimeter())  # 43.98
#
# tri = Triangle(3, 4, 5)
# print(tri.area())  # 6
# print(tri.perimeter())  # 12

#
# Задача 3: Логирование действий пользователей.
#
# Создай базовый класс Logger, который:
#   • Имеет метод log(message), который просто печатает сообщение.
#
# Создай подклассы:
#   • FileLogger – пишет лог в файл.
#   • ConsoleLogger – просто печатает сообщение (как базовый, но можешь изменить формат).
#   • DatabaseLogger – эмулирует запись лога в “базу” (можно просто сохранять в список).

class Logger:
    def log(self, message):
        print(message)


class FileLogger(Logger):
    def __init__(self, path_file):
        self.path_file = path_file

    def log(self, message):
        with open(self.path_file, "w", encoding="utf-8") as file:
            file.write(message)


class ConsoleLogger(Logger):
    pass


class DatabaseLogger(Logger):
    def __init__(self):
        self.database = []

    def log(self, message):
        self.database.append(message)


# file_logger = FileLogger("logs.txt")
# file_logger.log("Ошибка в системе")
# # file_logger.log("Error")
#
# console_logger = ConsoleLogger()
# console_logger.log("Приложение запущено")
#
# db_logger = DatabaseLogger()
# db_logger.log("Пользователь вошел в систему")
# print(db_logger.database)  # ['Пользователь вошел в систему']

# Задача 4: Система обработки платежей.
#
# Создай базовый класс PaymentProcessor, который:
#   •Имеет метод process_payment(amount), который просто выводит "Оплачено X у.е.".
#
# Создай подклассы:
#   •CreditCardPayment – добавляет 2% комиссии к amount.
#   •PayPalPayment – снимает фиксированную комиссию 1.5 у.е. .
#   •CryptoPayment – не берет комиссию, но требует transaction_fee (например, 0.0001 BTC).

class PaymentProcessor:
    def process_payment(self, amount):
        return f"Оплачено {amount} у.е."


class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Оплачено {amount + 0.02 * amount} у.е."


class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Оплачено {amount - 1.5} у.е."


class CryptoPayment(PaymentProcessor):
    def __init__(self, transaction_fee):
        self.transaction_fee = transaction_fee

    def process_payment(self, amount):
        return f"Оплачено {amount} у.е + комиссия {self.transaction_fee} BTC."


# credit = CreditCardPayment()
# print(credit.process_payment(100))  # 102
#
# paypal = PayPalPayment()
# print(paypal.process_payment(100))  # 98.5
#
# crypto = CryptoPayment(0.0001)
# print(crypto.process_payment(100))  # 100, но списывает еще 0.0001 BTC

# Задание:
#   1.  Создай базовый класс Vehicle с методом start_engine().
#   2.  Добавь классы Car и Bike, которые будут переопределять метод start_engine().
#   3.  В тестировании создай список транспортных средств и вызови метод start_engine() для каждого объекта.

# class Vehicle:
#     def start_engine(self):
#         return "Двигатель заведен."
#
# class Car(Vehicle):
#     def start_engine(self):
#         return "Автомобиль заведен."
#
# class Bike(Vehicle):
#     def start_engine(self):
#         return "Мотоцикл заведен."
#
# transports = [Car(), Bike()]
# for transport in transports:
#     print(transport.start_engine())


# Задание:
#   1.  Создай абстрактный класс PaymentMethod с абстрактным методом process_payment().
#   2.  Создай классы CreditCard и PayPal, которые реализуют метод process_payment().
#   3.  В тестировании создай список объектов разных платёжных систем и вызови метод process_payment() для каждого объекта, передавая сумму для платежа.

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self):
        pass

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        return f"S kreditki bylo oplaczeno {amount} y.e. ."

class PayPal(PaymentMethod):
    def process_payment(self, amount):
        return f"So sczeta PayPal bylo oplaczeno {amount} y.e. ."

accounts = [CreditCard(),PayPal()]
for account in accounts:
    print(account.process_payment(50))