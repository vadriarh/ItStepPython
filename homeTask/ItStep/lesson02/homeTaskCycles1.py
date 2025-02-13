numberOfBegin = int(input("Введите число начала диапазона: "))
numberOfEnd = int(input("Введите число конца диапазона: "))

for i in range(numberOfBegin, numberOfEnd + 1):
    if i % 7 == 0:
        print(i)
