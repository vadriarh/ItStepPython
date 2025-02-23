class Person:
    def __init__(self, name="unknown", age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello! My name is {self.name}")


class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, Цена: {self.price}"

    # p1 = Person("anto", 34)
    #
    # print(p1.name)
    # print(p1.age)
    # p1.say_hello()

book = Book("August","Rubenov", 1998, 235)
print(book.get_info())
