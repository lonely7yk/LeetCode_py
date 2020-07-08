"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

from typing import List

# Two Pointers: 先对 nums 排序，然后对于每一个 num，在 num 后面的 nums 中使用双指针找两个数，使得三个数的和为 0
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()     # 先进行排序
        n = len(nums)
        
        for i in range(n):
            # 如果 num 大于 0，那后面的数都大于 0，就找不到和为 0 的三个数了
            if nums[i] > 0: break
            # 如果 num 和前面一个数一样，则直接跳过
            if i > 0 and nums[i] == nums[i - 1]: continue
            
            left, right = i + 1, n - 1
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                if tmp < 0:
                    left += 1
                elif tmp > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # 跳过重复的数
                    while left < right and nums[left] == nums[left - 1]: left += 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1
        
        return res
        