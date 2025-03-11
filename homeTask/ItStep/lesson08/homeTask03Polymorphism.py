# Создайте два класса Bird и Plane, которые имеют:
# 	•	Метод fly(), но с разной реализацией:
# 	•	Bird выводит: “Птица машет крыльями и летит”.
# 	•	Plane выводит: “Самолет разгоняется и взлетает”.
# Напишите функцию start_flying(entity), которая принимает объект и вызывает у него метод fly(), не зная заранее, птица это или самолет.
# 📌 Дополнительно:
# 	•	Добавьте еще один класс Superhero, у которого тоже есть метод fly().
# 	•	Передайте в start_flying() объекты Bird, Plane и Superhero.

class Bird:
    def fly(self):
        print("Птица машет крыльями и летит")


class Plane:
    def fly(self):
        print("Самолет разгоняется и взлетает")


class Superhero:
    def fly(self):
        print("Поднимая кулак взлетает ввысь")


def start_flying(entity):
    entity.fly()


# Test Data
flying = [Bird(), Plane(), Superhero()]
for entity in flying:
    entity.fly()
