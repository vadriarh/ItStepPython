import sqlite3, os

db_path = "test.db"

if os.path.exists(db_path):
    os.remove(db_path)


def connect_db():
    return sqlite3.connect(db_path)


def create_table():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE IF EXISTS users""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        age INTEGER
    )""")
    conn.commit()
    conn.close()


def add_user(username: str, age: int):
    with connect_db() as conn:
        conn.execute("""
        INSERT INTO users (username, age)
        VALUES (?, ?)""", (username, age))


def get_all_users():
    with connect_db() as conn:
        cursor = conn.execute(
            "SELECT * FROM users")
    return cursor.fetchall()


def get_one_user(user_id: int):
    with connect_db() as conn:
        cursor = conn.execute(
            "SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


def update_user(user_id, username: str = None, age: int = None):
    with connect_db() as conn:
        if username and age:
            conn.execute("""
            UPDATE users
            SET username = ?, age = ?
            WHERE id = ?""", (username, age, user_id))
        elif username:
            conn.execute("""
            UPDATE users
            SET username = ?
            WHERE id = ?""", (username, user_id))
        elif age:
            conn.execute("""
            UPDATE users
            SET age = ?
            WHERE id = ?""", (age, user_id))

def delete_user(user_id):
    with connect_db() as conn:
        conn.execute("""
        DELETE FROM users
        WHERE id = ?""",(user_id,))

def filter_db():
    with connect_db() as conn:
        # cursor = conn.execute("""
        #     SELECT * FROM users WHERE age >27""")
        # cursor = conn.execute("""
        #     SELECT * FROM users WHERE username LIKE 'I%'""")
        # cursor = conn.execute("""
        #     SELECT * FROM users WHERE age BETWEEN 18 AND 60""") #vozrast ot 18 do 60
        # cursor = conn.execute("""
        #     SELECT * FROM users ORDER BY age ASC""")   #vozrastayuszczaya
        # cursor = conn.execute("""
        #     SELECT * FROM users ORDER BY age DESC LIMIT 2""")    #ubyvayuszczaya
        # cursor = conn.execute("""
        #     SELECT * FROM users WHERE age IS NOT NULL""")    #ubyvayuszczaya
        # cursor = conn.execute("""
        #     SELECT * FROM users WHERE username IN ('Ivan')""")    #usery s odnim imenem
        # cursor = conn.execute("""
        #     SELECT * FROM users OFFSET 2""")    #PROPUSK pervych 2 zapisej
        cursor = conn.execute("""
            SELECT * FROM users WHERE username LIKE 'A%' ORDER BY age ASC LIMIT 3""")
    return cursor.fetchall()

# create_table()
# add_user("John Doe", 25)
# add_user("Ivan", 23)
# print(get_all_users())
# print(get_one_user(2))
# update_user(2, "Anton", 15)
# print(get_one_user(2))
# update_user(2, "Max")
# print(get_one_user(2))
# update_user(2, age = 24)
# print(get_one_user(2))
# add_user("Gry",33)
# add_user("Mas",23)
# add_user("Ola",32)

create_table()
add_user('Ivan', 24)
add_user('Anna', 23)
add_user('Petr', 22)
add_user('Masha', 21)
add_user('Sasha', 2)
add_user('Karen', 22)
add_user('Masha', 21)
add_user('Sasha', 2)
print(get_all_users())
print(get_one_user(1))
update_user(1, age=10)
# delete_user(1)
print(get_all_users())
print(filter_db())

print(filter_db())

#SELECT * FROM users WHERE username LIKE 'A%' ORDER BY age ASC LIMIT 3
#SELECT * FROM users WHERE age < 18 AND age > 60
#SELECT * FROM users WHERE username IS NOT 'Karen' OR 'Arman' OR 'Lilit
#SELECT * FROM users WHERE username LIKE '%e%'
#SELECT * FROM users ORDER BY id DESC LIMIT 5

