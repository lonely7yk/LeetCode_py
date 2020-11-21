"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""

from typing import List


# Binary Search: Average O(logn)   Worst O(n)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # 等于直接返回 True
            if nums[mid] == target: return True
            
            # 如果 left 和 mid 的值一样，那 left 也不等于 target，我们可以因此缩减 left 的范围
            while left < mid and nums[left] == nums[mid]:
                left += 1
                
            # 如果 left 到 mid 是升序的
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: right = mid - 1
                else: left = mid + 1
            # 如果 mid 到 right 是升序的
            else:
                if nums[mid] < target <= nums[right]: left = mid + 1
                else: right = mid - 1
                    
        return False
        
