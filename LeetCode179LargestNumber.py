"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""

import functools
from typing import List

# # 用 functools.cmp_to_key
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         def cmp(s1, s2):
#             if s1 + s2 > s2 + s1: return -1
#             else: return 1
            
#         numsStr = [str(x) for x in nums]
#         numsStr.sort(key=functools.cmp_to_key(cmp))
#         return "".join(numsStr) if numsStr[0] != "0" else "0"
        

# 使用类来实现 key
class LargerNumberKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numsStr = [str(x) for x in nums]
        numsStr.sort(key=LargerNumberKey)
        return "".join(numsStr) if numsStr[0] != "0" else "0"