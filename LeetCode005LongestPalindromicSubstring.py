"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum 
length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    # # brute force: O(n^2) TLE
    # def longestPalindrome(self, s: str) -> str:
    #     def isPalindrome(s):
    #         for i in range(len(s) // 2):
    #             if s[i] != s[len(s) - 1 - i]: return False

    #         return True

    #     for length in reversed(range(1, len(s) + 1)):
    #         for i in range(0, len(s) - length + 1):
    #             if isPalindrome(s[i : i + length - 1]):
    #                 return length

    #     return 0

    # # O(n^2) 916ms 86%
    # def longestPalindrome(self, s: str) -> str:
    #     def findPalindrome(s, i, j):
    #         while i >= 0 and j < len(s) and s[i] == s[j]:
    #             i -= 1
    #             j += 1

    #         return s[i+1:j]

    #     res = ""
    #     for i in range(len(s)):
    #         tmp = findPalindrome(s, i, i)
    #         if len(tmp) > len(res):
    #             res = tmp

    #         tmp = findPalindrome(s, i, i + 1)
    #         if len(tmp) > len(res):
    #             res = tmp

    #     return res

    # manacher: O(n) 84ms 96%
    # reference: https://zhuanlan.zhihu.com/p/70532099
    def longestPalindrome(self, s: str) -> str:
        def processStr(s):
            if len(s) == 0: return "^$"

            res = "^"
            for c in s:
                res += "#" + c

            res += "#$"
            return res

        C = 0
        R = 0
        T = processStr(s)
        P = [0 for i in range(len(T))]
        maxP = 0
        maxPIndex = -1

        for i in range(1, len(T) - 1):
            iMirror = 2 * C - i;
            if R > i:
                P[i] = min(R - i, P[iMirror])
            else:
                P[i] = 0

            while T[i - 1 - P[i]] == T[i + 1 + P[i]]:
                P[i] += 1

            # 找到最大的 P[i] 和其对应的索引
            if P[i] > maxP:
                maxP = P[i]
                maxPIndex = i

            if i + P[i] > R:
                C = i
                R = i + P[i]

        length = maxP
        start = (maxPIndex - maxP) // 2
        return s[start:start+length]





