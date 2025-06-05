import sqlite3

DB_NAME = ("database.db")


def connect():
    return sqlite3.connect(DB_NAME)


def create_table_users():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL UNIQUE,
            username TEXT NOT NULL)
        """)


def create_table_notes():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS notes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL,
            content TEXT NOT NULL
        """)


def create_table_logs():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        """)


def add_user(telegram_id: int, username: str):
    with connect() as conn:
        cursor = conn.cursor()
        try:
            conn.execute("""
                INSERT INTO users (telegram_id, username)
                VALUES (?, ?)
            """, (telegram_id, username))
            conn.commit()
        except sqlite3.IntegrityError:
            print(f"Пользователь с ID {telegram_id} уже существует.")
        else:
            print(f"Пользователь {username} с ID {telegram_id} добавлен в базу.")


def add_note(telegram_id: int, note: str):
    with connect() as conn:
        cursor = conn.cursor()
        conn.execute("""
            INSERT INTO notes (telegram_id, note)
            VALUES (?, ?)
        """, (telegram_id, note))
        conn.commit()



def get_user(telegram_id):
    with connect() as conn:
        cursor = conn.cursor("""
            SELECT * FROM users WHERE telegram_id = ?
            """, (telegram_id,))
        user = cursor.fetchone()
        return {
            "id: ": user[0],
            "username: ": user[1],
            "telegram_id: ": user[2],
            "created at: ": user[3]
        }
