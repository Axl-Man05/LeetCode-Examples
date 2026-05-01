# Contains Duplicate

## Problem Description

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Example 1:
- **Input:** `nums = [1,2,3,1]`
- **Output:** `true`

### Example 2:
- **Input:** `nums = [1,2,3,4]`
- **Output:** `false`

### Example 3:
- **Input:** `nums = [1,1,1,3,3,4,3,2,4,2]`
- **Output:** `true`

## Solution Explanation

The optimal approach utilizes a Hash Set to keep track of the elements we have seen so far as we iterate through the array. 

1. Initialize an empty Hash Set called `seen`.
2. Iterate through each number in `nums`.
3. If the current number is already in `seen`, it means we have found a duplicate. Return `true`.
4. If the current number is not in `seen`, add it to the set and continue.
5. If the loop finishes without finding any duplicates, return `false`.

### Complexity Analysis

- **Time Complexity:** O(n) - We iterate through the array exactly once. Hash Set lookups and insertions take O(1) time on average.
- **Space Complexity:** O(n) - In the worst-case scenario (no duplicates in the array), the Hash Set will store all elements from the array.

## Running Tests

This solution includes a test suite implemented using `pytest` to ensure correctness across multiple edge cases.

To run the tests:
1. Ensure `pytest` is installed:
   ```bash
   pip install pytest
   ```
2. Navigate to the directory containing the code.
3. Run the following command in your terminal:
   ```bash
   pytest test_containsDuplicate.py
   ```
