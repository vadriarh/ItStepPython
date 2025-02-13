number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
operacjya = input("Введите опецию s/p - сумма/произведение: ")

if operacjya == "s":
    print("Сумма равна ", number1 + number2 + number3)
elif operacjya == "p":
    print("Произведение равно ", number1 * number2 * number3)
else:
    print("Неправильный выбор")
