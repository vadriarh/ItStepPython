def factorial(number):  # решение через цикл
    result = number
    while number > 1:
        result = result * (number - 1)
        number -= 1
    return result


def factorialRecursion(number):  # решение через рекурсию
    if number == 1:
        return 1
    return number * factorialRecursion(number - 1)
