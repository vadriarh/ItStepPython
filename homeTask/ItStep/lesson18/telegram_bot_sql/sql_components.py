import sqlite3
import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
LIMIT_SLOTS = 20


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_table_users():
    with connect_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL UNIQUE,
            username TEXT NOT NULL,
            slots INTEGER)
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
    bot_message = ""
    with connect_db() as conn:
        try:
            conn.execute("""
                INSERT INTO users (telegram_id, username, slots)
                VALUES (?, ?, ?)
            """, (telegram_id, username, 0))
        except sqlite3.IntegrityError:
            bot_message = f"Пользователь с ID {telegram_id} совершил попытку перерегистрации."
            user_message = f"Вы уже были зарегистрированы под именем {username}."
        else:
            if telegram_id != ADMIN_ID:
                user_message = f"Привет, {username}! Ты зарегистрирован."
            else:
                user_message = f"Привет, {username}. Вам присвоен статус Администратора."
            bot_message = f"Пользователь {username} с ID {telegram_id} добавлен в базу."
    logging_message(bot_message)
    return user_message


def add_note(telegram_id: int, note: str):
    user = get_user(telegram_id)
    if user["slots"] < LIMIT_SLOTS:
        with connect_db() as conn:
            conn.execute("""
               INSERT INTO notes (telegram_id, content)
               VALUES (?, ?)
           """, (telegram_id, note))
        with connect_db() as conn:
            conn.execute("""
                UPDATE users
                SET slots = ?
                WHERE telegram_id = ?
           """, (user["slots"]+1, telegram_id))
        message = f"Добавлена заметка \"{note}\" для пользователя {telegram_id}"
    else:
        message = "Превышен лимит доступных слотов. Необходимо удалить заметки."
    logging_message(message)


def show_notes(telegram_id: int):
    with connect_db() as conn:
        cursor = conn.execute("""
            SELECT content FROM notes WHERE telegram_id = ?
            """, (telegram_id,))
        notes = cursor.fetchall()
    message = f"Пользователь {telegram_id} запросил список заметок."
    logging_message(message)
    return notes


def remove_notes(telegram_id: int):
    with connect_db() as conn:
        conn.execute("""
            DELETE FROM notes
            WHERE telegram_id = ?
        """, (telegram_id,))
    with connect_db() as conn:
        conn.execute("""
            UPDATE users
            SET slots = 0
            WHERE telegram_id = ?
        """, (telegram_id,))
    message = f"Пользователь {telegram_id} удалил свои заметки."
    logging_message(message)


def logging_message(message: str):
    with connect_db() as conn:
        conn.execute("""
               INSERT INTO logs (message)
               VALUES (?)
           """, (message,))
    print(message)


def get_user(telegram_id):
    with connect_db() as conn:
        cursor = conn.execute("""
            SELECT * FROM users WHERE telegram_id = ?
            """, (telegram_id,))
        user = cursor.fetchone()
    return {
        "id": user[0],
        "telegram_id": user[1],
        "username": user[2],
        "slots": user[3]
    }


def search_note(note: str):
    with connect_db() as conn:
        cursor = conn.execute("""
            SELECT telegram_id FROM notes WHERE content = ?
            """, (note,))
        users = cursor.fetchall()
    return users


def get_users():
    with connect_db() as conn:
        cursor = conn.execute("""
            SELECT * FROM users""")
        users = cursor.fetchall()
    return users


def change_limit_slots(new_limit: int):
    global LIMIT_SLOTS
    LIMIT_SLOTS = new_limit
