number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
operacjya = input("Введите опецию s/p - сумма/произведение: ")

if operacjya == "s":
    print("Suma ravna ", number1 + number2 + number3)
elif operacjya == "p":
    print("Proizvedzenie ravno ", number1 * number2 * number3)
else:
    print("Nepravil\'nyj vybor")

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
vybor = input("Vyberite, czto iskat\': min/max/avg? :")
if vybor == "min":
    print("min = ", min(number1, number2, number3))
elif vybor == "max":
    print("max = ", max(number1, number2, number3))
elif vybor == "avg":
    print("avg = ", sum(number1, number2, number3))
else:
    print("Nepravil\'nyj vybor")

metres = int(input("Введите число метров: "))
vybor = input("Vyberite, vo czto perevodzit\' metry: mili/dziujmy/yardy - m/d/y")
if vybor == "m":
    print()
elif vybor == "d":
    print()
elif vybor == "y":
    print()
else:
    print("Nepravil\'nyj vybor")
