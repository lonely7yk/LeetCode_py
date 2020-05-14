"""
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s. Return the longest happy prefix of s .

Return an empty string if no such prefix exists.

Example 1:

Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
Example 2:

Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
Example 3:

Input: s = "leetcodeleet"
Output: "leet"
Example 4:

Input: s = "a"
Output: ""

Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.
"""

# Brute Force: O(n^2)
# class Solution:
#     def longestPrefix(self, s: str) -> str:
#         n = len(s)
#         maxLen = 0
#         res = ""
#         for i in range(1, n):
#             if s[:i] == s[-i:]:
#                 maxLen = i
#                 res = s[:i]
#
#         return res

# KMP: O(n)
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        if n <= 1: return ""
        kmp = [0 for i in range(n)]

        j = 0
        i = 1

        while i < n:
            if s[i] == s[j]:
                kmp[i] = j + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    kmp[i] = 0
                    i += 1
                else:
                    j = kmp[j - 1]

        return s[:kmp[-1]]

# grid = [[2,4,3],[6,5,2]]
# grid = [[1,2,1],[1,2,1]]
# grid = [[1,1,2]]
# grid = [[1,1,1,1,1,1,3]]
grid = [[2],[2],[2],[2],[2],[2],[6]]
res = Solution().hasValidPath(grid)
print(res)
