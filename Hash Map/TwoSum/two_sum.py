class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        memory = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in memory:
                return [memory[complement],i]
            memory[num] = i
        return[]