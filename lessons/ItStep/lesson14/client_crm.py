import sqlite3

db_path = "clients_list.db"


def connect():
    return sqlite3.connect(db_path)


def create_table():
    with connect() as conn:
        conn.execute("""DROP TABLE IF EXISTS clients""")
        conn.execute("""CREATE TABLE IF NOT EXISTS clients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        email TEXT,
        created_at DATE DEFAULT CURRENT_DATE)""")


def add_client(name: str, phone: int = None, email: str = None):
    with connect() as conn:
        conn.execute("""INSERT INTO clients (name, phone, email)
        VALUES (?,?,?)""", (name, phone, email))


def find_clients(name: str):
    with connect() as conn:
        cursor = conn.execute("""SELECT * FROM clients 
        WHERE name = ?""", (name,))
        return cursor.fetchall()


def sort():
    with connect() as conn:
        cursor = conn.execute("""SELECT * FROM clients ORDER BY created_at ASC""")
        return cursor.fetchall()


def show_menu():
    print("Menu.")
    print("1. Add client.")
    print("2. Find clients.")
    print("3. Sort clients.")
    print("4. Quit.")


def print_clients(clients):
    if clients:
        for client in clients:
            print(f"Client ID: {client[0]}. Name: {client[1]} "
                  f"PhoneNumber: {client[2]}. Email: {client[3]} "
                  f"Date: {client[4]}")
    else:
        print("No clients.")



create_table()

loop = True
choose = 0
print("Welcome in Client Manager.")
while loop:
    show_menu()
    try:
        choose = int(input("Please you choose: "))
    except:
        print(ValueError)
    if choose in range(1, 5):
        if choose == 1:
            add_client(input("Input name: "), input("Input phoneNumber: "), input("Input email: "))
            print("Client added")
        if choose == 2:
            print_clients(find_clients(input("Input name: ")))
        if choose == 3:
            print_clients(sort())
        if choose == 4:
            loop = False
            print("Program exiting.")
    else:
        print("Incorrect choose. Please retry.")

print("Goodbye")
