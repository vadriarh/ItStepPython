# Задача: Система учета сотрудников компании Ты разрабатываешь систему для управления сотрудниками в компании. В компании работают три типа сотрудников: офисные работники, разработчики и менеджеры. Каждый сотрудник имеет имя, возраст и зарплату, но у разных типов сотрудников есть свои особенности.
#
# Требования:
# 	1.	Создай абстрактный класс Employee, который содержит:
# 	•	Поля name (имя), age (возраст) и salary (зарплата).
# 	•	Абстрактный метод work(), который должен быть реализован в дочерних классах.
# 	•	Метод info(), который выводит информацию о сотруднике.
# 	2.	Создай три класса-наследника:
# 	•	OfficeWorker (офисный работник):
# 	•	Дополнительное поле department (отдел).
# 	•	Реализация метода work(), который выводит, что сотрудник работает в своем отделе.
# 	•	Developer (разработчик):
# 	•	Дополнительное поле programming_language (язык программирования).
# 	•	Реализация метода work(), который выводит, что разработчик пишет код на своём языке программирования.
# 	•	Manager (менеджер):
# 	•	Дополнительное поле team_size (размер команды).
# 	•	Реализация метода work(), который выводит, что менеджер управляет командой из team_size человек.
# 	3.	Создай несколько объектов сотрудников и протестируй их методы.

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str, age: int, salary: int):
        self._name = name
        self._age = age
        self._salary = salary

    @abstractmethod
    def work(self):
        pass

    def info(self):
        print(f"Name: \t{self._name}.")
        print(f"Age: \t{self._age}.")
        print(f"Salary: {self._salary}.")


class OfficeWorker(Employee):
    def __init__(self, name: str, age: int, salary: int, department: str):
        super().__init__(name, age, salary)
        self._department = department

    def work(self):
        print(f"Office worker {self._name} works in the {self._department} department.")


class Developer(Employee):
    def __init__(self, name: str, age: int, salary: int, programming_language: str):
        super().__init__(name, age, salary)
        self._programming_language = programming_language

    def work(self):
        print(f"Developer {self._name} writes code in {self._programming_language} language.")


class Manager(Employee):
    def __init__(self, name: str, age: int, salary: int, team_size: int):
        super().__init__(name, age, salary)
        self._team_size = team_size

    def work(self):
        print(f"Manager {self._name} manages a team of {self._team_size} people.")


# Test_Data
office_worker = OfficeWorker("Anton", 27, 6270, "HR")
dev = Developer("Michal", 23, 12000, "Python")
manager = Manager("Pawel", 34, 9200, 23)

for employee in [office_worker, dev, manager]:
    employee.info()
    employee.work()
    print()
