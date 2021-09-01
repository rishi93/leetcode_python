"""
Solution to Leetcode problem 53
 
Maximum Subarray
Return maximum sum of contiguous subarray
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending_here = 0
        max_so_far = -1000000
        for i in range(len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far

solution = Solution()

test_cases = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [1],
    [5, 4, -1, 7, 8],
    [-2, -3, 4, -1, -2, 1, 5, -3],
    [-1]
]

expected_results = [
    6,
    1,
    23,
    7,
    -1
]

solution = Solution()

try:
    for(t, e) in zip(test_cases, expected_results):
        assert solution.maxSubArray(t) == e
except AssertionError:
    print("Failed!")
else:
    print("Success!")