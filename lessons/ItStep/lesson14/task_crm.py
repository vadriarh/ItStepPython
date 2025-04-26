# Можно добавить задачу(описание + дата дедлайна).
# Можно посмотреть все задачи
# Можно отметить задачу как выполненную.
# Можно удалить задачу.

import sqlite3

db_path = "tasks_list.db"


def connect():
    return sqlite3.connect(db_path)


def create_table():
    with connect() as conn:
        conn.execute("""DROP TABLE IF EXISTS tasks""")
        conn.execute("""CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            is_done BOOLEAN DEFAULT 0,
            deadline DATE
            )""")


def add_task(title: str, deadline: str):
    with connect() as conn:
        conn.execute("""INSERT INTO tasks (title, is_done, deadline)
            VALUES (?,?,?)""", (title, 0, deadline))


# def add_task():
#     with connect() as conn:
#         title = input("")
#         conn.execute("""INSERT INTO tasks (title, is_done, deadline)
#             VALUES (?,?,?)""", (title, 0, deadline))

def show_tasks():
    with connect() as conn:
        return conn.execute("""SELECT * FROM tasks""").fetchall()



def task_completed(task_id: int):
    with connect() as conn:
        conn.execute("""UPDATE tasks 
        SET is_done = 1
        WHERE id = ?""", (task_id,))


def remove_task(task_id: int):
    with connect() as conn:
        conn.execute("""DELETE FROM tasks 
        WHERE id = ?""", (task_id,))


def show_menu():
    print("Menu.")
    print("1. Create task.")
    print("2. Check all tasks.")
    print("3. Mark task as completed.")
    print("4. Remove task.")
    print("5. Quit.")


create_table()

loop = True
choose = 0
print("Welcome in To-Do list.")
while loop:
    show_menu()
    try:
        choose = int(input("Please you choose: "))
    except:
        print(ValueError)
    if choose in range(1, 6):
        if choose == 1:
            add_task(input("Input title: "), input("Input deadline: "))
            print("Task added")
        if choose == 2:
            tasks = show_tasks()
            if tasks:
                for record in tasks:
                    print(f"Task {record[0]}:{record[1]}")
                    print(f"Status: {"C" if record[2] else "Not c"}ompleted")
                    print(f"Deadline:{record[3]}")
                    print()
            else:
                print("No tasks")
        if choose == 3:
            task_completed(int(input("Input ID of task: ")))
            print()
        if choose == 4:
            remove_task(int(input("Input ID of task: ")))
        if choose == 5:
            loop = False
            print("Program exiting.")
    else:
        print("Incorrect choose. Please retry.")

print("Goodbye")
# add_task("Create planogamms","2025-05-26")
# add_task("Create pictures","2025-03-14")
# add_task("Create lessons","2025-07-09")
# show_tasks()
# print()
# task_completed(2)
# show_tasks()
