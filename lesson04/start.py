# numbers = set()
# for index in range(5):
#     numbers.add(int(input(f"Vveddite {index + 1} czislo: ")))
# print(numbers)
#
from string import digits

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1 & set2)  # пересечение
# print(set1 | set2)  # объеденение
# print(set1 - set2)  # разность
# print(set2 - set1)  # разность
# print(set1 ^ set2)  # симметричная разность
# print(set2 ^ set1)  # симметричная разность - обратно пересечению

# friends1 = {"Andrey", "Viktor", "Denis"}
# friends2 = {"Aleksandr", "Viktor", "Oleg"}
# print(f"Obsczie druzjya: {friends1 & friends2}")
#

# def main():
#     print("Hello")
#
#
# def sum(a, b):
#     print(a + b)
#
# sum(5,6)
#
#
# main()
# print(sum(4,5))

# def ifDiv(num):
#     if num%2==0:
#         return "czetnoe"
#     else:
#         return "neczetnoe"
#
# print(f"Czislo est\' {ifDiv(int(input("Vvedite chislo: ")))}")

import calculations


# module.hello_module()
#
# print(module.sum_module(4, 5))
# num1 = 5
# num2 = 6
# print(f"Summa czisel {num1} i {num2} ravna {calculations.sum(num1, num2)}")
# print(f"Raznica czisel {num1} i {num2} ravna {calculations.razn(num1, num2)}")
# print(f"Proizvedenie czisel {num1} i {num2} ravna {calculations.umn(num1, num2)}")
# print(f"Delenie czisel {num1} i {num2} daet {calculations.delen(num1, num2)}")
#
#
# def calculate(num1, operation, num2):
#     if (operation == "+"):
#         return calculations.sum(num1, num2)
#     elif (operation == "-"):
#         return calculations.razn(num1, num2)
#     elif (operation == "*"):
#         return calculations.umn(num1, num2)
#     elif (operation == "/"):
#         return calculations.delen(num1, num2)
#     else:
#         return "Neizvestnaya operacija"
#
#
# print(calculate(int(input("Vvedite 1 czislo: ")), input("Vvedite znak operacii (+,-,*,/): "),
#                 int(input("Vvedite 2 czislo: "))))

# def printNumbers(num):
#     for index in range(1,num+1):
#         print(index)
# number = int(input("Vvedite czislo: "))
# printNumbers(number)

#
# def sumNumbers(num):
#     sum = 0
#     for index in range(1, num + 1):
#         sum += index
#     return sum
#
#
# number = int(input("Vvedite czislo: "))
# print(sumNumbers(number))
#

# def countEven(*args):
#     count = 0
#     for number in args:
#         if number % 2 == 0:
#             count += 1
#     return count
#
#
# print(countEven(5,4,3,2,2,3,56,6))


def unicalNumber(number):
    digitsList = []
    digitsSet = set()
    while number > 1:
        digit = number % 10
        digitsList.append(digit)
        digitsSet.add(digit)
        number = int(number / 10)
    return len(digitsList)==len(digitsSet)


number = 548655
digitsList = []
digitsSet = set()
tempNumber = number
while tempNumber > 1:
    digit=tempNumber%10
    digitsList.append(digit)
    digitsSet.add(digit)
    tempNumber=int(tempNumber/10)


print(digitsList)
print(digitsSet)

print(unicalNumber(4518))
