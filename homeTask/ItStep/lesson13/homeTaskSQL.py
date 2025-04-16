import sqlite3

# Найди трёх самых молодых пользователей с именами, начинающимися на “A”.
#  Выбери всех пользователей, чей возраст либо до 18, либо от 60 и выше.
#  Покажи имена и возраст всех пользователей, имя которых не ‘Ivan’, не ‘Petr’ и не ‘Lilit’.
#  Покажи всех пользователей, у кого имя содержит букву “e” (в любом месте).
#  Покажи возраст 5-ти последних пользователей, добавленных в базу.

db_path = "test.db"


def connect_db():
    return sqlite3.connect(db_path)


def create_table():
    with connect_db() as conn:
        conn.execute("""DROP TABLE IF EXISTS users""")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                age INTEGER,
                date_added DATE
            )""")


def add_user(username: str, age: int, date: str):
    with connect_db() as conn:
        conn.execute("""
        INSERT INTO users (username, age, date_added)
        VALUES (?, ?, ?)""", (username, age, date))


def filter_db(sql_command: str):
    with connect_db() as conn:
        cursor = conn.execute("""SELECT * FROM users """ + sql_command)
    return cursor.fetchall()


users = [
    ("James", 32, "2025-02-15"),
    ("Emily", 27, "2025-03-19"),
    ("Michael", 65, "2025-01-15"),
    ("Olivia", 12, "2024-07-12"),
    ("Ivan", 19, "2023-02-14"),
    ("William", 76, "2020-02-25"),
    ("Sophia", 29, "2021-03-23"),
    ("Benjamin", 21, "2023-02-14"),
    ("Petr", 47, "2024-02-15"),
    ("Emma", 24, "2023-02-15"),
    ("Daniel", 18, "2021-02-15"),
    ("Astaphiel", 28, "2023-12-11"),
    ("Esmarild", 28, "2022-01-27"),
    ("Lilith", 33, "2024-08-11"),
    ("Isabella", 11, "2023-06-11")
]

sql_commands = [
    ("Task 1", "WHERE username LIKE 'A%' ORDER BY age ASC LIMIT 3"),
    ("Task 2", "WHERE age < 18 OR age > 60"),
    ("Task 3", "WHERE username NOT IN ('Ivan', 'Petr', 'Lilith')"),
    ("Task 4", "WHERE username GLOB '*e*'"),
    ("Task 5", "ORDER BY date_added DESC LIMIT 5")
]

create_table()
for user in users:
    add_user(user[0], user[1], user[2])

for command in sql_commands:
    print(f"{command[0]}: {filter_db(command[1])}")
