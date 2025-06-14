from functools import reduce


def add(a, b):
    return a + b


add_lambda = lambda a, b: a + b


# print(add_lambda(3,7))

# Написать обычную функцию def и лямбда-аналог к ней:
#   • квадрат числа
#   • сумма двух чисел
#   • проверка чётности

def square(number: int):
    return number ** 2


square_lambda = lambda number: number ** 2


def summa(a: int, b: int):
    return a + b


summa_lambda = lambda a, b: a + b


def is_even(number: int):
    return number % 2 == 0


is_even_lambda = lambda number: number % 2 == 0

# print(square(5))
# print(square_lambda(5))
# print(summa(2, 5))
# print(summa_lambda(7, 8))
# print(is_even(8))
# print(is_even_lambda(10))


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x ** 2, nums))
# print(squares)

squares = list(filter(lambda x: x % 2 == 0, nums))  # only True-conditions
# print(squares)

squares = sorted(nums, key=lambda x: x % 2 == 0)
# print(squares)

words = ["apple", "banana", "cherry", "date"]
squares = sorted(words, key=lambda x: len(x))
# print(squares)

# Практика:
#   • Удвоить каждый элемент списка.
#   • Отфильтровать только строки длиной > 4
#   • Отсортировать список словарей по ключу "age"

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

double = list(map(lambda x: x * 2, nums))
len_four = list(filter(lambda x: len(x) > 4, words))
sort_age = sorted(people, key=lambda x: x["age"])

# print(double)
# print(len_four)
# print(sort_age)

nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
# print(product)

# Уровень 1: Базовый синтаксис
#   1.  Остаток от деления на 3
# Напиши lambda, возвращающую остаток от деления числа на 3.
#   2.  Последняя цифра числа
# Сделай lambda, которая возвращает последнюю цифру переданного числа.
# Пример: lambda 247 → 7.
#   3.  Возведение в степень
# Сделай lambda x, y, которая возвращает x в степени y.

task1 = lambda x: x % 3
task2 = lambda x: x - int(x / 10) * 10
task3 = lambda x, y: x ** y
print(task2(247))
print(task2(87))
# Уровень 2: Работа с map и filter
#   4.  Перевод в верхний регистр
# Список: ["hi", "python", "lambda"].
# Используй map + lambda, чтобы сделать все слова заглавными.
#   5.  Оставить только числа > 100
# Список: [120, 55, 133, 98, 200].
# Используй filter + lambda, чтобы оставить только числа больше 100.
#   6.  Список квадратов нечётных чисел
# Список: [1, 2, 3, 4, 5, 6, 7].
# Получи список квадратов только нечётных чисел.

task4 = list(map(lambda x: x.upper(), words))
task5 = list(filter(lambda x: x > 100, nums))
task6 = list(map(lambda x: x ** 2, list(filter(lambda x: x % 2 == 0, nums))))

# Уровень 3: Вложенные структуры и условия
#   7.  Сортировка по длине имени
#
# names = [{"name": "Al"}, {"name": "Barbara"}, {"name": "Joe"}]
#
# Отсортируй по длине имени, используя lambda.
#
#   8.  Добавь префикс к каждому имени
# Список: ["Artur", "Dima", "Karine"].
# Используй map + lambda, чтобы получить: ["Mr. Artur", "Mr. Dima", ...]
#   9.  Словарь: ключ — имя, значение — длина
#
names = ["Anna", "Leon", "Mikhail"]
#
# Преобразуй в список словарей:
# [{name: "Anna", length: 4}, ...] — с помощью map + lambda.

# task7 = sorted(names, key=lambda x: len(x["name"]))
task8 = list(map(lambda x: "Mr. " + x, names))
task9 = list(map(lambda x: {"name": x, "length": len(x)}, names))

# Уровень 4: Комбинации, reduce, условные lambda
#   10.  Сокращение имён до инициалов
#
names = ["Ivan Ivanov", "Sergey Petrov", "Anna Sidorova"]
#
# Преобразуй в формат I.I., S.P., A.S. — через map + lambda.
#
#   11.  Сумма всех чисел в строках
#
data = ["2", "5", "13", "7"]
#
# Преобразуй в int и найди сумму с помощью reduce.
#
#   12.  Lambda с вложенным условием
# Напиши лямбду, которая:
#   •  Если число > 10 и чётное → “big even”
#   •  Если > 10 и нечётное → “big odd”
#   •  Иначе → “small”
'ass'.strip()
task10 = list(map(lambda x: f"{x.split()[0][0]}.{x.split()[1][0]}.", names))
task11 = reduce(lambda x, y: x + y, map(int, data))
task12 = lambda x: "big " + ("even" if x % 2 == 0 else "odd") if x > 10 else "small"
print(task10)
print(task11)
print(task12(5))
print(task12(15))
print(task12(12))
