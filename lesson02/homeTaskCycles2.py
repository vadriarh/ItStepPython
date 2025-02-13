numberOfBegin = int(input("Введите число начала диапазона: "))
numberOfEnd = int(input("Введите число конца диапазона: "))

print("\n1. Все числа диапазона: ")
for i in range(numberOfBegin, numberOfEnd + 1):
    print(i)

print("\n2. Все числа диапазона в убывающем порядке: ")
for i in range(numberOfEnd, numberOfBegin - 1, -1):
    print(i)

print("\n3. Все числа, кратные 7")
for i in range(numberOfBegin, numberOfEnd + 1):
    if i == 0:
        continue
    if i % 7 == 0:
        print(i)

count = 0
for i in range(numberOfBegin, numberOfEnd + 1):
    if i == 0:
        continue
    if i % 5 == 0:
        count += 1
print("\n4. Чисел, кратных 5 равно", count, "штук.")
