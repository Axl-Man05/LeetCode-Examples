# Two Sum Problem

## Problem Description

Given a list of integers named `nums` and a `target` value, the main objective is to find the indices of two numbers in the list that add up to exactly the `target` amount.

## Technical Analysis

For those learning about algorithm performance:

- **Time Complexity:** O(n) - The code only needs to iterate through the array one time. Because of this, it is very fast and efficient.
- **Space Complexity:** O(n) - We are using a dictionary (hash map) to remember the numbers we have already checked. This means the memory used will grow depending on the size of the list.

## File Structure

- `two_sum.py`: Contains the principal logic to resolve the problem.
- `test.py`: Contains a set of unit tests to verify that the program works correctly in different scenarios.

## Usage Instructions

To test the code, open your terminal in this directory and execute the test file with the following command:

```bash
python test.py
```