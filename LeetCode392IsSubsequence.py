"""
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of the remaining 
characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one 
by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters.
"""

import collections
import bisect

# # DP: O(m * n)   dp[i][j] = dp[i][j - 1] if s[i - 1] == t[j - 1] else dp[i][j - 1] | dp[i - 1][j - 1]
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         m, n = len(s), len(t)
#         dp = [[False for j in range(n + 1)] for i in range(m + 1)]

#         for j in range(n + 1):
#             dp[0][j] = True

#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 dp[i][j] = dp[i][j - 1]
#                 if s[i - 1] == t[j - 1]:
#                     dp[i][j] |= dp[i - 1][j - 1]

#         return dp[m][n]

# # Greedy: O(m + n)
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if len(s) == 0: return True

#         m, n = len(s), len(t)
#         sIdx, tIdx = 0, 0

#         while tIdx < n:
#             if s[sIdx] == t[tIdx]:
#                 sIdx += 1
#                 if sIdx == m: return True

#             tIdx += 1

#         return False


# Follow up: HashMap + BinarySearch
# 先把 t 中所有字母的 idx 按顺序保存在一个字典中，字典的 value 是 list
# 设 nextIdx 表示当前 t 中找到第几个位置，然后对于每一个 s 中的字母，找 t 中对应
# list 中第一个比 nextIdx 大的索引，如果该索引超出 list 长度，则返回 False
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idxMap = collections.defaultdict(list)

        # preprocess time of t: O(n)
        for i in range(len(t)):
            c = t[i]
            idxMap[c].append(i)

        # process time: O(mlogk)
        nextIdx = -1
        for c in s:
            idxs = idxMap[c]
            i = bisect.bisect(idxs, nextIdx)
            if i >= len(idxs): return False
            nextIdx = idxs[i]

        return True



# s = "abc"
# t = "ahbgdc"

s = "axc"
t = "ahbgdc"

res = Solution().isSubsequence(s, t)
print(res)

