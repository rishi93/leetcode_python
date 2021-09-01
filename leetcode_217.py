"""
Solution to Leetcode problem 217
Contains duplicate

Approach:
Use set to keep track of elements already encountered
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()
        for i in range(0, len(nums)):
            if nums[i] in unique_set:
                return True
            else:
                unique_set.add(nums[i])
        return False

test_cases = [
    [1, 2, 3, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
]

expected_results = [
    True,
    False,
    True
]

solution = Solution()

try:
    for (test_case, expected_result) in zip(test_cases, expected_results):
        assert solution.containsDuplicate(test_case) == expected_result 
except AssertionError:
    print("Some test case failed!")
else:
    print("All test cases passed!")