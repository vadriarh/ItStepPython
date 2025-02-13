# while по условию
# for по счетчику
#
# dist = 10
# while dist > 0:
#     print("distance", dist)
#     dist -= 0.5
# print("robot on finish")

# for i in range(10): #0-9 ot 0 do poslednego ne vklychaja
#     print(i, " step")
# print("finish")
#
# for i in range(1,11):#1-10 ot kakogo do kakogo ne vklychaya poslednij
#     print(i, " step")
# print("finish")
#
# for i in range(2,11,2):#ot kakogo do kakogo s kakim shagom
#     print(i, " step")
# print("finish")
#
# number = int(input("Введите число: "))
# for i in range(1, 10):
#     print(number, "*", i, "=", number * i)

# number = int(input("Введите число от 1 до 50: "))
# if 1<=number<=50:
#     if number % 2 != 0:
#         number+=1
#     for i in range(number,51,2):
#         print(i)
# else:
#     print("ERROR")


number = int(input("Введите число от 1 до 100: "))
step = int(input("Введите шаг: "))
if 1<=number<=100:
    for i in range(number,101,step):
        print(i)
else:
    print("ERROR")


number2=number
while number2<100:
    print(number2)
    number2+=step
print("Pol\'zovatel\' vvel czislo", number)

while number<100:
    print(number)
    number+=step
print("Pol\'zovatel\' vvel czislo", number)