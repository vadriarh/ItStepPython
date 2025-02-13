setFilms=set()
for indexOfFilm in range(5):
    while True:
        setFilms.add(input(f"Введите название {indexOfFilm + 1} фильма: "))
        if len(setFilms) < indexOfFilm + 1:
            print("Этот фильм уже был назван.")
            continue
        break

print(setFilms)