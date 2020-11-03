"""
You are given coins of different denominations and a total amount of money amount. Write a function 
to compute the fewest number of coins that you need to make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Example 4:

Input: coins = [1], amount = 1
Output: 1

Example 5:

Input: coins = [1], amount = 2
Output: 2

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""

from typing import List
import functools


# # DFS + memo
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         # @functools.lru_cache(None)
#         def dfs(target, idx):
#             if (target, idx) in memo: return memo[(target, idx)]
#             if idx < 0: return float('inf')
#             if target < 0: return float('inf')
#             if target == 0: return 0
            
#             res = min(dfs(target, idx - 1), 1 + dfs(target - coins[idx], idx))
#             memo[(target, idx)] = res
#             return res
        
#         memo = dict()
#         coins.sort()
#         res = dfs(amount, len(coins) - 1)
#         return res if res != float('inf') else -1

# # DP: O(amount * n) - O(amount * n)
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)
#         dp = [[0 for j in range(amount + 1)] for i in range(n + 1)]
        
#         for j in range(1, amount + 1):
#             dp[0][j] = float('inf')
            
#         for i in range(1, n + 1):
#             for j in range(1, amount + 1):
#                 if j >= coins[i - 1]:
#                     dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
#                 else:
#                     dp[i][j] = dp[i - 1][j]
                    
#         return dp[n][amount] if dp[n][amount] != float('inf') else -1
                   

# DP memory optimization: O(amount * n) - O(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0 for j in range(amount + 1)]
        
        for j in range(1, amount + 1):
            dp[j] = float('inf')
            
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[j] = min(dp[j], 1 + dp[j - coins[i - 1]])
                else:
                    dp[j] = dp[j]
                    
        return dp[amount] if dp[amount] != float('inf') else -1

        
