"""
Given an array of size n, find the majority element. The majority element is the element that 
appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

from typing import List
import collections

# # hashmap: O(n)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         cntMap = collections.defaultdict(lambda : 0)
#         n = len(nums)

#         for num in nums:
#             cntMap[num] += 1
#             if cntMap[num] > n // 2: return num

#         return -1

# moore voting: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        res = -1

        for num in nums:
            if num == res:
                cnt += 1
            elif cnt == 0:
                res = num
                cnt = 1
            else:
                cnt -= 1

        return res


nums = [2,2,1,1,1,2,2]
res = Solution().majorityElement(nums)
print(res)
