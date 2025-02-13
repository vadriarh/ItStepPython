# dictStudents = {
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
    studentName = ""
    studentRate = 0
    while True:
        studentName = input("Введите фамилию студента: ")
        if studentName in dictStudents:
            print("Ошибка. Это студент уже записан.")
            continue
        break
    while True:
        studentRate = int(input(f"Введите оценку студента {studentName}: "))
        if 0 < studentRate < 13:
            break
        else:
            print("Ошибка. Оценка выходит за пределы диапазона [1-12].")
            continue
    dictStudents[studentName] = studentRate
maxRating = max(dictStudents.values())
for student in dictStudents.keys():
    if dictStudents.get(student) == maxRating:
        print(student, dictStudents[student])
