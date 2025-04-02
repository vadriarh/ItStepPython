# Задача:
#
# Создайте систему для управления заказами в ресторане. Каждый заказ состоит из списка блюд, и должен содержать методы
# для добавления блюда в заказ и расчета стоимости заказа. Также создайте класс для каждого типа блюда (например, пицца
# и паста), который будет хранить информацию о названии, цене и порции.
#
# Требования:
#   1.  Абстракция: Создайте абстрактный класс Dish, который будет содержать абстрактные методы для получения стоимости
#   и отображения информации о блюде.
#   2.  Наследование: Создайте классы-наследники для различных типов блюд, например, Pizza и Pasta.
#   3.  Инкапсуляция: Сделайте атрибуты блюда, такие как название, цена и порция, приватными и используйте методы для
#   их доступа.
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
        return self.get_portion() * (self.get_price() + 5 * (len(self.ingredients) + 2))

    def get_info(self):
        return (f"{self.get_portion()} {self.get_name()} pizzas at {self.checkout()} each"
                f" with ({", ".join(self.ingredients)}) ingredients.")


class Pasta(Dish):
    def __init__(self, name: str, price: float, portion: int, sos_type: str = None):
        super().__init__(name, price, portion)
        self.sos_type = sos_type

    def checkout(self):
        return self.get_portion() * (self.get_price() + (7.5 if self.sos_type else 0))

    def get_info(self):
        return (f"{self.get_portion()} {self.get_name()} pastas at {self.checkout()}"
                f" with {self.sos_type if self.sos_type is not None else "out"}  soses.")


class Order:
    def __init__(self, list_dishes: list):
        self.list_dishes = list_dishes

    def add_dish(self, dish: Dish):
        self.list_dishes.append(dish)

    def remove_dish(self, dish: Dish):
        self.list_dishes.remove(dish)

    def get_total(self):
        if self.list_dishes:
            summa = 0
            for dish in self.list_dishes:
                summa += dish.checkout()
            return summa
        else:
            return "Order is empty"


pasta1 = Pasta("Carbonara", 12, 2, "carbonara")
pasta2 = Pasta("Bolognese", 14, 1, "bolognese")
pizza1 = Pizza("Havajska", 23, 1, ["ser", "ananas"])
pizza2 = Pizza("Capriciossa", 21, 2, ["ser", "szynka", "olivki", "pieczarki"])

list_dishes = [pasta1, pasta2, pizza1, pizza2]
for dish in list_dishes:
    print(dish.get_info())

order = Order(list_dishes)
print(order.get_total())
order.remove_dish(pizza2)
print(order.get_total())
order.add_dish(pizza2)
print(order.get_total())
