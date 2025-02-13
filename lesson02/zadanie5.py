age = int(input("Введите свой возраст: "))
gender = input("Введите свой пол (m/f): ")

# вариант1 простые условия
# if(gender == 'm'):
#     if age<=14:
#         print("Он мальчик")
#     else:
#         print("Он мужчина")
# else:
#     if age<=14:
#         print("Она девочка")
#     else:
#         print("Она женщина")
#
# вариант2 коибинированные условия
if gender == "m" and age <= 14:
    print("Он мальчик")
elif gender == "m" and age > 14:
    print("Он мужчина")
elif gender == "f" and age <= 14:
    print("Она девочка")
elif gender == "f" and age > 14:
    print("Она женщина")
