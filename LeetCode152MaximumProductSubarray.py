"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

from typing import List


# Mine: O(n)
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         idx = 0
#         n = len(nums)
#         firstNegProduct = None  # 第一次出现负数的累积的乘积
#         firstNegIdx = -1        # 第一次出现负数的索引
#         res = max(nums)
#         curr = 1
        
#         while idx < n:
#             # 遍历到出现 0
#             while idx < n and nums[idx] != 0:
#                 curr = curr * nums[idx]
#                 res = max(res, curr)
                
#                 # firstNeg 没被赋值，且第一次出现 0
#                 if not firstNeg and nums[idx] < 0:
#                     firstNeg = curr
#                     firstNegIdx = idx
                    
#                 idx += 1
                
#             # 如果 curr < 0，说明上面的遍历过程中有奇数个负数，我们只要再比较一下 [firstNegIdx + 1, idx) 的乘积就可以了
#             # 另外要注意 firstNegIdx 不能等于 idx - 1，否则 [firstNegIdx + 1, idx) 之间没有数
#             if curr < 0 and firstNegIdx != idx - 1:
#                 res = max(res, curr // firstNeg)
                
#             # 下一次遍历，重新初始化
#             curr = 1
#             firstNeg = None
#             firstNegIdx = -1
#             idx += 1
        
#         return res


# https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC%2B%2BPython-it-can-be-more-simple
# O(n)
# 算 nums 的 prefix 和 suffix，然后找两个数组中的最大值
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         nums2 = nums[::-1]

#         for i in range(1, len(nums)):
#             nums[i] *= nums[i - 1] if nums[i - 1] else 1
#             nums2[i] *= nums2[i - 1] if nums2[i - 1] else 1

#         return max(nums + nums2)

# O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxCurr = nums[0]
        minCurr = nums[0]
        maxLast = maxCurr
        minLast = minCurr
        res = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            maxCurr = max(num, num * maxLast, num * minLast)
            minCurr = min(num, num * maxLast, num * minLast)

            maxLast = maxCurr
            minLast = minCurr

            res = max(res, maxCurr)

        return res

