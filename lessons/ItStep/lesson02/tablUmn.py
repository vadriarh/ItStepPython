# czislo=int(input("Введите число: "))
#
# for i in range(1,11):
#     print(czislo,"*",i,"=",czislo*i)

# haslo = ""
# while (haslo != 123):
#     haslo = input("Vvedite parol\'")
# print("Vhod vipolnen")

# while True:
#     czislo = int(input("Vvedite chislo: "))
#     if czislo == 0:
#         break
# print("END.")

# czislo = int(input("Vvedite chislo: "))
# sum = 0
# for i in range(1, czislo+1):
#     sum+=i
# print("Summa = ", sum)

# sum = 0
# for i in range(5):
#     czislo = int(input("Vvedite chislo: "))
#     sum+=czislo
# print("AVG = ", sum/5)

czislo = int(input("Vvedite chislo: "))
for i in range(2, czislo + 1, 2):
    print(i)
