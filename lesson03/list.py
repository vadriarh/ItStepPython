# name = ["Иван","Мария","Петр","Анна"]
# print(name[1])
# name[1]="Марина"
# print(name[1])
# name.append("Ольга")
# print(name)

# name=["Иван","Мария","Петр"]
# print(name[0],name[2])

# numbers = [1,2,3,4,5]
# for i in range(len(numbers)):
#     print(numbers[i])

# spisok = []
# for index in range(5):
#     spisok.append(int(input("Vvedite czislo: ")))
# print(spisok, ", ", sum(spisok))

# spisok = [1,2,"A",4,5]
# spisok.append(6)
# spisok.pop()
# spisok.pop(0)
# spisok.remove("A")
# spisok.sort()
# spisok.reverse()
# spisok.insert(2,8)

# spisok = []
# for index in range(5):
#     spisok.append((input("Vvedite slowo: ")))
# print(spisok)
# spisok.sort()
# print(spisok)
#
# colors = ("Anton","25","POL")
# name, age, country = colors
# print(name)
#
# colors = ("red","green","blue","red")
# print(colors.count("red"))
# print(colors.index("green"))

# colors = ("red","green","blue","red")
# col1,col2,*col_all=colors

# color = {
#     "name": "Anton",
#     "age": 25,
#     "country": "POL"
# }
# print(color.get("name"))
# print(color["name"])

# contacts = {
#     "Andrey": "754448253",
#     "Maksim": "458842215",
#     "Arseniy": "844418685"
# }
# print(contacts["Maksim"])

contacts = {
    "Andrey": "754448253",
    "Maksim": "458842215",
    "Arseniy": "844418685"
}
name = input("Vvedite imya: ")
if contacts.get(name) != None:
    print(contacts[name])
