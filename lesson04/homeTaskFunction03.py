def isPrime(number):
    if number == 0:
        return False  # ноль не является простым числом
    if number == 1:
        return True  # частный случай, 1 при делении на саму себя дает себя же
    for i in range(2, number):  # рассчатриваем только натуральные числа, которые больше 1
        if number % i == 0:
            return False
    return True
