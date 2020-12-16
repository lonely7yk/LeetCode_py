"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each 
number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
"""

from typing import List


# Two Pointer: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums: return []
        
        res = []
        n = len(nums)
        posIdx = 0
        while posIdx < n:
            if nums[posIdx] > 0:
                break
            posIdx += 1
            
        if posIdx == 0:
            return [nums[i] ** 2 for i in range(n)]
        if posIdx == n:
            return [nums[i] ** 2 for i in range(n - 1, -1, -1)]
        
        idx1, idx2 = posIdx - 1, posIdx
        while idx1 >= 0 and idx2 < n:
            if -nums[idx1] < nums[idx2]:
                res.append(nums[idx1] ** 2)
                idx1 -= 1
            else:
                res.append(nums[idx2] ** 2)
                idx2 += 1
                
        res.extend([nums[i] ** 2 for i in range(idx1, -1, -1)])
        res.extend([nums[i] ** 2 for i in range(idx2, n)])
        
        return res
        
