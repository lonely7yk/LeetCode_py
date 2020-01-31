"""
Given a non-negative integer num represented as a string, remove k 
digits from the number so that the new number is the smallest possible.

Note:
- The length of num is less than 10002 and will be ≥ k.
- The given num does not contain any leading zero.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 
1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the 
output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with 
nothing which is 0.
"""

class Solution:
    # Greedy + Stack
    # 先从前往后找，如果前一位比后一位大，则把前一位删除
    # 如果全部入栈后，k仍然大于0，则从栈的尾部删除k位
    # 最后把 0 全去掉就可
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num): return '0'
        
        dq = collections.deque()
        
        for c in num:
            while k != 0 and dq and dq[-1] > c:
                dq.pop()
                k -= 1
            dq.append(c)
            
        while k != 0:
            dq.pop()
            k -= 1
        
        res = ''
        while dq:
            res += dq.popleft()
            
        return res.lstrip('0') or '0'
        
