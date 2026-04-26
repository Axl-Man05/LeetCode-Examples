import unittest
from romanToInteger import Solution

class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        # Caso estándar con adición simple
        self.assertEqual(self.sol.romanToInt("III"), 3)

    def test_case_2(self):
        # Caso con mezcla de letras y adición
        self.assertEqual(self.sol.romanToInt("LVIII"), 58)

    def test_case_3(self):
        # Caso complejo con sustracción
        self.assertEqual(self.sol.romanToInt("MCMXCIV"), 1994)

if __name__ == "__main__":
    unittest.main()
