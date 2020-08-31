"""
Given a list of non-negative numbers and a target integer k, write a function to check 
if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, 
that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

Constraints:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""

from typing import List

# # Brute Force: O(n^2) 10%
# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         preSum = [0]
        
#         for num in nums:
#             preSum.append(preSum[-1] + num)
            
#         for i in range(1, len(preSum)):
#             for j in range(i - 1):
#                 curSum = preSum[i] - preSum[j]
#                 if k == 0:
#                     if curSum == 0: return True
#                 else:
#                     if curSum % k == 0: return True
                
#         return False
        
# HashMap: O(n)
# 有点像 Two Sum，map 的 key 为 currSum % k，value 为 currSum % k 第一次出现的索引
# 因为只要出现两次 currSum 位置为 i,j，那么 (i,j] 之间的和一定为 k 的倍数
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderIdxDict = dict()
        remainderIdxDict[0] = -1

        curSum = 0
        for idx, num in enumerate(nums):
            curSum += num
            remainder = curSum % k if k != 0 else curSum
            if remainder not in remainderIdxDict:
                remainderIdxDict[remainder] = idx
            else:
                firstIdx = remainderIdxDict[remainder]
                if idx - firstIdx >= 2: return True # 确保长度大于等于2

        return False

