# Создайте абстрактный класс Device, который:
# 	•	Имеет абстрактный метод turn_on().
# 	•	Имеет абстрактный метод turn_off().
# Создайте два подкласса:
# 	•	Smartphone, который реализует turn_on() как “Смартфон включается” и turn_off() как “Смартфон выключается”.
# 	•	Laptop, который реализует turn_on() как “Ноутбук загружается” и turn_off() как “Ноутбук выключается”.
# 📌 Дополнительно:
# 	•	Попробуйте создать экземпляр Device. Что произойдет?
# 	•	Добавьте еще один подкласс, например Tablet, и реализуйте в нем turn_on() и turn_off().

from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Smartphone(Device):
    def turn_on(self):
        print("Смартфон включается")

    def turn_off(self):
        print("Смартфон выключается")


class Laptop(Device):
    def turn_on(self):
        print("Ноутбук включается")

    def turn_off(self):
        print("Ноутбук выключается")


class Tablet(Device):
    def turn_on(self):
        print("Планшет включается")

    def turn_off(self):
        print("Планшет выключается")

#Test Data
# dev = Device()    # невозможно создать объект, так как абстрактные методы требуют своей реализации
smart = Smartphone()
lap = Laptop()
tabl = Tablet()

smart.turn_on()
smart.turn_off()

lap.turn_on()
lap.turn_off()

tabl.turn_on()
tabl.turn_off()
