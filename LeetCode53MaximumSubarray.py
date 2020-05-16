"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide 
and conquer approach, which is more subtle.
"""

from typing import List

# # O(n) : greedy
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         currSum = 0
#         maxSum = float('-inf')

#         for num in nums:
#             currSum += num
#             if currSum > maxSum: maxSum = currSum
#             if currSum < 0: currSum = 0

#         return maxSum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = 0
        maxSum = float('-inf')
        for num in nums:
            currMax = max(currMax + num, num)
            maxSum = max(currMax, maxSum)

        return maxSum


nums = [-2,1,-3,4,-1,2,1,-5,4]
res = Solution().maxSubArray(nums)
print(res)
