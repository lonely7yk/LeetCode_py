"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]

Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

from typing import List

# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         if not nums or len(nums) <= 1: return nums

#         cnt1, cnt2, candidate1, candidate2 = 0, 0, 0, 1 # 要确保 candidate1 和 candidate2 不等

#         for num in nums:
#             # 1. 判断 num 是否是候选值，如果是，cnt 加1
#             # 2. 判断 cnt 是否为 0，如果是，更新候选值和 cnt
#             # 3. 1 和 2 都不满足，则 cnt 减1
#             if candidate1 == num:
#                 cnt1 += 1
#             elif candidate2 == num:
#                 cnt2 += 1
#             elif cnt1 == 0:
#                 candidate1 = num
#                 cnt1 = 1
#             elif cnt2 == 0:
#                 candidate2 = num
#                 cnt2 = 1
#             else:
#                 cnt1 -= 1
#                 cnt2 -= 1

#         return [x for x in [candidate1, candidate2] if nums.count(x) > len(nums) // 3]


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 = 0
        cnt2 = 0
        last1 = None
        last2 = None
        n = len(nums)
        
        for num in nums:
            if num == last1:
                cnt1 += 1
            elif num == last2:
                cnt2 += 1
            else:
                if cnt1 == 0:
                    last1 = num
                    cnt1 = 1
                elif cnt2 == 0:
                    last2 = num
                    cnt2 = 1
                else:
                    cnt1 -= 1
                    cnt2 -= 1
                    
        return [x for x in [last1, last2] if nums.count(x) > n // 3]


nums = [3,3]
# nums = [1,1,1,3,3,2,2,2]
res = Solution().majorityElement(nums)
print(res)
