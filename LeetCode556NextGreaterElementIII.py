"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the
 integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not
 fit in 32-bit integer, return -1.

Example 1:

Input: n = 12
Output: 21

Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 2^31 - 1
"""


# O(n)
# 和 lc031 next permutation 原理是一样的
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        def reverse(digits, start, end):
            while start < end:
                digits[start], digits[end] = digits[end], digits[start]
                start += 1
                end -= 1
        
        digits = [int(c) for c in str(n)]
        num = len(digits)
        # 从后往前找到第一个 digits[idx1 - 1] < digits[idx1] 的位置
        idx1 = 0
        for i in range(num - 1, 0, -1):
            if digits[i - 1] < digits[i]:
                idx1 = i
                break
                
        if idx1 == 0: return -1
        
        # 从后往前找到第一个 digits[idx1 - 1] < digits[idx2] 的位置
        idx2 = 0
        for i in range(num - 1, 0, -1):
            if digits[i] > digits[idx1 - 1]:
                idx2 = i
                break
        
        # swap + reverse
        digits[idx1 - 1], digits[idx2] = digits[idx2], digits[idx1 - 1]
        reverse(digits, idx1, num - 1)
        res = int("".join([str(d) for d in digits]))
        return res if res <= 2 ** 31 - 1 else -1
        
        
