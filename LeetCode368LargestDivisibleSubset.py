"""
Given a set of distinct positive integers, find the largest subset such 
that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)

Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""

from typing import List

class Solution:
    # # DP: O(n^2) - O(n^2) 940ms 5.03%
    # # 先排序，然后参考 LIS 的 DP 思路做就行
    # # dp 保存的是以 nums[i] 结尾的最长 subset
    # def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    #     if not nums: return []

    #     n = len(nums)
    #     nums.sort()
    #     # dp = [1 for i in range(n)]
    #     dp = [[num] for num in nums]
    #     resIdx = 0

    #     for i in range(1, n):
    #         num = nums[i]

    #         for j in range(i):
    #             # num % nums[j] == 0 的话说明，num 都能整除 nums[j] 前面的数
    #             if num % nums[j] == 0:
    #                 if len(dp[j]) + 1 > len(dp[i]):
    #                     dp[i] = dp[j] + [num]

    #             if len(dp[i]) > len(dp[resIdx]):
    #                 resIdx = i

    #     return dp[resIdx]

    # DP: O(n^2) - O(n) 356ms 77.09%
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []

        nums.sort()
        n = len(nums)
        dp = [1 for i in range(n)]      # 表示以 nums[i] 结尾的最长 subset 的长度
        pre = [-1 for i in range(n)]    # 表示对应 dp[i] 的 nums[i] 的前面接着的元素的索引
        maxIdx = 0
        res = []

        for i in range(1, n):
            num = nums[i]
            for j in range(i):
                if num % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        pre[i] = j

            if dp[i] > dp[maxIdx]:
                maxIdx = i

        idx = maxIdx
        while idx != -1:
            res.append(nums[idx])
            idx = pre[idx]

        return res



if __name__ == '__main__':
    # nums = [1,2,3]
    nums = [1,2,4,8]

    res = Solution().largestDivisibleSubset(nums)
    print(res)

