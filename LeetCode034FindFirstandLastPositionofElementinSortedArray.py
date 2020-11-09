"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""

from typing import List
import bisect


# # use bisect: O(logn)
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         idx1 = bisect.bisect_left(nums, target)
#         if idx1 >= len(nums) or nums[idx1] != target: return [-1, -1]
        
#         idx2 = bisect.bisect(nums, target)
#         return [idx1, idx2 - 1]
        

# Binary Search: O(logn)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findInsertPos(a, x, toLeft):
            left = 0
            right = len(a)
            
            while left < right:
                mid = (left + right) // 2
                if a[mid] < x:
                    left = mid + 1
                elif a[mid] > x:
                    right = mid
                else:
                    if toLeft: right = mid
                    else: left = mid + 1
                        
            return left
        
        
        idx1 = findInsertPos(nums, target, True)
        if idx1 >= len(nums) or nums[idx1] != target: return [-1, -1]
        
        idx2 = findInsertPos(nums, target, False)
        return [idx1, idx2 - 1]
