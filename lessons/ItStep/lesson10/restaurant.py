# Задача:
#
# Создайте систему для управления заказами в ресторане. Каждый заказ состоит из списка блюд, и должен содержать методы для добавления блюда в заказ и расчета стоимости заказа. Также создайте класс для каждого типа блюда (например, пицца и паста), который будет хранить информацию о названии, цене и порции.
#
# Требования:
#   1.  Абстракция: Создайте абстрактный класс Dish, который будет содержать абстрактные методы для получения стоимости и отображения информации о блюде.
#   2.  Наследование: Создайте классы-наследники для различных типов блюд, например, Pizza и Pasta.
#   3.  Инкапсуляция: Сделайте атрибуты блюда, такие как название, цена и порция, приватными и используйте методы для их доступа.
#   4.  Полиморфизм: Реализуйте метод получения стоимости и отображения информации по-разному для разных типов блюд.
#   5.  Композиция: Создайте класс Order, который будет хранить список блюд и рассчитывать общую стоимость заказа.

from abc import ABC, abstractmethod


class Dish(ABC):
    def __init__(self, name: str, price: float, portion: int):
        self.__name = name
        self.__price = price
        self.__portion = portion

    @abstractmethod
    def checkout(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_portion(self):
        return self.__portion


class Pizza(Dish):
    def __init__(self, name: str, price: float, portion: int, ingredients: list):
        super().__init__(name, price, portion)
        self.ingredients = ingredients

    def checkout(self):
        return self.get_portion() * (self.get_price() * 50 * (len(self.ingredients) + 2))

    def get_info(self):
        return f"{self.get_portion()} {self.get_name()} pizzas at {self.checkout()} each with ({", ".join(self.ingredients)}) ingredients."


class Pasta(Dish):
    def __init__(self, name: str, price: float, portion: int, sos_type: str):
        super().__init__(name, price, portion)
        self.sos_type = sos_type

    def checkout(self):

        return self.get_portion() * (self.get_price() + 75 if self.sos_type else 0)

    def get_info(self):
        return f"Pasta"


class Order:
    def __init__(self, list_dishes: list):
        self.list_dishes = list_dishes

    def get_total(self):
        pass