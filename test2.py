import unittest
from main import check

class TestCheck(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(check(6))
        self.assertFalse(not check(220))
        self.assertFalse(check(1))
        self.assertFalse(check(3))
        self.assertTrue(not check(57))


if __name__ == '__main__':
    unittest.main()
