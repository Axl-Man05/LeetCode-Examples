import unittest
from two_sum import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        # Caso estándar al inicio del arreglo
        self.assertEqual(self.sol.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_case_2(self):
        # Caso con números negativos
        self.assertEqual(self.sol.twoSum([1, -2, 5, 3], 3), [1, 2])

    def test_case_3(self):
        # Caso al final del arreglo
        self.assertEqual(self.sol.twoSum([10, 20, 30, 40], 70), [2, 3])

if __name__ == "__main__":
    unittest.main()