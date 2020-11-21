"""
Given an array of digits, you can write numbers using each digits[i] as many times as we want.  For example, if 
digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.

Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

Example 2:

Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.

Example 3:

Input: digits = ["7"], n = 8
Output: 1

Constraints:

1 <= digits.length <= 9
digits[i].length == 1
digits[i] is a digit from '1' to '9'.
All the values in digits are unique.
1 <= n <= 10^9
"""

from typing import List


# Binary Search: O(nlogn)
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        def dfs(digits, n):
            # 这边返回 1，因为如果最后一位和 digit 相同，那么还是有一种可能
            if not n: return 1
            
            first = n[0]
            # 用二分搜索找到一个比 first 大的数，那么 idx - 1 就是第一个比 first 小的数
            idx = bisect.bisect_left(digits, first)
            # 对于 idx 前面的数，每个都有 len(digits) ** (len(n) - 1) 种可能
            res = idx * len(digits) ** (len(n) - 1)
            # 如果 digits[idx] == first，那么还要加上 n[1:] 的所有可能性
            if idx < len(digits) and digits[idx] == first:
                res += dfs(digits, n[1:])
            return res
            
        n = str(n)
        digitNum = len(n)
            
        res = 0
        # 先加上所有位数少于 digitNum 的数
        for l in range(1, digitNum):
            res += len(digits) ** l
        digits.sort()
        res += dfs(digits, n)
                
        return res
        
