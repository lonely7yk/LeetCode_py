"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3

Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


# # Stack: O(n)
# class Solution:
#     def calculate(self, s: str) -> int:
#         stack = []
#         curr = 0
#         sign = 1
#         res = 0
        
#         for c in s:
#             if c.isdigit():
#                 curr = curr * 10 + int(c)
#             elif c == "+":
#                 res += sign * curr
#                 curr = 0
#                 sign = 1
#             elif c == "-":
#                 res += sign * curr
#                 curr = 0
#                 sign = -1
#             elif c == "(":
#                 stack.append(res)
#                 stack.append(sign)
#                 res = 0
#                 sign = 1
#             elif c == ")":
#                 res += sign * curr
                
#                 s = stack.pop()
#                 r = stack.pop()
#                 res = r + s * res
#                 curr = 0
#                 sign = 1
                
#         res += sign * curr
#         return res

# Stack 第二种写法
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        sign = 1
        curr = 0
        s = s + " "
        
        for c in s:
            if c.isdigit():
                curr = curr * 10 + int(c)
            else:
                res += sign * curr
                curr = 0
                
                if c == "+":
                    sign = 1
                elif c == "-":
                    sign = -1
                elif c == "(":
                    stack.append(res)
                    stack.append(sign)
                    res = 0
                    sign = 1
                elif c == ")":
                    s = stack.pop()
                    r = stack.pop()
                    res = r + s * res
                    
        return res
                    

        
        
