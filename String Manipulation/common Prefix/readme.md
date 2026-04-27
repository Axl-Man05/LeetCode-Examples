# Longest Common Prefix

## Problem Description
The objective of this exercise is to write a function that finds the longest common prefix string amongst an array of strings. If there is no common prefix, the function should return an empty string.

## Approach
The implemented solution uses a horizontal scanning method:
1. The algorithm initializes the first string in the array as the presumed common prefix.
2. It then iterates through the subsequent strings in the array.
3. During each iteration, it continuously checks if the current string starts with the presumed prefix.
4. If it does not, the prefix is shortened by removing the last character until a match is found.
5. If the prefix becomes empty, the algorithm terminates early and returns an empty string.

## Complexity Analysis
- **Time Complexity:** O(S), where S represents the total number of characters across all strings in the array. In the worst-case scenario, all strings are identical, and the algorithm must examine every character.
- **Space Complexity:** O(1). The algorithm only utilizes constant extra space to store and manipulate the prefix string, without allocating additional proportional memory.
