"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""

from typing import List

# DP: O(n^2)-O(n^2) 分成两组和相等的，则每组的和必定为总和的一半，因此题目可以化简为找到一组数的和为总数的一半即可。
# dp[i][j] 表示对于前 i 个整数，是否能选出一组数的和为 j。
# 对于第 i 个整数(索引是i-1)，如果不选那么 dp[i][j] = dp[i - 1][j]
# 如果选，那么 dp[i][j] = dp[i - 1][j - nums[i-1]]
# 所以递推关系式为：dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i-1]]
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         sum_ = sum(nums)
#         if sum_ % 2 != 0: return False # 所有数的和一定是2的倍数

#         n = len(nums)
#         x = sum_ // 2

#         dp = [[0 for j in range(x + 1)] for i in range(n + 1)]

#         for i in range(n):
#             dp[i][0] = 1

#         for i in range(1, n + 1):
#             for j in range(1, x + 1):
#                 if j - nums[i - 1] < 0:
#                     dp[i][j] = dp[i - 1][j]
#                 else:
#                     dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i - 1]]

#         return dp[n][x] == 1

# 上面 DP 的改进版，O(n^2)-O(n)
# dp[i] 表示是否能存在和为 i 的一组数，
# 对于每一个数 num，从后往前计算 dp[i] = dp[i] | dp[i - num]
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         sum_ = sum(nums)
#         if sum_ % 2 != 0: return False # 所有数的和一定是2的倍数
#         x = sum_ // 2

#         dp = [0 for i in range(x + 1)]
#         dp[0] = 1

#         for num in nums:
#             for i in range(x, num - 1, -1):
#                 dp[i] = dp[i] | dp[i - num]

#         return dp[x] == 1

# Set: O(n^2)-O(n^2) 将所有的和的结果都放在一个集合中，然后判断所有数的和的一半是否在这个集合中
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 != 0: return False # 所有数的和一定是2的倍数
        x = sum_ // 2

        set_ = {0}

        for num in nums:
            tmp = set()
            for val in set_:
                tmp.add(num + val)
            set_.update(tmp)

        return x in set_



nums = [1, 5, 11, 5]
res = Solution().canPartition(nums)
print(res)

