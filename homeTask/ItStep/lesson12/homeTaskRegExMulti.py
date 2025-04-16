import re


def reg_ex(input_pattern: str, input_text: str, modification=None):
    if modification is None:
        return re.findall(input_pattern, input_text)
    else:
        return re.findall(input_pattern, input_text, modification)


records = [
    (r"\d+", "У меня 2 кошки, 1 собака и 12 рыбок."),  # 1 Найти все отдельные цифры.
    (r"\s+", "Hello,   world! How are you?"),  # 2 Найти все пробелы (в том числе подряд идущие).
    (r"[A-Za-z]+", "Python 3.10 is cool!"),  # 3 Найти все слова, состоящие только из букв.
    (r"\d{2,4}", "Вася ввел PIN: 1234, а Петя — 56"),  # 4 Найти все числа длиной от 2 до 4 цифр.
    (r"[A-Z]\w*", "My name is Artur and I love Python")  # 5 Найти все слова, начинающиеся с заглавной буквы.
]

count_tasks = 1
for record in records:
    if len(record) > 2:
        print(f"Task {count_tasks}: {reg_ex(record[0], record[1], record[2])}")
    else:
        print(f"Task {count_tasks}: {reg_ex(record[0], record[1])}")
    count_tasks += 1


