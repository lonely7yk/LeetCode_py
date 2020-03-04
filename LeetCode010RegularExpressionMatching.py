"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

class Solution:
    # DP: O(n^2) 56ms 52%
    # reference: https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(p), len(s)
        dp = [[False for j in range(n + 1)] for i in range(m + 1)]
        dp[0][0] = True
        
        for i in range(1, m + 1):
            if p[i - 1] == "*":
                dp[i][0] = dp[i - 2][0]
                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == "*":
                    if p[i - 2] == s[j - 1] or p[i - 2] == ".":
                        dp[i][j] = dp[i - 2][j] or dp[i - 1][j] or dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 2][j]
                        
        return dp[-1][-1]
        
s = "mississippi"
p = "mis*is*p*."
res = Solution().isMatch(s, p)
print(res)
