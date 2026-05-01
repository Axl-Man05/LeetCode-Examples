import unittest
from typing import List
from containsDuplicate2 import Solution

class TestContainsNearbyDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.containsNearbyDuplicate([1, 2, 3, 1], 3))

    def test_example_2(self):
        self.assertTrue(self.solution.containsNearbyDuplicate([1, 0, 1, 1], 1))

    def test_example_3(self):
        self.assertFalse(self.solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))

    def test_empty_list(self):
        self.assertFalse(self.solution.containsNearbyDuplicate([], 0))
        
    def test_k_zero(self):
        self.assertFalse(self.solution.containsNearbyDuplicate([1, 2, 3, 1], 0))

if __name__ == '__main__':
    unittest.main()
