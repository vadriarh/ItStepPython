try:
    num1=int(input("Введите 1 число: "))
    num2=int(input("Введите 2 число: "))
    summa = num1 + num2
except ValueError:
    print("Введеное значение не есть число.")
    print("Расчет сложения ПРЕРВАН")
else:
    print(f"Сумма чисел {num1} и {num2} равна {summa}.")
print("Программа завершена.")