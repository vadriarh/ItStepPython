import re
text = "test@example.com tresr@ubi.cv"
pattern = r"(\w+)@([\w.]+)"
print(re.findall(pattern,text))

text1 = "eweabba sdgnoonsadu oidsiffia"
pattern1 = r"(.)(.)\2\1"
print(re.findall(pattern1,text1))

text2 = "ab-ba akj aa-aa kfjio asb-dd-dd"
pattern2 = r"(.)\1\-\1\1"
print(re.findall(pattern2,text2))

text3 =  "baaaacaa bbb aa a"
pattern3 = r"a*"
print(re.findall(pattern3,text3))
pattern4 = r"a+"
print(re.findall(pattern4,text3))

text5 =  "ac abc ab a abb"
pattern5 = r"ab?"
print(re.findall(pattern5,text5))

text6 =  "1 12 123 1234 12345"
pattern6 = r"\b\d{3}\b"
print(re.findall(pattern6,text6))

text7 =  "1 12 123 1234 12345"
pattern7 = r"\b\d{2,}\b"
print(re.findall(pattern7,text7))

text8 =  "1 12 123 1234 12345"
pattern8 = r"\b\d{2,4}\b"
print(re.findall(pattern8,text8))

text9 =  "Серверы: 192.168.0.1, 10.1.1.1, 999.999.999.999, test.12.34"
pattern9 = r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
print(re.findall(pattern9,text9))


text10 =  "<div><p>Hello</p></div><h1>"
pattern10 = r"</?\w+>"
print(re.findall(pattern10,text10))

text11 =  "1. Начни здесь\n2. Иди туда\nА вот тут — нет"
pattern11 = r"\d.+$"
print(re.findall(pattern11,text11,re.MULTILINE))

text12 =  "Follow @john_doe, @jane123, @no_underscore_here @wrong!"
pattern12 = r"@\w*_+\w*"
print(re.findall(pattern12,text12))

text13 =  "100 54s 3.14 as4 0.01 15ad5 -25 -as5d22f"
pattern13 = r"-?\b\d+.?\d+\b"
print(re.findall(pattern13,text13))