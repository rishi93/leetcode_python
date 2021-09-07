"""
Solution to Leetcode problem 4

Median of two sorted arrays

Return the median of two sorted arrays in O(log(m+n)) time

Approach:
https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
"""

from typing import List

class Solution:
    def isOdd(self, num):
        return num & 1

    def findClassicMedian(self, arr):
        n = len(arr)

        if self.isOdd(n):
            return arr[n//2]
        else:
            return (arr[n//2] + arr[n//2 - 1]) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m == 0:
            return self.findClassicMedian(nums2)
        if n == 0:
            return self.findClassicMedian(nums1)

        # nums1 is the shorter array
        # m is the smaller number
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        leftHalfLength = (m + n + 1) // 2

        # A contributes either 0 or all the elements
        # in the left half
        aMin = 0
        aMax = m

        while aMin <= aMax:
            aCount = aMin + (aMax - aMin) // 2
            bCount = leftHalfLength - aCount

            if aCount > 0 and nums1[aCount-1] > nums2[bCount]:
                aMax = aCount - 1
            elif aCount < m and nums2[bCount-1] > nums1[aCount]:
                aMin = aCount + 1
            else:
                if aCount == 0:
                    leftHalfEnd = nums2[bCount-1]
                elif bCount == 0:
                    leftHalfEnd = nums1[aCount-1]
                else:
                    leftHalfEnd = max(nums1[aCount-1], nums2[bCount-1])
                
                if self.isOdd(m + n):
                    return leftHalfEnd

                else:
                    if aCount == m:
                        rightHalfEnd = nums2[bCount]
                    elif bCount == n:
                        rightHalfEnd = nums1[aCount]
                    else:
                        rightHalfEnd = min(nums1[aCount], nums2[bCount])
    
                    return (leftHalfEnd + rightHalfEnd) / 2




solution = Solution()

# arr1 = [4, 20, 32, 50, 55, 61]
# arr2 = [1, 15, 22, 30, 70]
# arr1 = [1, 3]
# arr2 = [2]
arr1 = [1]
arr2 = [2, 3, 4, 5, 6, 7]
result = solution.findMedianSortedArrays(arr1, arr2)
print(result)