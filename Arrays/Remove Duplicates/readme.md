# Remove Duplicates from Sorted Array

## Problem Description
The objective of this exercise is to remove duplicates in-place from an integer array sorted in non-decreasing order such that each unique element appears only once. The relative order of the elements should be kept the same. The function must return the number of unique elements in the array.

## Approach
The implemented solution uses a two-pointer approach:
1. A slow pointer `k` is initialized to 0, representing the index of the last unique element found.
2. A fast pointer `i` iterates through the array starting from the second element (index 1).
3. During each iteration, the algorithm compares the current element `nums[i]` with the last unique element `nums[k]`.
4. If they are different, it means a new unique element has been found. The pointer `k` is incremented, and the new element is placed at `nums[k]`.
5. Finally, the function returns `k + 1`, which represents the total number of unique elements in the modified array.

## Complexity Analysis
- **Time Complexity:** O(N), where N is the number of elements in the array. The array is traversed only once.
- **Space Complexity:** O(1). The algorithm operates in-place and only requires constant extra space for the pointers.
