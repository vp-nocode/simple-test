import unittest
from main import mod


class TestMath(unittest.TestCase):
    def test_mod(self):
        self.assertEqual(mod(5, 2), 1)
        self.assertNotEqual(mod(13, 4), 3)
        self.assertEqual(mod(-22, 5), 3)
        self.assertNotEqual(mod(-15, 7), 4)
        self.assertEqual(mod(22, -5), -3)

    def test_mod_by_zero(self):
        self.assertRaises(ValueError, mod, 6, 0)
        self.assertRaises(ValueError, mod, -6, 0)

if __name__ == '__main__':
    unittest.main()
