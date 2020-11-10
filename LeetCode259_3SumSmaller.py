"""
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that 
satisfy the condition nums[i] + nums[j] + nums[k] < target.

Follow up: Could you solve it in O(n^2) runtime?

Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
Example 2:

Input: nums = [], target = 0
Output: 0
Example 3:

Input: nums = [0], target = 0
Output: 0
 

Constraints:

n == nums.length
0 <= n <= 300
-100 <= nums[i] <= 100
-100 <= target <= 100
"""

from typing import List


# O(n^2)
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        
        for i in range(n - 2):
            t = target - nums[i]
            left = i + 1
            right = n - 1
            
            while left < right:
                if nums[left] + nums[right] < t:
                    res += right - left
                    left += 1
                else:
                    right -= 1
                    
        return res
        
