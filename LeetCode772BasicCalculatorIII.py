"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and
empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Follow up: Could you solve the problem without using built-in library functions.

Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 6-4 / 2 "
Output: 4

Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21

Example 4:

Input: s = "(2+6* 3+5- (3*14/7+2)*5)+3"
Output: -12

Example 5:

Input: s = "0"
Output: 0


Constraints:

1 <= s <= 10^4
s consists of digits, '+', '-', '*', '/', '(', ')' and ' '.
s is a valid expression.
"""


class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        lastNum = 0
        curr = 0
        sign = "+"
        n = len(s)

        i = 0
        while i < n:
            c = s[i]

            if c.isdigit():
                curr = curr * 10 + int(c)
            elif c == "(":
                cnt = 0
                j = i
                while i < n:
                    if s[i] == "(": cnt += 1
                    if s[i] == ")": cnt -= 1

                    if cnt == 0: break
                    i += 1

                curr = self.calculate(s[j + 1:i])

            if c == "+" or c == "-" or c == "*" or c == "/" or i == n - 1:
                if sign == "+":
                    lastNum += curr
                elif sign == "-":
                    lastNum -= curr
                elif sign == "*":
                    lastNum *= curr
                elif sign == "/":
                    if lastNum < 0 and lastNum % curr != 0:
                        lastNum = lastNum // curr + 1
                    else:
                        lastNum //= curr

                if c == "+" or c == "-" or i == n - 1:
                    res += lastNum
                    lastNum = 0

                curr = 0
                sign = c

            i += 1

        return res


s = " 6-4 / 2 "
s = "2*(5+5*2)/3+(6/2+8)"
res = Solution().calculate(s)
print(res)

