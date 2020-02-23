"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

class Solution:
    # HashMap: O(n) 28ms 82%
    def longestPalindrome(self, s: str) -> int:
        dp = {}
        for c in s:
            if c not in dp:
                dp[c] = 1
            else:
                dp[c] += 1
                
        length = 0
        left = False
        
        for c in dp:
            while dp[c] >= 2:
                dp[c] -= 2
                length += 2
                
            if dp[c] == 1:
                left = True
                
        if left:
            length = length + 1
            
        return length
        
