"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

# # DFS + memo
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         memo = dict()
        
#         def dfs(s):
#             if s in memo: return memo[s]
            
#             if len(s) == 1:
#                 return 0 if s[0] == '0' else 1
            
#             if len(s) == 2:
#                 num = int(s)
#                 res = 0
#                 if 10 <= num <= 26: res += 1
#                 if 1 <= int(s[0]) <= 9 and 1 <= int(s[1]) <= 9: res += 1
#                 return res
            
#             res = 0
#             if 1 <= int(s[0]) <= 9:
#                 res += dfs(s[1:])
            
#             if 10 <= int(s[:2]) <= 26:
#                 res += dfs(s[2:])
                
#             memo[s] = res
                
#             return res
            
#         return dfs(s)

# DP
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1: return 1 if s[0] != '0' else 0

        n = len(s)
        dp = [0 for i in range(n)]

        # 先算出 dp[0] 和 dp[1]
        dp[0] = 1 if s[0] != '0' else 0
        if 10 <= int(s[:2]) <= 26: dp[1] += 1
        if 1 <= int(s[1]) <= 9: dp[1] += dp[0]

        for i in range(2, n):
            if 1 <= int(s[i]) <= 9: dp[i] += dp[i - 1]
            if 10 <= int(s[i-1:i+1]) <= 26: dp[i] += dp[i - 2]

        return dp[-1]

