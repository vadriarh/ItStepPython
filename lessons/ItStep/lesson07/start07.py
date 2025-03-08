# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say(self):
#         print(f"My name is {self.name}. I have {self.age} years.")
#
# h1 = Human("Anton", 23)
# h1.say()

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, cash):
#         self.balance+=cash
#         print(f"Balance replenishment on {cash}")
#
#     def withdraw(self, cash):
#         if self.balance < cash:
#             print("Not enough money.")
#         else:
#             self.balance -= cash
#             print(f"Cash withdrawal in {cash}.")
#
#     def status(self):
#         print(f"Balance: {self.balance}")
#
# account = BankAccount("Anton",2000)
# account.deposit(500)
# account.status()
# account.withdraw(1500)
# account.status()
# account.withdraw(1500)
# account.status()
# account.withdraw(1000)
# account.status()

# class Car:
#     def __init__(self, model, color,price):
#         self.model = model #public
#         # self.color = color  #public
#         self._color = color #protected
#         self.__price = price #private
#
#
#     def show_info(self):
#         print(f" model {self.model}. color {self._color}. price {self.__price}")
#
# car = Car("BMW","Black", 1500)
# car.show_info()
# car._color = "Red"
# car.show_info()
# print(car.__price)
# car.show_info()

# Артур, [01.03.2025 12:28]
# 1 Задание:
# Создай класс User, который содержит:
#   •  публичный атрибут name,
#   •  защищенный атрибут _email,
#   •  приватный атрибут __password,
#   •  метод show_info(), который выводит имя и email,
#   •  метод set_password(new_password), который изменяет __password,
#   •  метод check_password(password), который сравнивает переданный пароль с __password.
#
# Артур, [01.03.2025 12:28]
# Дополнительно: Проверь, можно ли получить доступ к _email и __password извне.

# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self._email = email
#         self.__password = password
#
#     def show_info(self):
#         print(f"Name: {self.name}.\nEmail: {self._email}")
#
#     def show_password(self):
#         print(f"password: {self.__password}")
#
#     def set_password(self, new_password):
#         self.__password = new_password
#         print("Password changed.")
#
#     def check_password(self, password):
#         if self.__password == password:
#             print("Passwords match.")
#         else:
#             print("Passwords not match.")
#
# user = User("anton","anton@mail.com","Yuuer")
# user.show_info()
# user.set_password("Uyww")
# user.show_password()
# user.check_password("Yuuer")
# user.check_password("Uyww")
# user._email = "asdf"
# user.show_info()
# # user.__password = "qwd"
# print(user.__password)
# user.show_password()


# Условие:
#
# Создай класс Product, который представляет товар в магазине.
#
# Атрибуты:
#   •  name – публичный (название товара).
#   •  _price – защищенный (цена товара).
#   •  __discount – приватный (размер скидки в процентах, от 0 до 50).
#
#  Методы:
#   •  get_price() – возвращает цену с учетом скидки.
#   •  set_discount(discount) – устанавливает скидку (но не более 50%).
#
# Дополнительно: Запрети установку скидки более 50%, но попробуй обойти ограничение через _Product__discount.

# class Product:
#     def __init__(self, name, price, discount = 0):
#         self.name = name
#         self._price = price
#         self.__discount = discount if 0 <= discount <= 50 else 0 if discount < 0 else 50
#
#     def get_price(self):
#         return f"Price with discount: {self._price - self.__discount / 100 * self._price}"
#
#     def set_discount(self, discount):
#         if 0 <= discount <= 50:
#             self.__discount = discount
#             print("Discount changed.")
#         else:
#             print("Incorrect discount.")
#
#
# item = Product("Laptop", 1000)
#
# print(item.get_price())  # ✅ 1000
#
# item.set_discount(10)
# print(item.get_price())  # ✅ 900
#
# item.set_discount(60)  # ❌ Ошибка: Скидка не может быть больше 50%!
# print(item.get_price())  # ✅ 900
#
# # Попробуй изменить скидку напрямую
# # print(item.__discount)  # ❌ Ошибка!
# item._Product__discount = 70  # ⚠️ Обход ограничения
# print(item.get_price())  # ⚠️ 700 (но так делать нельзя!)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def say_hello(self):
#         return "Hello"
#
#
# class Dog(Animal):
#     def say_hello(self):
#         return "Woof"
#
#
# class Cat(Animal):
#     def say_hello(self):
#         return "Meow"
#
# dog = Dog("Bob")
# cat = Cat("Tom")
# print(f"{dog.name} say {dog.say_hello()}")
# print(f"{cat.name} say {cat.say_hello()}")

# class Vehicle:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#
#     def show_info(self):
#         print(f"Model: {self.model}, Year: {self.year}")
#
#
# class Car(Vehicle):
#     def __init__(self, model, year, color):
#         super().__init__(model, year)
#         self.color = color
#
#     def show_info(self):
#         print(f"Model: {self.model}, Year: {self.year}, Color: {self.color}")
#
#
# car = Car("BMW", 2020, "Black")
# car.show_info()
# print(car.model)
# print(car.year)

# class Computer:
#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram
#
#
# class Laptop(Computer):
#     def __init__(self,cpu, ram, battery_life):
#         super().__init__(cpu, ram)
#         self.battery_life = battery_life
#
#     def show_info(self):
#         return f"CPU: {self.cpu}\nRAM: {self.ram}\nBattery life: {self.battery_life} hours"
#
# laptop = Laptop("Intel", 4086, 11)
# print(laptop.cpu)
# print(laptop.ram)
# print(laptop.battery_life)
# print(laptop.show_info())


# Создайте class Animal с make_sound(),
# наследуйтесь и переопределите метод в Dog и Bird.

class Animal:
    def make_sound(self):
        return "Hello"


class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Bird(Animal):
    def make_sound(self):
        return "Pew-Pew"
