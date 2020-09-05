"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending 
multiple copies of the substring together. You may assume the given string consists of lowercase 
English letters only and its length will not exceed 10000.

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"
Output: False

Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

# # O(n^2)
# # 直接找所有的长度，对于能被 n 整除的长度，计算组合的字符串是否等于 s
# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         n = len(s)
        
#         for l in range(1, n // 2 + 1):
#             if n % l == 0:
#                 currSubStr = s[:l]
#                 if currSubStr * (n // l) == s: return True
                
#         return False
        

# # O(n^2)
# # 如果是 repeat，那结果形式为 PatternPattern，否则为 Pattern1Pattern2
# # 把 s 赋值一份加在后面，变成 PatternPatternPatternPattern 和 Pattern1Pattern2Pattern1Pattern2
# # 只考虑 [1:-1) 的字符串 *atternPatternPatternPatter* 和 *attern1Pattern2Pattern1Pattern*
# # 只要 s 在字符串中就说明是 repeat
# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         return s in (s + s)[1:-1]

# KMP: O(n)
# https://leetcode.com/problems/repeated-substring-pattern/solution/
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 找到 next 数组
        def findNext(s):
            n = len(s)
            nxt = [0 for i in range(n)]
            
            i, j = 1, 0
            while i < n:
                if s[j] == s[i]:
                    nxt[i] = j + 1
                    i += 1
                    j += 1
                else:
                    if j == 0:
                        nxt[i] = 0
                        i += 1
                    else:
                        j = nxt[j - 1]
                        
            return nxt
        
        n = len(s)
        nxt = findNext(s)
        l = nxt[-1]
        return l != 0 and n % (n - l) == 0

