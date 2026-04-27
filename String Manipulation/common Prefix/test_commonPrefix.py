import unittest
from typing import List
from commonPrefix import Solution

class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_common_prefix(self):
        """Test with an array containing a standard common prefix."""
        strs = ["flower", "flow", "flight"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "fl")

    def test_no_common_prefix(self):
        """Test with an array where strings have no common prefix."""
        strs = ["dog", "racecar", "car"]
        # Note: The current implementation might return " " instead of "". 
        # The standard LeetCode expected output is an empty string "".
        self.assertEqual(self.solution.longestCommonPrefix(strs), "")

    def test_empty_list(self):
        """Test with an empty array."""
        strs: List[str] = []
        self.assertEqual(self.solution.longestCommonPrefix(strs), " ")

    def test_single_string(self):
        """Test with an array containing a single string."""
        strs = ["single"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "single")

    def test_identical_strings(self):
        """Test with an array where all strings are identical."""
        strs = ["test", "test", "test"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "test")

if __name__ == '__main__':
    unittest.main()
