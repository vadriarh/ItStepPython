# Уровень 1 (Базовый)
# 	1.	Создайте класс Animal с атрибутом name и методом make_sound(), который возвращает "Какой-то звук".
# 	2.	Создайте классы Dog и Cat, наследуемые от Animal.
# 	•	В Dog метод make_sound() должен возвращать "Гав-гав!"
# 	•	В Cat метод make_sound() должен возвращать "Мяу!"
# 	3.	Создайте объекты dog = Dog("Шарик") и cat = Cat("Мурка").
# 	4.	Выведите их имена и звуки, которые они издают.

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Какой-то звук"


class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"


class Cat(Animal):
    def make_sound(self):
        return "Мяу!"


dog = Dog("Шарик")
cat = Cat("Мурка")

print(f"{dog.name} говорит {dog.make_sound()}")
print(f"{cat.name} говорит {cat.make_sound()}")
