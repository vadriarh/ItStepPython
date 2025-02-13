def factorial(number):
    result = number
    while number > 1:
        result = result * (number - 1)
        number -= 1
    return result


def factorialRecursion(number):
    if number == 1:
        return 1
    result = number * factorialRecursion(number - 1)
    return result
