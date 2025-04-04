import re


def reg_ex(input_pattern: str, input_text: str, modification=None):
    if modification is None:
        return re.findall(input_pattern, input_text)
    else:
        return re.findall(input_pattern, input_text, modification)


records = [
    (r"\d+", "У меня 2 яблока и 15 груш."),
    (r"\b[^0-9^ ]\w+[^0-9^ ]\b", "Привет123, мир! Python_rocks 42d 4d2 42"),
    (r"\s+", "Hello world! "),
    (r"^[A-Z]\w+", "Apple is tasty.\nbanana is yellow.", re.MULTILINE),
    (r".*!$", "Это важно!\nНо не всё.\nДа!", re.MULTILINE),
    (r"[@#!]{2,4}", "Hello!!! @#@#!!!"),
    (r"\b(cat|dog)\b", "I love my cat and my dog.")
]

count_tasks = 1
for record in records:
    if len(record) > 2:
        print(f"Task {count_tasks}: {reg_ex(record[0], record[1], record[2])}")
    else:
        print(f"Task {count_tasks}: {reg_ex(record[0], record[1])}")
    count_tasks+=1