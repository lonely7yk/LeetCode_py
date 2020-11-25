"""
Given a positive integer K, you need to find the length of the smallest positive integer N such 
that N is divisible by K, and N only contains the digit 1.

Return the length of N. If there is no such N, return -1.

Note: N may not fit in a 64-bit signed integer.

Example 1:

Input: K = 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.

Example 2:

Input: K = 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.

Example 3:

Input: K = 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.

Constraints:

1 <= K <= 10^5
"""


# O(1)
# curr % k == (remainder of curr) % k
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        seen = set()
        remainder = 0   # 这边用 remainder 而不用原始的数是为了减少运算量
        
        # 最多 K 次循环，因为 K 次循环后如果没有 return 或者 break，那么 seen 中的元素为 K 个，下一个 remainder 一定在 seen 中
        for i in range(1, K + 1):
            remainder = (remainder * 10 + 1) % K
            if remainder == 0:
                return i
            
            if remainder in seen:
                break
            else:
                seen.add(remainder)
            
        return -1
        
