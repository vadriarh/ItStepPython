# import random
# print(random.randint(1,100))

# try:
#     name = input("Vvedite imya: ")
#     age = int(input("Vvedite vozrast: "))
#     with open("data.txt", "a+") as file:
#         file.write(f"Imja {name} i vozrast {age}\n")
#     with open("data.txt","r") as file:
#         print(file.read())
# except ValueError:
#     print("Vozrast - eto czislo")

# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Na 0 delit nelzya"
#
# print(divide(5,0))

# import random
#
# targetNumber = random.randint(1, 10)
# while True:
#     try:
#         inputNumber = int(input("Ugadaj czislo ot 1 do 10: "))
#         if inputNumber in range(1, 11):
#             if inputNumber == targetNumber:
#                 print("Ty ugadal.")
#                 break
#             else:
#                 print("Uvy. Ty nie ugadal.")
#         else:
#             print("Czislo doljno byt ot 1 do 10")
#     except ValueError:
#         print("Ty vvel nie czislo")
#
# print("Konec igry.")
#
# numbersLine = input("Vvedite czisla czerez probel: ")
# numberList = map(int,)
# for i in range(len(numbersLine.split())):
#     numberList.append(int(numbersLine.split()[i]))
# print(numberList)
# numberTuple = tuple(numberList)
# print(numberTuple)
# summa = sum(numberTuple)


# print(sum(tuple(map(int,input("Vvedite czisla czerez probel: ").split()))))

# i = ["1"," ","2"]
# c = map(int, i.split(" "))
# print(list(c))

# i = tuple(map())

# try:
#     with open("data.txt","r") as file:
#         print("Fail otkryt.")
#         print(f"Koliczestvo strok ravno {len(file.readlines())}")
# except FileNotFoundError:
#     print("Error. Net faila")

str = input("Vvedite stroku: ")
print(str.strip().replace(","," ").capitalize())
