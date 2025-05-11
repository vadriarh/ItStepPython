import sqlite3

DB_PATH = "library.db"

LIMIT_RESULTS_OUTPUT = 5
program_enabled = True


def connect_db():
    return sqlite3.connect(DB_PATH)


def create_table():
    with connect_db() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT,
        year INTEGER
        )""")


def show_menu():
    print("Please make a choice.")
    print("1. Add book.")
    print("2. Show books.")
    print("3. Find books by author.")
    print("4. Find books by genre.")
    print("5. Delete book.")
    print("6. Sort books by year of publication.")
    print(f"7. Change the limit of results output. Current limit: {LIMIT_RESULTS_OUTPUT}")
    print("8. Book correcting.")
    print("9. Exit.")
    print()


def menu_command(number_command: int):
    return {
        1: add_book,
        2: show_all_books,
        3: find_author,
        4: find_genre,
        5: delete_book,
        6: show_sorted_books,
        7: change_limit,
        8: book_correct,
        9: stop_program

    }.get(number_command, lambda: error_info(ValueError))


def add_book():
    try:
        title = input("Title: ")
        if title == "":
            raise ValueError
        author = input("Author: ")
        if author == "":
            raise ValueError
        genre = input("Genre: ")
        year = int(input("Year: "))
        with connect_db() as conn:
            conn.execute("""INSERT INTO books (title, author, genre, year) 
            VALUES (?, ?, ?, ?)""", (title, author, genre, year))
    except sqlite3.Error as e:
        error_info(e)
    except Exception as e:
        error_info(e)


def show_books(books: list):
    if books:
        for book in books:
            print(f"{book[0]}. Title: {book[1]}.")
            print(f"   Author: {book[2]}.")
            print(f"   Genre: {book[3]}.")
            print(f"   Year: {book[4]}. ")
        print()
    else:
        book_not_exists()

def show_one_book(book:tuple):
    if book:
        print(f"{book[0]}. Title: {book[1]}.")
        print(f"   Author: {book[2]}.")
        print(f"   Genre: {book[3]}.")
        print(f"   Year: {book[4]}. ")
    else:
        book_not_exists()


def show_all_books():
    with connect_db() as conn:
        books = conn.execute("""SELECT * FROM books 
        LIMIT ?""", (LIMIT_RESULTS_OUTPUT,)).fetchall()
    show_books(books)


def find_author():
    author = input("Author: ")
    with connect_db() as conn:
        books = conn.execute("SELECT * FROM books "
                             "WHERE author LIKE ? LIMIT ?",
                             (f"%{author}%", LIMIT_RESULTS_OUTPUT)).fetchall()
    show_books(books)


def find_genre():
    genre = input("Genre: ")
    with connect_db() as conn:
        books = conn.execute("""SELECT * FROM books
            WHERE genre = ? LIMIT ?""", (genre, LIMIT_RESULTS_OUTPUT)).fetchall()
    show_books(books)


def delete_book():
    book_id = int(input("Book ID: "))
    with connect_db() as conn:
        book = conn.execute("""SELECT * FROM books
                    WHERE id = ?""",
                            (book_id,)).fetchone()
    if book:
        show_one_book(book)
        choice_deletion = input("Press y to confirm deletion, any key to cancel: ")
        if choice_deletion == "y":
            with connect_db() as conn:
                conn.execute("""DELETE FROM books 
                WHERE id = ?""", (book_id,))
        else:
            print("Deletion cancelled.")
    else:
        book_not_exists()





def show_sorted_books():
    year = input("Year of publication: ")
    with connect_db() as conn:
        books = conn.execute("""SELECT * FROM books
                WHERE year > ? ORDER BY year ASC LIMIT ?""",
                             (year, LIMIT_RESULTS_OUTPUT)).fetchall()
    show_books(books)


def change_limit():
    global LIMIT_RESULTS_OUTPUT
    try:
        LIMIT_RESULTS_OUTPUT = int(input("New limit: "))
    except ValueError:
        error_info(ValueError)


def book_correct():
    try:
        book_id = int(input("Book ID: "))
        with connect_db() as conn:
            book = conn.execute("""SELECT * FROM books
                WHERE id = ?""",
                                (book_id,)).fetchone()
        if book:
            show_one_book(book)
            title = input("New title: ")
            if title == "": title = book[1]
            author = input("New author: ")
            if author == "": author = book[2]
            genre = input("New genre: ")
            if genre == "": genre = book[3]
            year = input("New year: ")
            if year == "":
                year = book[4]
            else:
                year = int(year)
            with connect_db() as conn:
                conn.execute("""UPDATE books 
                        SET title = ?, author = ?, genre = ?, year = ?
                        WHERE id = ?""", (title, author, genre, year, book_id))
        else:
            book_not_exists()
    except sqlite3.Error as e:
        error_info(e)
    except Exception as e:
        error_info(e)


def stop_program():
    global program_enabled
    print("Program ended. Goodbye.")
    program_enabled = False


def error_info(e):
    print(f"{e}. Error. Please, retry.")
    return None

def book_not_exists():
    print("This book/books does not exist")
    print()


create_table()

print("Welcome to Library Manager.")
while program_enabled:
    show_menu()
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        error_info(ValueError)
        continue
    action = menu_command(choice)
    if action is not None:
        action()
