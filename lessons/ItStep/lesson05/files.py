# file = open("text.txt", "r") # r - read, w - write,
# print(file.read())
# print(file.readline())
# print(file.readlines())
# file.close()
#
# file=open("text.txt","w")
# file.write("Hello world!\n")
# file.writelines(["Hello 2world!\n","Hello 3World!\n"])
# file.close()
#
# file=open("text.txt","a")
# file.write("\nHello 2World!")
# file.close()
#
# with open("text.txt", "r") as file:
#     print(file.read())
#
# with open("text.txt", "w") as file:
#     file.write("Hello world!\n")
#     file.writelines(["Hello 2world!\n","Hello 3World!\n"])
#

# with open("output.txt", "w") as file:
#     file.write(input("Vvedite text: "))
#
# with open("output.txt", "r") as file:
#     print(file.read())
#
# with open("output.txt", "r") as file:
#     print(len(file.readlines()))
#
# with open("output.txt", "r") as file:
#     if input("Vvedite slowo: ") in file.read():
#         print("Eto slowo jest")
#     else:
#         print("Etogo slowa net")
#
# with open("source.txt", "r") as fileIn:
#     with open("copy.txt", "w") as fileOut:
#         fileOut.write(fileIn.read())
#
# with open("data.txt", "r") as file:
#     listStrok=file.readlines()
#     for i in range(len(listStrok)):
#         if "python" in listStrok[i].lower():
#             print(listStrok[i],end="")
#
# print("\n")
#
# with open("data.txt", "r") as file:
#     for line in file:
#         if "python" in line.lower():
#             print(line,end="")
#
# try:
#     number = int(input("Vvedite czislo: "))
# except ValueError:
#     print("Errorrrrr")

# class MyError(Exception):
#     pass
# try:
#     i=4
#     if 0>1:
#         raise MyError("Czislo < 0")
#     else:
#         raise MyError("CZislo > 0")
# except MyError as e:
#     print(e)

# try:
#     num1 = int(input("Vvedite 1 czislo: "))
#     num2 = int(input("Vvedite 2 czislo: "))
#     print(f"Resultat raven {num1/num2}")
# except ValueError:
#     print("Vvedeno ne czislo")
# except ZeroDivisionError:
#     print("Delenie na 0 nedopustimo")

class ShortPaswordError(Exception):
    pass

try:
    password = input("Vvedite parol: ")
    if len(password)<6:
        raise ShortPaswordError("Vvedennyi parol korotkij")
except ShortPaswordError as e:
    print("Error.",e)
else:
    print("Vhod vipolnen po paroly ","*"*len(password))