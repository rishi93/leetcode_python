"""
Solution to Leetcode problem 26
Remove duplicates from sorted array

Approach:
Straight-forward
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        # Initial condition
        curr = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[curr]:
                curr += 1
                nums[curr] = nums[i]

        # print(nums) 
        return curr + 1

test_cases = [
    [1, 1, 2],
    [0,0,1,1,1,2,2,3,3,4],
    [0, 1, 2],
    [0],
    [1, 2, 2, 2, 2]
]

expected_results = [
    2,
    5,
    3,
    1,
    2
]

solution = Solution()

try:
    for (test_case, expected_result) in zip(test_cases, expected_results):
        assert solution.removeDuplicates(test_case)  == expected_result
except:
    print("Some test case failed!")
else:
    print("All test cases passed!")