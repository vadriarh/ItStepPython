metres = int(input("Введите число метров: "))
vybor = input("Выберите, во что переводить метры: мили/дюймы/ярды - m/d/y: ")
if vybor == "m":
    print("Растояние", metres, "в милях равно", metres * 0.00062137, "миль.")
elif vybor == "d":
    print("Растояние", metres, "в дюймах равно", metres * 39.3701, "дюймов.")
elif vybor == "y":
    print("Растояние", metres, "в ярдах равно", metres * 1.09361, "ярдов.")
else:
    print("Неправильный выбор")
