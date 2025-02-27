class Student:
    def __init__(self, name, age, listOfGrades ):
        self.name = name
        self.age = age
        self.listOfGrades = list(listOfGrades)

    def add_grade(self,grade):
        self.listOfGrades.append(grade)

    def average_grade(self):
        return round(sum(self.listOfGrades)/len(self.listOfGrades),2)

# Test Data
# st1 = Student("Anton", 21, [7, 9, 6, 8, 9, 8])
# print(st1.name)
# print(st1.age)
# print(st1.listOfGrades)
# print(st1.average_grade())
# st1.add_grade(9)
# print(st1.listOfGrades)
# print(st1.average_grade())