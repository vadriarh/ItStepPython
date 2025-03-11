# Создайте базовый класс Employee (сотрудник), который содержит:
# 	•	Атрибуты: name (имя), salary (зарплата).
# 	•	Метод get_info(), который выводит информацию о сотруднике.
# Создайте дочерний класс Manager, который:
# 	•	Наследует Employee.
# 	•	Добавляет новый атрибут bonus.
# 	•	Переопределяет метод get_info(), чтобы также выводить размер бонуса.
# 📌 Дополнительно:
# 	•	Создайте несколько объектов и выведите информацию о них.
# 	•	Попробуйте создать еще один подкласс, например Developer, у которого есть атрибут programming_language.

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_info(self):
        print(f"Name: {self._name}.\nSalary: {self._salary}.")


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self._bonus = bonus

    def get_info(self):
        super().get_info()
        print(f"Bonus: {self._bonus}.")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self._programming_language = programming_language

    def get_info(self):
        super().get_info()
        print(f"Programming language: {self._programming_language}.")


# Test Data
emp1 = Employee("Anton", 7000)
man1 = Manager("Taras", 12000, 5000)
dev1 = Developer("Maksim", 14000, "C++")

emp1.get_info()
man1.get_info()
dev1.get_info()
