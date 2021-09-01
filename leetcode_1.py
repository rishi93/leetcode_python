"""
Solution to Leetcode problem 1

Two sum

Return the indices of two numbers in the array such that they add upto target

Approach:
Straight-forward hashmap to record elements already encountered
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(0, len(nums)):
            curr_element = nums[i]
            remaining_sum = target - curr_element
            if remaining_sum in hashMap:
                return i, hashMap[remaining_sum]
            else:
                hashMap[curr_element] = i

solution = Solution()

result = solution.twoSum([2, 7, 11, 15], 9)
print(result)