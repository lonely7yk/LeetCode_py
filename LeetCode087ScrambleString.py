"""
Given a string s1, we may represent it as a binary tree by partitioning 
it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two 
children.

For example, if we choose the node "gr" and swap its two children, it 
produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", 
it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a 
scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true

Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
"""

class Solution:
    # DFS resursive: O(5^n) 44ms 73%
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        if s1 == s2: return True

        # 判断是否所有字母的个数都是一样的
        map_ = dict()
        for i in range(len(s1)):
            if s1[i] not in map_: map_[s1[i]] = 0
            if s2[i] not in map_: map_[s2[i]] = 0
            map_[s1[i]] += 1
            map_[s2[i]] -= 1

        for key, val in map_.items():
            if val != 0: return False

        f = self.isScramble
        for i in range(1, len(s1)):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
                f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True

        return False

    # # DP: O(n^4) 512ms 5%
    # def isScramble(self, s1: str, s2: str) -> bool:
    #     if len(s1) != len(s2): return False
    #     n = len(s1)
    #     # dp[i][j][k] 表示 s1[i:i+k] 和 s2[j:j+k] 是否为 scramble
    #     # dp = [[[False] * (n + 1)] * n] * n    # 这样创建二维数组会有bug
    #     dp = [[[False for k in range(n + 1)] for i in range(n)] for j in range(n)]
    #
    #
    #     for k in range(1, n + 1):
    #         for i in range(n - k + 1):
    #             for j in range(n - k + 1):
    #                 if k == 1:
    #                     dp[i][j][k] = s1[i] == s2[j]
    #                 else:
    #                     for q in range(1, k):
    #                         if dp[i][j][k]: break
    #                         dp[i][j][k] = (dp[i][j][q] and dp[i + q][j + q][k - q]) or \
    #                                         (dp[i][j + k - q][q] and dp[i + q][j][k - q])
    #
    #     return dp[0][0][n]


if __name__ == '__main__':
    s1 = "ab"
    s2 = "ba"
    # s1 = "abcde"
    # s2 = "caebd"
    res = Solution().isScramble(s1, s2)
    print(res)

