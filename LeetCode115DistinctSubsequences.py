"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of the remaining 
characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3

Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

Example 2:

Input: S = "babgbag", T = "bag"
Output: 5

Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""

class Solution:
    # # DP: O(n^3) 1000ms 5%
    # 画一张表格就能理解了，dp[i][j] 表示匹配到 t 中的第 i 个字母，s 使用第 j 个字母有多少种匹配方法
    # def numDistinct(self, s: str, t: str) -> int:
    #     if len(t) == 0: return 1
    #     if len(s) == 0: return 0

    #     dp = [[0 for j in range(len(s))] for i in range(len(t))]
    #     for i in range(len(s)):
    #         if t[0] == s[i]: dp[0][i] = 1

    #     for i in range(1, len(t)):
    #         for j in range(1, len(s)):
    #             if t[i] == s[j]:
    #                 for k in range(j):
    #                     dp[i][j] += dp[i - 1][k]

    #     res = 0
    #     for j in range(len(s)):
    #         res += dp[len(t) - 1][j]

    #     retrun res

    # DP: O(n^2) 116ms 83.8%
    # 是在上面方法进行的改进，dp[i][j] 表示匹配到 t 中的第 i 个字母，s 使用 [0, j] 个字母有多少种匹配方法
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) == 0: return 1
        if len(s) == 0: return 0

        dp = [[0 for j in range(len(s))] for i in range(len(t))]

        # 第一行
        cnt = 0
        for i in range(len(s)):
            if t[0] == s[i]: 
                cnt += 1
            dp[0][i] = cnt

        for i in range(1, len(t)):
            cnt = 0     # 表示这个字母到目前为止有多少个匹配方法
            for j in range(1, len(s)):
                if t[i] == s[j]:
                    cnt += dp[i - 1][j - 1]
                dp[i][j] = cnt

        return dp[len(t) - 1][len(s) - 1]

    # # DP: O(n^2): 152ms 57%
    # # discuss 中看到的一种写法，本质是一样的，写法更简洁一点
    # def numDistinct(self, s: str, t: str) -> int:
    #     dp = [[0 for j in range(len(s) + 1)] for i in range(len(t) + 1)]

    #     for j in range(len(s) + 1):
    #         dp[0][j] = 1

    #     for i in range(1, len(t) + 1):
    #         for j in range(1, len(s) + 1):
    #             if t[i - 1] == s[j - 1]:
    #                 dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
    #             else:
    #                 dp[i][j] = dp[i][j - 1]

    #     return dp[len(t)][len(s)]


if __name__ == '__main__':
    # S = "rabbbit"
    # T = "rabbit"

    S = "babgbag"
    T = "bag"

    res = Solution().numDistinct(S, T)
    print(res)