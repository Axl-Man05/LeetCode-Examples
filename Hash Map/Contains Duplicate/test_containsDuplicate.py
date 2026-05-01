from typing import List
import pytest
import containsDuplicate
containsDuplicate.List = List
from containsDuplicate import Solution

def test_contains_duplicate_true():
    solution = Solution()
    assert solution.containsDuplicate([1, 2, 3, 1]) == True

def test_contains_duplicate_false():
    solution = Solution()
    assert solution.containsDuplicate([1, 2, 3, 4]) == False

def test_contains_duplicate_multiple():
    solution = Solution()
    assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True

def test_empty_array():
    solution = Solution()
    assert solution.containsDuplicate([]) == False

def test_single_element():
    solution = Solution()
    assert solution.containsDuplicate([1]) == False
