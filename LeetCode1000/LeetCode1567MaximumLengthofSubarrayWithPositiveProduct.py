"""
Given an array of integers nums, find the maximum length of a subarray where the product of all 
its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.

Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not 
positive.

Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].

Example 4:

Input: nums = [-1,2]
Output: 1

Example 5:

Input: nums = [1,2,3,5,-6,4,0,10]
Output: 4

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List


# # O(n) - O(k)
# class Solution:
#     def getMaxLen(self, nums: List[int]) -> int:
#         if not nums: return 0

#         n = len(nums)

#         start = 0
#         end = 0
#         res = 0

#         while end < n:
#             negPos = []

#             # 找到第一个 0，[start,end) 中的数都为非0，把负数的位置都存到一个 list
#             while end < n and nums[end] != 0:
#                 if nums[end] < 0: negPos.append(end)
#                 end += 1

#             if len(negPos) % 2 == 0:
#                 # 如果负数个数是 2 的倍数，那么 [start,end) 的积一定为正数
#                 res = max(res, end - start)
#             else:
#                 # 如果负数个数不是 2 的倍数，那么结果为 [negPos[0]+1,end) 和 [start,negPos[-1]) 中的较长者
#                 res = max(res, negPos[-1] - start, end - negPos[0] - 1)

#             end += 1
#             start = end

#         return res


# O(n) - O(1)
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)
        negNum = 0
        firstNegIdx = -1
        zeroPos = -1
        res = 0
        
        for i, num in enumerate(nums):
            if num < 0:
                negNum += 1
                # 只找第一个负数出现的位置
                if firstNegIdx < 0: firstNegIdx = i
            
            if num == 0:
                negNum = 0
                firstNegIdx = -1
                zeroPos = i
            else:
                if negNum % 2 == 0:
                    res = max(res, i - zeroPos)
                else:
                    res = max(res, i - firstNegIdx)
                    
        return res
