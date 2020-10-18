"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some 
characters(can be none) deleted without changing the relative order of the remaining characters. 
(eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings 
is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""

# # 2D-DP: O(mn) - O(mn)
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         m, n = len(text1), len(text2)
#         dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        
#         # dp[i][j] 如果 text1[i-1] == text2[j-1] 那 dp[i][j] = dp[i-1][j-1]
#         # 否则 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if text1[i - 1] == text2[j - 1]:
#                     dp[i][j] = 1 + dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                        
#         return dp[m][n]

# # 1-D DP: O(mn) - O(n)
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         m, n = len(text1), len(text2)
#         dp = [0 for j in range(n + 1)]

#         for i in range(1, m + 1):
#             last = list(dp)
#             for j in range(1, n + 1):
#                 if text1[i - 1] == text2[j - 1]:
#                     dp[j] = 1 + last[j - 1]
#                 else:
#                     dp[j] = max(last[j], dp[j - 1])

#         return dp[n]

# 1-D DP improve
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0 for j in range(n + 1)]

        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                tmp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = tmp  # 保存 dp[i-1][j-1]

        return dp[n]
        
