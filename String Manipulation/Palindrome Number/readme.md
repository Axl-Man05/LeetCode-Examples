# Palindrome Number

## Problem Description

Given an integer `x`, the goal is to determine if it is a palindrome or not. A number is a palindrome if it reads the same from left to right as from right to left. For example, `121` is a palindrome, but `-121` or `10` are not.

## Technical Analysis

- **Time Complexity:** O(n) - The algorithm converts the number into a string, so the time depends on `n`, which is the number of digits.
- **Space Complexity:** O(n) - Converting the number to a string requires extra memory proportional to the number of digits.

## My Initial Solution

My first approach was to convert the number to a string. If the number is negative, I automatically return false, because the minus sign at the beginning prevents it from being a palindrome. 
For the rest of the cases, I use a loop to compare the first character with the last one, the second with the second to last, and so on using reverse indices. If all the characters match at every step, I return true.

I decided to keep my original solution in the code as a personal learning log, so I can see my progress and how my logic evolves over time.

## The Most Efficient Solution (From LeetCode)

After finishing, I checked the best execution times on LeetCode and found a much faster approach. This solution is not mine, but I want to explain what I understood about how it works:

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
```

### How I understand this optimized algorithm:

1. **Discarding negatives:** Just like in my solution, if the number is negative, it cannot be a palindrome and is discarded immediately.
2. **String conversion:** It converts the number to a string and stores it in the variable `s`.
3. **String slicing:** In Python, the syntax `s[::-1]` automatically generates an inverted copy of the string `s`. 
4. **Direct comparison:** By returning `s == s[::-1]`, it evaluates if the original string is identical to its reversed version. If they are exactly the same, the number is a palindrome.

The reason this alternative is faster is because the operation to reverse the string `[::-1]` is executed internally in C (the language Python is built on). This makes it much more efficient than iterating character by character using a manual Python loop like I did.

## File Structure

- `palindromeNumber.py`: Contains the main code with my original logic and the optimized version commented out.
- `test.py`: Contains a set of unit tests to validate the algorithm with different success and failure scenarios.

## Usage Instructions

To test the code, open your terminal in this folder and run the test file with the following command:

```bash
python test.py
```
