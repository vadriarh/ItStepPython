# school
# id autoincrement name not null age email unique

import sqlite3

db_path = "test.db"


def connect():
    return sqlite3.connect(db_path)


def create_table():
    with connect() as conn:
        conn.execute("""DROP TABLE IF EXISTS school""")
        conn.execute("""CREATE TABLE IF NOT EXISTS school(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE
            )""")


def add_user(name: str, age: int, email: str):
    try:
        with connect() as conn:
            conn.execute("""INSERT INTO school (name, age, email)
            VALUES (?, ?, ?)""", (name, age, email))
    except:
        print("IntegrityError")


def show_users():
    with connect() as conn:
        cursor = conn.execute("""SELECT * FROM school""")
        print(cursor.fetchall())


def show_user(name: str):
    with connect() as conn:
        cursor = conn.execute("""SELECT * FROM school WHERE name = ?""", (name,))
        print(cursor.fetchone())


def update_user(id: int, name: str, age: int = None, email: str = None):
    if name:
        if age and email:
            with connect() as conn:
                conn.execute("""UPDATE school 
                SET name = ?, age = ?, email = ?
                WHERE id = ?""", (name, age, email, id))
        elif age:
            with connect() as conn:
                conn.execute("""UPDATE school 
                SET name = ?, age = ?
                WHERE id = ?""", (name, age, id))
        else:
            with connect() as conn:
                conn.execute("""UPDATE school 
                SET name = ?,  email = ?
                WHERE id = ?""", (name, email, id))
    else:
        print("Name is not be empty")


def delete_user(id: int):
    with connect() as conn:
        conn.execute("""DELETE FROM school 
        WHERE id = ?""", (id,))


create_table()
add_user("Anton", 25, "flakman@trick.nb")
add_user("Artur", 22, "f1lakman@trick.com")
add_user("David", 18, "sitreo@brain.fr")
add_user("Maxim", 23, "truthme@abobus.su")
add_user("Grzegorz", 31, "leprotko_sause@ymmie.mn")
add_user("Anatole", 27, "leprotko_sause@ymmie.mn")

show_users()
show_user("Maxim")

# update_user(2, "Kleo", 26, "hakumatum@spreo.jp")
# show_user("Kleo")
# delete_user(2)
# show_user("Kleo")


# Упражнения:
#   1.  Выбери всех пользователей с именем “Artur”.
#   2.  Найди пользователей с email на домене .com.
#   3.  Отсортируй пользователей по email в обратном порядке.
#   4.  Сгруппируй пользователей по имени и посчитай сколько раз каждое имя встречается.
def filter_db(command_db: str):
    with connect() as conn:
        cursor = conn.execute("""SELECT * FROM school """ + command_db)
        return cursor.fetchall()


print(filter_db("WHERE name = 'Artur'"))
print(filter_db("WHERE email LIKE '%.com'"))
print(filter_db("ORDER BY email DESC"))
names = {}

for user in filter_db("ORDER BY name ASC"):
    if user[1] not in names.keys():
        names[user[1]] = 1
    else:
        names[user[1]] += 1
print(names)

with connect() as conn:
    cursor = conn.execute("""SELECT name, COUNT(*) FROM school GROUP BY name """)
    print(cursor.fetchall())
