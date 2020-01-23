"""
Given a string s, partition s such that every substring of the partition 
is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

from typing import List

class Solution:
    # # DFS: 112 7.85%
    # def partition(self, s: str) -> List[List[str]]:
    #     def isValid(s):
    #         # 判断回文
    #         return s == s[::-1]

    #     def dfs(curr, res, s):
    #         if not s:
    #             res.append(curr)
    #             return

    #         for i in range(1, len(s) + 1):
    #             if isValid(s[:i]):
    #                 dfs(curr + [s[:i]], res, s[i:])

    #     if not s: return []

    #     curr = []
    #     res = []
    #     dfs(curr, res, s)
    #     return res

    # DP + DFS: 68ms 84.9%
    def partition(self, s: str) -> List[List[str]]:
        def dfs(curr, res, idx, s, dp):
            if idx == len(s):
                res.append(curr)
                return

            for i in range(idx + 1, len(s) + 1):
                if dp[idx][i - 1]:
                    dfs(curr + [s[idx:i]], res, i, s, dp)

        if not s: return []

        n = len(s)
        dp = [[False for j in range(n)] for i in range(n)]

        # for l in range(1, n + 1):
        #     for i in range(n + 1 - l):
        #         if s[i] == s[i + l - 1] and (l <= 2 or dp[i + 1][i + l - 2]):
        #             dp[i][i + l - 1] = True

        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True

        res = []
        curr = []
        dfs(curr, res, 0, s, dp)

        return res


if __name__ == '__main__':
    s = "efe"

    res = Solution().partition(s)
    print(res)

