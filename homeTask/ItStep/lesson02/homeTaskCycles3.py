numberOfBegin = int(input("Введите число начала диапазона: "))
numberOfEnd = int(input("Введите число конца диапазона: "))

for i in range(numberOfBegin, numberOfEnd + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)