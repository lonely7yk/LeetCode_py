"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""

from typing import List

# Bit Manipulation: O(n)
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxValue = 0    # 当前可以达到的最大结果
        mask = 0

        for i in range(31, -1, -1):
            # 用于取前缀
            mask = mask | 1 << i
            prefixes = set()

            # 得到所有数的前缀，放到 prefixes 中
            for num in nums:
                prefixes.add(num & mask)

            greedyTry = maxValue | 1 << i
            # 确定 prefixes 是否有两个 prefix 的异或结果为 greedyTry，如果是则说明 maxValue 目前可以到达 greedyTry
            for prefix in prefixes:
                # 注意这里，因为有一个公式  a^b=c <==> a^c=b，所以 anotherPrefix 可以用 prefix ^ greedyTry 求出来
                anotherPrefix = prefix ^ greedyTry
                if anotherPrefix in prefixes:
                    maxValue = greedyTry
                    break

        return maxValue


nums = [3, 10, 5, 25, 2, 8]
res = Solution().findMaximumXOR(nums)
print(res)
