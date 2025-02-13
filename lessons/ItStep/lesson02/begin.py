# Условия
# bool- true / false - 1/0
# >, <, >=, <=, == (равно), !=(не равно)

# print(15 > 10)
# print(15 > 100)
# print(15 == 15)
# print(15 != 15)
# print(abs(15) == 15)

# if (условие):
age = int(input("Введите свой возраст: "))  # пользователь вводит свой возраст
if age >= 21:
    print("Добро пожаловать в клуб!")
else:
    print("Вам ещё рано!")
print("Конец программы")
answer = int(input("Введите кол ответов: "))
sdore = 0
if answer <= 5:
    score = 1
elif 6 <= answer <= 8:
    score = 2
elif 9 <= answer <= 12:
    score = 3
else:
    pass
