import re
#
# text = "I love Python"
# pattern = r"Python"
# match = re.search(pattern, text)
# print(match)
# text = "I love Python, and Python is great"
# pattern = r"Python"
# match = re.search(pattern, text)  # Ищет первое вхождение
# print(match)
# text = "I love Python, and Python is great"
# pattern = r"Python"
# match = re.findall(pattern, text)  # Ищет все совпадения
# print(match)
# match = re.match((pattern, text))  # Ищет совпадения в начале строки
# match = re.sub(pattern, "I hate", text)  # заменяет совпадения
#
# pattern = r"a.c"
# text = "abc, a_c, a-c, a1c, a2d"
# match = re.findall(pattern,text)

# pattern = r"world!$"
# text = "Hello, world!"
# text2 = "Hi, world day"
# pattern = r"cat|dog"
# text = "I have a cat and a dog"
# match = re.findall(pattern, text)
# print(match)
pattern1 = r"b.t"
pattern2 = r"^Python"
pattern3 = r"2025$"
pattern4 = r"[3-7]"
pattern5 = r"Python|Java"

text1 = "abt, b_t, a-c, b1t, a2t"
text2 = "Python is great"
text3 = "Happy New 2025"
text4 = "0123456789"
text5 = "I love Python, and Java is great"

match1 = re.findall(pattern1,text1)
match2 = re.findall(pattern2,text2)
match3 = re.findall(pattern3,text3)
match4 = re.findall(pattern4,text4)
match5 = re.findall(pattern5,text5)

print(match1)
print(match2)
print(match3)
print(match4)
print(match5)