fruits = ["яблоко", "банан", "яблоко", "груша", "банан", "яблоко"]
dictOfFruits = {}
for fruit in fruits:
    if fruit in dictOfFruits:
        dictOfFruits[fruit] += 1
    else:
        dictOfFruits[fruit] = 1
print(dictOfFruits)
