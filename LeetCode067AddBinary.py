"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxLen = max(len(a), len(b))
        a = a.rjust(maxLen, '0')
        b = b.rjust(maxLen, '0')
        res = ""
        flag = 0
        
        for i in range(maxLen - 1, -1, -1):
            currA = int(a[i])
            currB = int(b[i])
            
            curr = (currA + currB + flag) % 2
            flag = (currA + currB + flag) // 2
            
            res = str(curr) + res
            
        if flag: res = "1" + res
            
        return res
