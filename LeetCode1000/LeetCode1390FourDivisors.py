"""
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return 0.

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.

Constraints:

1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5
"""

from typing import List
import math


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def helper(num):
            cnt = 2
            sum_ = 1 + num
            for i in range(2, int(math.sqrt(num) + 1)):
                if num % i == 0:
                    if i == num / i:
                        cnt += 1
                        sum_ += i
                    else:
                        cnt += 2
                        sum_ += (i + num // i)
                    if cnt > 4: return 0

            if cnt < 4: return 0
            return sum_

        res = 0
        for num in nums:
            res += helper(num)

        return res


nums = list(range(1, 11))
res = Solution().sumFourDivisors(nums)
print(res)
