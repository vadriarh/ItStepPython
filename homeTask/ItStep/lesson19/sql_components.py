import sqlite3
import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_table():
    try:
        with connect_db() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                type TEXT,             
                amount REAL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
            """)
            return True
    except sqlite3.Error as e:
        print(f"Ошибка создания базы данных {DB_NAME}")
        return None



def add_transaction(user_id: int, type_transaction: str, amount: float, description: str):
    try:
        with connect_db() as conn:
            conn.execute("""
            INSERT INTO transactions (user_id, type, amount, description)
            VALUES (?, ?, ?, ?)
            """, (user_id, type_transaction, amount, description))
            return True
    except sqlite3.Error as e:
        print(f"Ошибка добавления транзакции для пользователя ID{user_id} - {e}")
        return None


def get_history(user_id: int):
    try:
        with connect_db() as conn:
            cursor = conn.execute("""
                SELECT type, amount, description, created_at
                FROM transactions WHERE user_id = ?
                ORDER BY created_at DESC LIMIT 5
            """, (user_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка получения истории для пользователя ID{user_id} - {e}")
        return None


def get_balance(user_id: int):
    result = get_summary_history(user_id)
    if result:
        result["balance"] = result["income"] - result["expense"]
        return result
    else:
        print(f"Ошибка получения баланса для пользователя ID{user_id}")
        return None



def remove_all_transaction(user_id: int):
    try:
        with connect_db() as conn:
            conn.execute("""
                DELETE FROM transactions WHERE user_id = ?
                """, (user_id,))
            return True
    except sqlite3.Error as e:
        print(f"Ошибка удаления записей для пользователя ID{user_id} - {e}")
        return None

def get_summary_history(user_id:int):
    pass