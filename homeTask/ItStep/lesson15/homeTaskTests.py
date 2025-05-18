import unittest


def is_divisible(a: int, b: int):
    if b == 0:
        print("Can't divide by zero.")
        raise ZeroDivisionError
    if a % b == 0:
        return True
    else:
        return False


def max_of_three(a: int, b: int, c: int):
    return max(a, b, c)


def list_sum(lst: list):
    summa = 0
    if lst:
        for number in lst:
            summa += number
    return summa


def capitalize_words(s: str):
    return s.title()


class TestTaskOperations(unittest.TestCase):
    def test_true_res(self):
        is_divisible(6, 2)

    def test_false_res(self):
        is_divisible(5, 3)

    def test_equal(self):
        with self.assertRaises(ZeroDivisionError):
            is_divisible(6, 0)

        self.assertEqual(max(5, 4, 3), 5)
        self.assertEqual(max(4, 8, 2), 8)
        self.assertEqual(max(3, 6, 9), 9)
        self.assertEqual(list_sum([5, 4, 3]), 12)
        self.assertEqual(list_sum([4, 3, 1]), 8)
        self.assertEqual(list_sum([]), 0)
        self.assertEqual(capitalize_words("i am max"), "I Am Max")
        self.assertEqual(capitalize_words("dsudo per quadro"), "Dsudo Per Quadro")
        self.assertEqual(capitalize_words("aMore teS dIo"), "Amore Tes Dio")

    def test_not_equal(self):
        self.assertNotEqual(max(5, 4, 3), 4)
        self.assertNotEqual(max(8, 4, 7), 7)
        self.assertNotEqual(max(3, 1, 7), 1)
        self.assertNotEqual(list_sum([]), 2)
        self.assertNotEqual(list_sum([]), 2)
        self.assertNotEqual(list_sum([5, 7, 4]), 25)
        self.assertNotEqual(capitalize_words("jerk aser mov"), "jerk Aser mov")
        self.assertNotEqual(capitalize_words("trean tuck of"), "TreaN tuCk oF")


if __name__ == "__main__":
    unittest.main()
