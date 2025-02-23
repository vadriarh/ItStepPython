def decode(number):
    key = "1234567890ABCDEF"
    result = ""
    while number / 16 > 1:
        result += key[number % 16]
        number = int(number / 16)
    result += key[number % 16 - 1]
    return result[::-1]


print(int(2.6))
print(decode(700))
