import unittest


def add(a, b):
    return a + b


def isEven(number):
    return True if abs(number) % 2 == 0 else False


def reverse_string(string: str):
    if string == "":
        return ""
    return string[::-1]


def factorial(number: int):
    if number == 1:
        return 1
    return number * factorial(number - 1)


def count(string: str):
    result = 0
    for char in string.lower():
        if char in ["a", "e", "i", "o", "u"]:
            result+=1
    return result


class TestMathOperations(unittest.TestCase):
    def test_true_res(self):
        self.assertTrue(add(1, 2))  # a!=b
        self.assertTrue(isEven(4))
        self.assertTrue(isEven(-44))
        self.assertTrue(isEven(56))
        self.assertTrue(isEven(-8))

    def test_false_res(self):
        self.assertFalse(add(1, -1))  # a!=b
        self.assertFalse(isEven(5))  # a!=b
        self.assertFalse(isEven(-11))  # a!=b
        self.assertFalse(isEven(67))  # a!=b
        self.assertFalse(isEven(-55))  # a!=b

    def test_equal(self):
        self.assertEqual(add(1, 2), 3)  # a==b
        self.assertNotEqual(add(1, 2), 5)  # a!=b
        self.assertEqual(reverse_string("hello"), "olleh")  # a!=b
        self.assertNotEqual(reverse_string("hello"), "hello")  # a!=b
        self.assertEqual(factorial(5), 120)  # a!=b
        self.assertNotEqual(factorial(5), 16)  # a!=b
        self.assertEqual(count("hello"),2)  # a!=b
        self.assertEqual(count("MAx"),1)  # a!=b
        self.assertEqual(count("Hmm"),0)  # a!=b
        self.assertNotEqual(count("adrian"),23)  # a!=b
        self.assertNotEqual(count("Max"),2)  # a!=b

        with self.assertRaises(TypeError):
            add("2", 2)


if __name__ == "__main__":
    unittest.main()
