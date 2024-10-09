import unittest
from main import divide_zero

class TestDivide(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide_zero(10, 2), 5)
        self.assertEqual(divide_zero(6, 3), 2)
        self.assertEqual(divide_zero(70, 2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide_zero, 6, 0)


if __name__ == '__main__':
    unittest.main()
