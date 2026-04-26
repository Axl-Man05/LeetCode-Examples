# Roman to Integer Problem

## Problem Description

Given a string `s` that represents a Roman numeral, the main objective is to convert it to an integer number. Roman numerals are usually written from largest to smallest, but sometimes a smaller numeral appears before a larger one to indicate subtraction.

## Technical Analysis

For those learning about algorithm performance:

- **Time Complexity:** O(n) - The code iterates through the characters of the string one time, where `n` is the length of the string. This makes it very fast and efficient.
- **Space Complexity:** O(1) - We are using a dictionary (hash map) to store the Roman numeral values, but its size is constant (only 7 symbols). Therefore, the memory used does not grow with the size of the input string.

## File Structure

- `romanToInteger.py`: Contains the principal logic to resolve the problem.
- `test.py`: Contains a set of unit tests to verify that the program works correctly in different scenarios.

## Usage Instructions

To test the code, open your terminal in this directory and execute the test file with the following command:

```bash
python test.py
```
