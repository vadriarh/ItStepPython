class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.available = True

    def get_info(self):
        return f"\"{self.title}\". Author - {self.author}"

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        if not self.available:
            self.available = True


class Reader:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} take book {book.get_info()}.")
        else:
            print(f"{book.get_info()} been borrow.")

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{book.get_info()} was returned into library.")
        else:
            print(f"{book.get_info()} located in library.")

    def show_books(self):
        print(f"Name: {self.name}.\nBorrowed books: {len(self.borrowed_books)}.")
        if self.borrowed_books:
            for book in self.borrowed_books:
                print(book.get_info())
            print()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def show_books(self):
        if self.books:
            for book in self.books:
                print(f"[{"" if book.available else "NOT "}AVAILABLE] {book.get_info()}")


library = Library()
book1 = Book("Rasputin", "Czehov")
book2 = Book("Karenina", "Pushkin")
book3 = Book("Ternii", "Astahov")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.show_books()

reader = Reader("Pawel")
reader.show_books()
reader.borrow_book(book2)
reader.borrow_book(book1)
reader.show_books()

library.show_books()
reader.return_book(book2)
reader.return_book(book1)
reader.show_books()
library.show_books()
