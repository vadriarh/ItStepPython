setFilms=set()
for i in range(5):
    while True:
        setFilms.add(input(f"Vvedite nazvanie {i + 1} fil\'ma: "))
        if len(setFilms) < i + 1:
            print("Etot fil\'m uje nazvan")
            continue
        break

print(setFilms)