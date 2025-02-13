number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
vybor = input("Выберите, что искать: Минимальное/Максимальное/Среднее арифметическое - min/max/avg? :")
if vybor == "min":
    print("Минимальное число = ", min(number1, number2, number3))
elif vybor == "max":
    print("Максимальное число = ", max(number1, number2, number3))
elif vybor == "avg":
    print("Среднее арифметическое = ", (number1 + number2 + number3) / 3)
else:
    print("Неправильный выбор")
