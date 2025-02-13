# dictStudents = {    #тестовый словарь из студентов
#     "Иванов": 10,
#     "Петров": 11,
#     "Сидоров": 7,
#     "Кузнецов": 12,
#     "Смирнов": 10,
#     "Попов": 11,
#     "Васильев": 7,
#     "Михайлов": 5,
#     "Новиков": 9,
#     "Фёдоров": 12,
#     "Морозов": 8,
#     "Волков": 8,
#     "Алексеев": 5,
#     "Лебедев": 9
# }

countStudent = int(input("Введите число студентов: "))
dictStudents = {}
for _ in range(countStudent):
    studentSurname = ""
    studentRate = 0
    while True:
        studentSurname = input("Введите фамилию студента: ")
        if studentSurname in dictStudents:
            print("Ошибка. Это студент уже записан.")
            continue
        break
    while True:
        studentRate = int(input(f"Введите оценку студента {studentSurname}: "))
        if 0 < studentRate < 13:
            break
        else:
            print("Ошибка. Оценка выходит за пределы диапазона [1-12].")
            continue
    dictStudents[studentSurname] = studentRate
maxRating = max(dictStudents.values())
print(f"\nСтуденты с максимальным балом [{maxRating}]:")
for student in dictStudents.keys():
    if dictStudents.get(student) == maxRating:
        print(student, dictStudents[student])
