"""
Given an array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]

Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]

Note:

2 <= nums.length <= 30000
0 <= nums[i] <= 10^6
It is guaranteed there is at least one way to partition nums as described.
"""

from typing import List


# # O(n) - O(n)
# class Solution:
#     def partitionDisjoint(self, nums: List[int]) -> int:
#         n = len(nums)
#         left_max = [0 for i in range(n)]
#         right_min = [0 for i in range(n)]
        
#         left_max[0] = nums[0]
#         right_min[n - 1] = nums[n - 1]
        
#         for i in range(1, n):
#             left_max[i] = max(left_max[i - 1], nums[i])
        
#         for i in range(n - 2, -1, -1):
#             right_min[i] = min(right_min[i + 1], nums[i])
            
#         for i in range(n - 1):
#             if left_max[i] <= right_min[i + 1]:
#                 return i + 1
            
#         return n - 1     


# O(n) - O(1)
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = nums[0]  # res 长度中的最大值
        all_max = nums[0]   # i+1 长度中的最大值
        res = 1
        
        for i in range(1, len(nums)):
            all_max = max(all_max, nums[i])
            
            if nums[i] < left_max:
                left_max = all_max
                res = i + 1
                
        return res
        

