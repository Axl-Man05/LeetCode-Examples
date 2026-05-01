# Contains Duplicate II

## Problem Description
Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

## Approach
This solution uses a sliding window approach with a Hash Set (`seen`).
1. We iterate through the array `nums` while maintaining a set of the elements in our current window of size `k`.
2. If we find an element that is already in the `seen` set, it means we found a duplicate within the distance `k`, so we return `True`.
3. Otherwise, we add the current element to the `seen` set.
4. If the size of the `seen` set exceeds `k`, we remove the oldest element from the set (the one at index `i - k`) to maintain the window size.
5. If the loop finishes without finding any duplicates, we return `False`.

## Complexity Analysis
- **Time Complexity:** $O(N)$ where $N$ is the length of the array. We iterate through the array exactly once, and set operations (add, remove, check existence) take $O(1)$ time on average.
- **Space Complexity:** $O(\min(N, k))$ since the hash set will store at most $k+1$ elements at any given time.
