"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []
 

Constraints:

0 <= nums.length <= 200
-109 <= nums[i] <= 10^9
-109 <= target <= 10^9
"""

from typing import List


# 和 3sum 一样的思路：O(n^3)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                
                t = target - (nums[i] + nums[j])
                left = j + 1
                right = n - 1
                while left < right:
                    s = nums[left] + nums[right]
                    if s < t:
                        left += 1
                    elif s > t:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]: left += 1
                        while left < right and nums[right] == nums[right + 1]: right -= 1
                            
        return res
                
        
