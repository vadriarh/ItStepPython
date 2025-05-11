import sqlite3, random

DB_PATH = "game.db"

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS score (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player TEXT NOT NULL,
            attempts INTEGER NOT NULL
            )""")
    conn.commit()
    conn.close()


def get_best_score(player: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""SELECT MIN(attempts) FROM score
                WHERE  player = ?""", (player,))
    best_score = cursor.fetchone()
    conn.close()
    return best_score[0] if best_score[0] is not None else None


def add_result(player, attempts):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO score (player, attempts) 
        VALUES (?, ?)""", (player, attempts))
    conn.commit()
    conn.close()




def play_game(player):
    best_result = get_best_score(player)
    if best_result:
        print(f"Your best result: {best_result}")
    else:
        print("First time? Good luck!")
    limit_generation = 10
    target_number = random.randint(1, limit_generation)
    result = 0
    while True:
        try:
            input_number = int(input("Input your number: "))
            result+=1
            if target_number == input_number:
                print(f"Congratulations. Your result: {result}.")
                break
            elif target_number>input_number:
                print("Higher. Let's try.")
            else:
                print("Lower. Let's try.")
        except ValueError:
            print("Please, input number.")

    add_result(player, result)
    print(f"Your best result: {get_best_score(player)}")

def main():
    create_table()
    player = input("Input your name: ").strip()
    play_game(player)

if __name__ == "__main__":
    main()
