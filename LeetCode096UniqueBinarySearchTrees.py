"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# # DFS + memo: 对于每一个节点 i 作为定点，其可能的数量 = 其左边所有节点的可能数量 x 其右边所有节点的可能数量
# class Solution:
#     def numTrees(self, n: int) -> int:
#         memo = dict()
        
#         def dfs(n):
#             if n == 0: return 1
#             if n in memo: return memo[n]
            
#             num = 0
#             for i in range(1, n + 1):
#                 leftNum = i - 1
#                 rightNum = n - i
                
#                 num += dfs(leftNum) * dfs(rightNum)
            
#             memo[n] = num
#             return num
        
#         return dfs(n)


# DP: dp[i] = sum{dp[j - 1] * dp[i - j]} for 1 <= j <= i
class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] 表示使用 i 个节点有多少种可能结果
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                # j 为作为顶点的节点，j - 1 为 j 节点左边一共有多少节点，
                # i - j 为 j 节点右边一共有多少节点
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]
