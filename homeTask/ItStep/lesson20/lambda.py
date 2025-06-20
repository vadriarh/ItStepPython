from functools import reduce

# Начальный уровень.
# Создай лямбду square, которая возвращает квадрат числа.
# #  Пример: square(5) → 25
# Лямбда is_even, которая проверяет, чётное ли число.
# #  Пример: is_even(4) → True
# Лямбда add, которая возвращает сумму двух чисел.
# #  Пример: add(3, 7) → 10

square = lambda x: x ** 2
print(square(5))
is_even = lambda x: x % 2 == 0
print(is_even(4))
add = lambda x, y: x + y
print(add(3, 7))

# Средний уровень
# Список: [1, 2, 3, 4]
#  Используй map() и lambda, чтобы удвоить каждое число.
# Список: ['hi', 'hello', 'sun', 'python']
#  Используй filter() и lambda, чтобы оставить строки длиной больше 4.
# Список словарей:
# [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
# Отсортируй по возрасту с помощью lambda.

list_numbers = [1, 2, 3, 4]
task4 = list(map(lambda x: x * 2, list_numbers))
print(task4)

list_words = ['hi', 'hello', 'sun', 'python']
task5 = list(filter(lambda x: len(x) > 4, list_words))
print(task5)

dict_people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
task6 = sorted(dict_people, key=lambda x: x['age'])
print(task6)

# Продвинутый уровень
# Лямбда categorize, которая возвращает:
# # “Ребёнок” если < 13
# # “Подросток” если < 18
# # “Взрослый” иначе
# Используй reduce() и lambda, чтобы посчитать сумму чисел из списка: [1, 2, 3, 4, 5]
# Используй reduce() и lambda, чтобы найти максимальное число в списке:

categorize = lambda x: "Подросток" if 13 <= x <= 18 else ("Ребёнок" if x < 13 else "Взрослый")
print(categorize(12))
print(categorize(11))
print(categorize(19))
print(categorize(13))

sum_reduce = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(sum_reduce)

max_reduce = reduce(lambda x, y: x if x > y else y, [12, 5, 31, 7])
print(max_reduce)
