# 1.	Создайте класс Person с атрибутом name и методом introduce(), который возвращает "Привет, меня зовут {name}".
# 	2.	Создайте класс Student, наследуемый от Person.
# 	•	Добавьте атрибут university
# 	•	Переопределите introduce(), чтобы он возвращал:
# "Привет, меня зовут {name}, я учусь в {university}"


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Привет, меня зовут {self.name}"


class Student(Person):
    def __init__(self, name, university):
        super().__init__(name)
        self.university = university

    def introduce(self):
        return f"Привет, меня зовут {self.name}, я учусь в {self.university}"


student = Student("Артем", "МГУ")
print(student.introduce())
