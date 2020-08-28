"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings 
even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
Note:

The input string length won't exceed 1000.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        def count(s, left, right):
            cnt = 0
            
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    cnt += 1
                    left -= 1
                    right += 1
                else:
                    break
                    
            return cnt
        
        res = 0
        n = len(s)
        
        for i in range(n - 1):
            res += count(s, i, i)
            res += count(s, i, i + 1)
            
        return res + 1