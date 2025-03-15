# Задача: Система управления домашними животными
#
# Представь, что ты создаёшь систему для ветеринарной клиники. В клинику могут обращаться владельцы разных животных, но все животные имеют общие характеристики и поведение.
#
# Требования
#   1.  Создай абстрактный класс Animal, который содержит:
#   •  Поля name (имя животного) и age (возраст).
#   •  Абстрактный метод make_sound(), который должны реализовать потомки.
#   •  Метод info(), который выводит имя и возраст животного.
#   2.  Создай несколько классов-наследников, которые будут представлять конкретные виды животных:
#   •  Dog – добавь атрибут breed (порода) и реализуй make_sound(), чтобы собака лаяла.
#   •  Cat – добавь атрибут color (цвет шерсти) и реализуй make_sound(), чтобы кошка мяукала.
#   •  Parrot – добавь атрибут can_talk (может ли говорить) и реализуй make_sound() (если может говорить – повторяет слова, иначе просто чирикает).
#   3.  Создай несколько экземпляров разных животных и вызови у них make_sound() и info().
#
# Дополнительно: можно добавить метод feed(), который будет разный для каждого животного (например, собака ест мясо, кошка – рыбу, а попугай – зерно).

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self):
        pass

    def info(self):
        print(f"Name: {self.name}.")
        print(f"Age: {self.age}.")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        print("Bark-Bark.")

    def feed(self):
        print(f"Dog {self.name} eat meat.")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print("Meow.")

    def feed(self):
        print(f"Cat {self.name} eat fish.")


class Parrot(Animal):
    def __init__(self, name, age, can_talk):
        super().__init__(name, age)
        self.can_talk = can_talk

    def make_sound(self):
        if self.can_talk != "Can talk":
            print("Ary")
        else:
            print(f"{self.name} isss beautiful parrrrrot.")

    def feed(self):
        print(f"Parrot {self.name} eat corn.")


# dog = Dog("Beethoven", 4, "American Foxhound")
# cat = Cat("Steve", 1.5, "Grey")
# parrot = Parrot("Arnold", 3, "Can talk")
# for animal in [dog, cat, parrot]:
#     animal.info()
#     animal.make_sound()
#     animal.feed()

# Задача: Автопарк и система управления транспортом
#
# Ты разрабатываешь систему управления автопарком, в котором есть разные виды транспорта:
#       легковые автомобили, грузовики и велосипеды.
#   Каждый вид транспорта имеет свою скорость, способ передвижения и расход топлива (если он есть).
#
# ⸻
#
# Требования:
#   1.  Создай абстрактный класс Transport, который содержит:
#   •  Поля brand (марка) и max_speed (максимальная скорость).
#   •  Абстрактный метод move(), который должен быть реализован в дочерних классах.
#   •  Метод info(), который выводит информацию о транспорте.
#   2.  Создай три класса-наследника, реализующих транспортные средства:
#   •  Car (легковой автомобиль):
#   •  Дополнительное поле fuel_consumption (расход топлива на 100 км).
#   •  Реализация метода move(), который выводит, что машина едет с указанной скоростью.
#   •  Truck (грузовик):
#   •  Дополнительное поле cargo_capacity (грузоподъёмность).
#   •  Реализация метода move(), которая учитывает, что грузовик едет медленнее, если загружен.
#   •  Bicycle (велосипед):
#   •  Дополнительное поле type (тип велосипеда: горный, шоссейный).
#   •  Реализация метода move(), которая выводит, что велосипед движется на мускульной тяге.
#   3.  Создай несколько объектов разного транспорта и протестируй их поведение.

# Дополнительно (если хочешь хардкор):
#
# Добавь метод calculate_travel_time(distance), который вычисляет время в пути для заданного расстояния.
# У грузовика скорость уменьшается на 20%, если он загружен.

class Transport(ABC):
    def __init__(self, brand: str, max_speed: int):
        self.brand = brand
        self.max_speed = max_speed

    @abstractmethod
    def move(self):
        pass

    def info(self):
        print(f"Brand: {self.brand}.")
        print(f"Max speed: {self.max_speed}.")

    def calculate_travel_time(self, distance):
        print(f"{distance} km will pass by {distance / self.max_speed:.2f} hours.")


class Car(Transport):
    def __init__(self, brand, max_speed, fuel_consumption):
        super().__init__(brand, max_speed)
        self.fuel_consumption = fuel_consumption

    def move(self):
        print(f"The car is moving at speed {self.max_speed} km/h.")

    def fuel_needed(self, distance):
        print(f"Need {distance*self.fuel_consumption/100}litres.")


class Truck(Transport):
    def __init__(self, brand, max_speed, cargo_capacity=False):
        super().__init__(brand, max_speed)
        self.cargo_capacity = cargo_capacity

    def move(self):
        print(f"The truck is moving at speed {self.max_speed * (0.8 if self.cargo_capacity else 1)} km/h,"
              f" because it was{" " if self.cargo_capacity else " not "}loaded.")


class Bicycle(Transport):
    def __init__(self, brand, max_speed, type):
        super().__init__(brand, max_speed)
        self.type = type

    def move(self):
        print(f"The bicycle is moving at speed {self.max_speed} km/h on muscle traction.")


car = Car("BMW", 250, 7.2)
truck1 = Truck("Skania", 120, True)
truck2 = Truck("Mersedes", 140)
bicucle = Bicycle("Mintrea", 25, "City")
for transport in [car, truck1, truck2, bicucle]:
    transport.info()
    transport.move()
    transport.calculate_travel_time(125)
    if isinstance(transport,Car):
        transport.fuel_needed(125)


# Требования:
#   1.  Создай абстрактный класс ElectronicDevice, который содержит:
#   •  Поля brand (марка устройства) и power (мощность устройства в ваттах).
#   •  Абстрактный метод turn_on() и turn_off(), которые должны быть реализованы в дочерних классах.
#   •  Метод info(), который выводит информацию об устройстве.
#   2.  Создай три класса-наследника:
#   •  Smartphone (смартфон):
#   •  Дополнительное поле battery_life (время работы от батареи в часах).
#   •  Реализация методов turn_on() и turn_off() с выводом информации о зарядке устройства.
#   •  Laptop (ноутбук):
#   •  Дополнительное поле ram_size (размер оперативной памяти в ГБ).
#   •  Реализация методов turn_on() и turn_off() с выводом информации о запуске устройства.
#   •  Television (телевизор):
#   •  Дополнительное поле screen_size (диагональ экрана в дюймах).
#   •  Реализация методов turn_on() и turn_off() с выводом информации о включении устройства.
#   3.  Создай несколько объектов устройств и протестируй их включение и выключение.
#
# ⸻
#
# Дополнительно:
#
# Добавь возможность вывести состояние устройства (включено или выключено) и для каждого устройства добавь метод,
# который выводит “оставшийся ресурс” (например, для смартфона – оставшееся время работы от батареи, для ноутбука – сколько осталось памяти и т.д.).

class ElectronicDevice(ABC):
    def __init__(self, brand: str, power: int):
        self.brand = brand
        self.power = power
        self.__isOn = False
        self._resource = 15

    @abstractmethod
    def turn_on(self):
        if self._resource > 0 and self.__isOn == False:
            self.__isOn = True
            return True
        else:
            print("Unable to start the device. Not enough resources.")

    @abstractmethod
    def turn_off(self):
        self.__isOn = False

    def residual_resource(self):
        print(f"Residual_resource: {self._resource}%.")

    def tik(self):
        if self._resource > 10:
            self._resource -= 10
        else:
            print("The device has exhausted its resource. Shutdown.")
            self._resource = 0
            self.__isOn = False

    def info(self):
        print(f"Brand: {self.brand}.")
        print(f"Power: {self.power} watt.")

    def status(self):
        print(f"Device {self.brand} is {"on" if self.__isOn else "off"}.")


class Smartphone(ElectronicDevice):
    def __init__(self, brand, power, battery_life):
        super().__init__(brand, power)
        self.battery_life = battery_life

    def turn_on(self):
        if super().turn_on():
            print(f"Smarphone is on and will work {self.battery_life * self._resource / 100} hours.")

    def turn_off(self):
        super().turn_off()
        print("Smarphone is off.")


class Laptop(ElectronicDevice):
    def __init__(self, brand, power, ram_size):
        super().__init__(brand, power)
        self.ram_size = ram_size

    def turn_on(self):
        if super().turn_on():
            print(f"Laptop is on and have {self.ram_size * self._resource / 100} Gb on board.")

    def turn_off(self):
        super().turn_off()
        print("Laptop is off.")


class Television(ElectronicDevice):
    def __init__(self, brand, power, screen_size):
        super().__init__(brand, power)
        self.screen_size = screen_size

    def turn_on(self):
        if super().turn_on():
            print(f"Television is on and show video on {self.screen_size * self._resource / 100}\" display.")

    def turn_off(self):
        super().turn_off()
        print("Television is off.")


smartphone = Smartphone("Samsung", 65, 11)
laptop = Laptop("Dell", 19, 16)
tv = Television("Sharp", 45, 45)
for device in [smartphone, laptop, tv]:
    print()
    device.status()
    device.turn_on()
    device.status()
    device.residual_resource()
    device.status()
    device.tik()
    device.residual_resource()
    device.status()
    device.tik()
    device.residual_resource()
    device.status()
    device.turn_on()
    device.status()
