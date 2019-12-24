"""
Given an input string (s) and a pattern (p), implement wildcard pattern 
matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

- s could be empty and contains only lowercase letters a-z.
- p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', 
which does not match 'b'.

Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while 
the second '*' matches the substring "dce".

Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""

class Solution:
    # 44ms 97%
    # 参考：https://leetcode.com/problems/wildcard-matching/discuss/17810/Linear-runtime-and-constant-space-solution
    def isMatch(self, s: str, p: str) -> bool:
        spoint, ppoint = 0, 0
        match = 0
        starIdx = -1
        while spoint < len(s):
            if ppoint < len(p) and (p[ppoint] == s[spoint] or p[ppoint] == '?'):
                ppoint += 1
                spoint += 1
            elif ppoint < len(p) and p[ppoint] == '*':
                match = spoint
                starIdx = ppoint
                ppoint += 1
            elif starIdx != -1:
                ppoint = starIdx + 1
                match += 1
                spoint = match
            else:
                return False

        while ppoint < len(p) and p[ppoint] == '*':
            ppoint += 1

        return ppoint == len(p) 

    # # DFS: TLE
    # def isMatch(self, s: str, p: str) -> bool:
    #     return self.helper(s, 0, p, 0)
    #
    # def helper(self, s, spoint, p, ppoint):
    #     if ppoint == len(p):
    #         return spoint == len(s)
    #
    #     if all(x == '*' for x in p[ppoint:]):
    #         return True
    #
    #     while spoint < len(s) and ppoint < len(p):
    #         if p[ppoint] == '*':
    #             while ppoint + 1 < len(p) and p[ppoint + 1] == '*': ppoint += 1
    #             if ppoint == len(p) - 1: return True
    #
    #             nextChar = p[ppoint + 1]
    #             for idx in range(spoint, len(s)):
    #                 if s[idx] == nextChar or nextChar == '?':
    #                     if self.helper(s, idx + 1, p, ppoint + 2):
    #                         return True
    #             return False
    #         else:
    #             if p[ppoint] != '?' and p[ppoint] != s[spoint]: return False
    #
    #             spoint += 1
    #             ppoint += 1
    #
    #     if ppoint != len(p):
    #         return all(x == '*' for x in p[ppoint:])
    #     else:
    #         return spoint == len(s)

if __name__ == '__main__':
    s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
    p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
    res = Solution().isMatch(s, p)
    print(res)
