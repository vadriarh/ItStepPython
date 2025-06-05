import sqlite3

DB_NAME = ("bd_tgbot.db")

def create_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            telegram_id INTEGER NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        """)

def add_user(username:str, telegram_id:int):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        try:
            conn.execute("""
                INSERT INTO users (username, telegram_id)
                VALUES (?, ?)
            """,(username,telegram_id))
            conn.commit()
        except sqlite3.IntegrityError:
            print(f"Пользователь с ID {telegram_id} уже существует.")
        else:
            print(f"Пользователь {username} с ID {telegram_id} добавлен в базу.")

def get_user(telegram_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor("""
            SELECT * FROM users WHERE telegram_id = ?
            """,(telegram_id,))
        user = cursor.fetchone()
        return {
            "id: ": user[0],
            "username: ":user[1],
            "telegram_id: ":user[2],
            "created at: ":user[3]
        }