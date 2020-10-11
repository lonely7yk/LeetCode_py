"""
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are 
multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
 

Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
"""


# # Two Pointers
# # https://leetcode.com/problems/minimum-window-subsequence/discuss/109356/JAVA-two-pointer-solution-(12ms-beat-100)-with-explaination
# class Solution:
#     def minWindow(self, S: str, T: str) -> str:
#         sLen, tLen = len(S), len(T)
#         sIdx, tIdx = 0, 0
#         start, minLen = -1, float('inf')
        
#         while sIdx < sLen:
#             if S[sIdx] == T[tIdx]:
#                 tIdx += 1
#                 # check feasibility from left to right
#                 if tIdx == tLen:
#                     end = sIdx + 1
#                     tIdx -= 1
                    
#                     # check optimization from right to left
#                     while tIdx >= 0:
#                         while S[sIdx] != T[tIdx]: sIdx -= 1
#                         sIdx -= 1
#                         tIdx -= 1
#                     sIdx += 1
#                     tIdx += 1
                    
#                     if end - sIdx < minLen:
#                         start = sIdx
#                         minLen = end - sIdx
                        
#             sIdx += 1
            
#         return "" if start == -1 else S[start:start+minLen]
                        
# DP: O(n^2)
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        m, n = len(T), len(S)
        # dp 表示 T[:i] S[:j] 对应的 start index
        dp = [[-1 for j in range(n + 1)] for i in range(m + 1)]

        # 注意这个初始化很重要，dp[0][j] 表示 T 为空的情况，这种情况 S 也要为空，即 S[j:j]
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果 T[i-1] == S[j-1] 那 dp[i][j] 只要取 dp[i-1][j-1]
                # 否则，dp[i][j] 取 dp[i][j-1]
                if T[i - 1] == S[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        start = -1
        minLen = float('inf')
        for j in range(n + 1):
            # 直接找 T[:m] 中有最小长度的 substring
            if dp[m][j] != -1:
                if j - dp[m][j] < minLen:
                    start = dp[m][j]
                    minLen = j - dp[m][j]

        return "" if start == -1 else S[start:start+minLen]

S = "abcdebdde"
T = "bde"
res = Solution().minWindow(S,T)
print(res)
                        
            
        