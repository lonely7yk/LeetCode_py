"""
You are given coins of different denominations and a total amount of money. Write 
a function to compute the number of combinations that make up that amount. You may 
assume that you have infinite number of each kind of coin.

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10] 
Output: 1

Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
"""

from typing import List
import collections

# # DFS + memo: O(n^2) 5%
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         memo = [[-1 for j in range(len(coins) + 1)] for i in range(amount + 1)]

#         def dfs(target, leftCoins):
#             if target == 0: return 1
#             if not leftCoins: return 0

#             if memo[target][len(leftCoins)] != -1:
#                 return memo[target][len(leftCoins)]

#             last = leftCoins[-1]
#             res = 0
#             i = 0
#             while i * last <= target:
#                 res += dfs(target - i * last, leftCoins[:-1])
#                 i += 1

#             memo[target][len(leftCoins)] = res

#             return res

#         return dfs(amount, coins)

# # DP: O(n^2)-O(n^2) 60%
# # dp[i][j] 表示只使用前 i 个硬币，有多少种组合使和为 j。
# # 递推关系式：dp[i][j] = dp[i][j - 1] + (dp[i - coins[j - 1]][j] if i >= coins[j - 1] else 0)
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         m, n = amount, len(coins)
#         dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

#         for j in range(n + 1):
#             dp[0][j] = 1

#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 dp[i][j] = dp[i][j - 1] + (dp[i - coins[j - 1]][j] if i >= coins[j - 1] else 0)

#         return dp[m][n]

# DP 优化: O(n^2)-O(n) 90%
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]


amount = 500
coins = [1,2,5]
res = Solution().change(amount, coins)
print(res)
