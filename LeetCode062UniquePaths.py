"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach 
the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

 

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
"""

# # DP: O(mn)-O(mn) dp[i][j] = dp[i-1][j] + dp[i][j-1]
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[0 for j in range(n)] for i in range(m)]
        
#         for i in range(m):
#             dp[i][0] = 1
            
#         for j in range(n):
#             dp[0][j] = 1
            
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
#         return dp[-1][-1]
        

# DP improve: O(mn)-O(n)
# 因为 dp[i][j] 只和 dp[i-1][j] 和 dp[i][j-1] 有关，所以只需要保持一列的数据，dp[j] 就是上一行的 dp[i-1][j]，
# 所以更新当前行的 dp[j] 只需要让 dp[j] += dp[j-1]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0 for j in range(n)]

        for j in range(n):
            dp[j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[-1]
