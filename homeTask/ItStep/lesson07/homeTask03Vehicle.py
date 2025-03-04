# 1.	Создайте класс Vehicle с атрибутами brand и speed.
# 	2.	Создайте класс Car, наследуемый от Vehicle.
# 	•	Добавьте атрибут fuel_type
# 	•	Используйте super() для вызова конструктора Vehicle
# 	•	Добавьте метод info(), который выводит все характеристики
# 	3.	Создайте класс ElectricCar, наследуемый от Car.
# 	•	Добавьте атрибут battery_capacity
# 	•	Используйте super() для вызова конструктора Car
# 	•	Добавьте метод info(), который также показывает заряд батареи
# 	4.	Создайте объекты Car и ElectricCar, выведите их характеристики.

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def info(self):
        print(f"Brand: {self.brand}.\n"
              f"Speed: {self.speed}.")


class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def info(self):
        super().info()
        print(f"Fuel type: {self.fuel_type}.")


class ElectricCar(Car):
    def __init__(self, brand, speed, battery_capacity):
        fuel_type = "Electric"
        super().__init__(brand, speed, fuel_type)
        self.battery_capacity = battery_capacity

    def info(self):
        super().info()
        print(f"Battery capacity: {self.battery_capacity}.")


bmw = Car("BMW", 320, "Gasoline")
tesla = ElectricCar("Tesla", 260, 125)

bmw.info()
print()
tesla.info()
