"""
Given a non-empty array of integers, every element appears three times except for one, 
which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without 
using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3

Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            cnt = 0

            for num in nums:
                if ((num >> i) & 1) == 1:
                    cnt += 1

            if cnt % 3 != 0:
                res |= (1 << i)

            print(cnt)
            print(bin(res))

        if res >= 2 ** 31:
            res -= 2 ** 32

        return res


nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
res = Solution().singleNumber(nums)
print(res)
