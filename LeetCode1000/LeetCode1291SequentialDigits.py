"""
An integer has sequential digits if and only if each digit in the number 
is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive 
that have sequential digits.

Example 1:

Input: low = 100, high = 300
Output: [123,234]

Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345] 

Constraints:

10 <= low <= high <= 10^9
"""

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def generateNum(curr, count, res, low, high):
            if low <= curr <= high:
                res.append(curr)
            lastDigit = curr % 10
            if lastDigit == 9: return
            
            generateNum(curr % 10 ** (count - 1) * 10 + (lastDigit + 1), count, res, low, high)
            
        
        lowCnt = 0
        tmp = low
        while tmp > 0:
            tmp = tmp // 10
            lowCnt += 1
            
        highCnt = 0
        tmp = high
        while tmp > 0:
            tmp = tmp // 10
            highCnt += 1
            
        res = []
        curr = 0
        for i in range(lowCnt):
            curr = curr * 10 + (i + 1) 
        
        for cnt in range(lowCnt, highCnt + 1):
            generateNum(curr, cnt, res, low, high)
            lastDigit = curr % 10
            if lastDigit == 9: break
            curr = curr * 10 + (lastDigit + 1)
            
        return res
