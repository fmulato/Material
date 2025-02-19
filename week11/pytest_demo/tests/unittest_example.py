import unittest

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(sub(5, 1), 4)
    def test_mult(self):
        self.assertEqual(mult(5, 1), 5)
        self.assertEqual(mult(2, 3), 6)

if __name__ == '__main__':
    unittest.main()