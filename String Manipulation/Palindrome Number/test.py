import unittest
from palindromeNumber import Solution

class TestPalindromeNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(121))

    def test_negative_number(self):
        self.assertFalse(self.solution.isPalindrome(-121))

    def test_not_palindrome(self):
        self.assertFalse(self.solution.isPalindrome(10))

    def test_single_digit(self):
        self.assertTrue(self.solution.isPalindrome(10033001))

    def test_zero(self):
        self.assertTrue(self.solution.isPalindrome(0))

if __name__ == '__main__':
    unittest.main()
