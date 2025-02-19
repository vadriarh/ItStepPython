class IncorrectOperationError(Exception):
    pass


def calculate(num1, operation, num2):
    if (operation == "+"):
        return num1 + num2
    elif (operation == "-"):
        return num1 - num2
    elif (operation == "*"):
        return num1 * num2
    elif (operation == "/"):
        return num1 / num2


try:
    number1 = int(input("Введите 1 число: "))
    number2 = int(input("Введите 2 число: "))
    operation = input("Введите знак операции (+, -, *, /): ")
    if operation not in ["+", "-", "/", "*"]:
        raise IncorrectOperationError
    result = calculate(number1, operation, number2)
except ValueError:
    print("Введеное значение не является числом")
except IncorrectOperationError:
    print("Введенная операция недопустима или не существует")
except ZeroDivisionError:
    print("Ошибка. Деление на 0 недопустимо.")

try:
    print(f"Результат равен {result}.\n"+
          "Расчет закончен.")
except NameError:
    print("Расчет провален.")
