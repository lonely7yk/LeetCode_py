"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

# 40ms 73%
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        num2 = num2.zfill(len(num1))
        n = len(num1)
        res = ""
        flag = 0    # 进位

        for i in range(n):
            c1, c2 = num1[n - 1 - i], num2[n - 1 - i]
            sum_ = int(c1) + int(c2) + flag
            flag = sum_ // 10
            res = str(sum_ % 10) + res
            
        if flag:
            res = "1" + res
            
        return res

num1 = "9"
num2 = "99"
res = Solution().addStrings(num1, num2)
print(res)