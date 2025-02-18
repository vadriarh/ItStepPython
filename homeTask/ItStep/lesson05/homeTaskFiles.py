pathFile = "data.txt"
textNewFile = "Data created."
try:
    with open(pathFile, "r") as file:
        print("File reading")
        print(file.read())
    print("File read.")
except FileNotFoundError:
    print("File not found.")
    print("File creating.")
    with open(pathFile, "w") as file:
        file.write(textNewFile)
    print("File created.")
