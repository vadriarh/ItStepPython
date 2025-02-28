class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book name is {self.title}."


class Library:
    def __init__(self):
        self.books = dict()

    def add_book(self, title):
        if title not in self.books.keys():
            self.books[title] = Book(title)
            print(f"Book {title} added.")
        else:
            print(f"{title}: This book exists.")

    def remove_book(self, title):
        if title in self.books.keys():
            self.books.pop(title)
            print(f"Book {title} removed.")
        else:
            print(f"{title}: This book not exists.")

    def show_books(self):
        for book in self.books:
            print(f"{book}:{self.books[book]}")

# Test Data
# l1 = Library()
# l1.add_book("AS")
# l1.add_book("Ad")
# l1.add_book("aw")
# l1.add_book("qf")
# l1.add_book("nb")
# l1.add_book("AS")
# l1.add_book("df")
# l1.show_books()
# l1.remove_book("AS")
# l1.remove_book("ra")
# l1.show_books()
# print(l1.books["nb"])
