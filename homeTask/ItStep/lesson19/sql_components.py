import sqlite3
import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_table():
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


def add_transaction(user_id: int, type_transaction: str, amount: float, description: str):
    with connect_db() as conn:
        conn.execute("""
        INSERT INTO transactions (user_id, type, amount, description)
        VALUES (?, ?, ?, ?)
        """, (user_id, type_transaction, amount, description))


def get_history(user_id:int):
    with connect_db() as conn:
        cursor = conn.execute("""
            SELECT type, amount, description, created_at
            FROM transactions WHERE user_id = ?
            ORDER BY created_at DESC LIMIT 5
        """, (user_id,))
        rows = cursor.fetchall()
        result = ""
        if not rows:
            result = "Нет сохранённых транзакций."
        else:
            result = "Последние 5 транзакций:\n"
            for row in rows:
                result += f"{row[3]} - {row[0]}: {row[1]} (Описание: {row[2]})\n"

    return result

def get_balance(user_id:int):
    with connect_db() as conn:
        result = {}
        cursor = conn.cursor()
        cursor.execute("""
            SELECT SUM(amount) FROM transactions WHERE user_id = ? AND type = 'income'
            """, (user_id,))
        result["income"] = cursor.fetchone()[0] or 0

        cursor.execute("""
            SELECT SUM(amount) FROM transactions WHERE user_id = ? AND type = 'expense'
            """, (user_id,))
        result["expense"] = cursor.fetchone()[0] or 0

    result["balance"] = result["income"] - result["expense"]
    return result

def remove_all_transaction(user_id:int):
    try:
        with connect_db() as conn:
            conn.execute("""
                DELETE FROM transactions WHERE user_id = ?
                """, (user_id,))
            return True
    except sqlite3.Error as e:
        print(f"Ошибка удаления записей для пользователя ID{user_id} - {e}")
        return False

