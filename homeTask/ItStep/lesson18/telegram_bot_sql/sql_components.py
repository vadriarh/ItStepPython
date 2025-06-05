import sqlite3

DB_NAME = "database.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_table_users():
    with connect_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL UNIQUE,
            username TEXT NOT NULL)
        """)


def create_table_notes():
    with connect_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS notes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL,
            content TEXT NOT NULL)
        """)


def create_table_logs():
    with connect_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        """)


def add_user(telegram_id: int, username: str):
    message = f"Пользователь {username} с ID {telegram_id} добавлен в базу."
    logging_message(message)
    with connect_db() as conn:
        try:
            conn.execute("""
                INSERT INTO users (telegram_id, username)
                VALUES (?, ?)
            """, (telegram_id, username))
        except sqlite3.IntegrityError:
            print(f"Пользователь с ID {telegram_id} уже существует.")
        else:
            return message



def add_note(telegram_id: int, note: str):
    message = (f"Добавлена заметка \"{note}\""
               f" для пользователя {telegram_id}")
    logging_message(message)
    with connect_db() as conn:
        conn.execute("""
            INSERT INTO notes (telegram_id, content)
            VALUES (?, ?)
        """, (telegram_id, note))

def show_notes(telegram_id: int):
    message = f"Пользователь {telegram_id} запросил список заметок."
    logging_message(message)
    with connect_db() as conn:
        cursor = conn.execute("""
            SELECT content FROM notes WHERE telegram_id = ?
            """, (telegram_id,))
        return cursor.fetchall()



def remove_notes(telegram_id: int):
    message = f"Пользователь {telegram_id} удалил свои заметки."
    logging_message(message)
    with connect_db() as conn:
        conn.execute("""
        DELETE FROM notes
        WHERE telegram_id = ?""", (telegram_id,))



def logging_message(message: str):
    with connect_db() as conn:
        conn.execute("""
               INSERT INTO logs (message)
               VALUES (?)
           """, (message,))
        print(message)


def get_username(telegram_id):
    with connect_db() as conn:
        cursor = conn.execute("""
            SELECT * FROM users WHERE telegram_id = ?
            """,(telegram_id,))
        user = cursor.fetchone()
        return user[1]