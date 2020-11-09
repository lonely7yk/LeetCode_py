"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . 
The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7

Example 2:

Input: " 3/2 "
Output: 1

Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""

# # Two Stack: O(n) - O(n)
# class Solution:
#     def calculate(self, s: str) -> int:
#         def calc(n1, n2, char):
#             if char == "+":
#                 return n1 + n2
#             elif char == "-":
#                 return n1 - n2
#             elif char == "*":
#                 return n1 * n2
#             elif char == "/":
#                 return n1 // n2
                
        
#         prior = {"+": 0, "-": 1, "*": 2, "/": 2}
#         numStack = []
#         charStack = []
#         curr = 0
        
#         for c in s:
#             if c == " ": continue
                
#             if c.isdigit():
#                 curr = curr * 10 + int(c)
#             else:
#                 # 如果前一个符号的优先级大于等于当前符号的优先级，则取出前一个符号和数字，与 curr 进行运算
#                 while charStack and prior[charStack[-1]] >= prior[c]:
#                     char = charStack.pop()
#                     num = numStack.pop()
#                     curr = calc(num, curr, char)
                
#                 numStack.append(curr)
#                 curr = 0
#                 charStack.append(c)
        
#         numStack.append(curr)
        
#         while charStack:
#             char = charStack.pop()
#             n1 = numStack.pop()
#             n2 = numStack.pop()
#             numStack.append(calc(n2, n1, char))
            
#         return numStack[0]


# # Stack: O(n)
# class Solution:
#     def calculate(self, s: str) -> int:
#         sign = "+"
#         stack = []
#         curr = 0
#         s = s + "+"     # 加 "+" 是为了能让结果在循环中就算出来
        
#         for c in s:
#             if c == " ": continue
            
#             if c.isdigit():
#                 curr = curr * 10 + int(c)
#             else:
#                 if sign == "+":
#                     stack.append(curr)
#                 elif sign == "-":
#                     stack.append(-curr)
#                 elif sign == "*":
#                     stack.append(stack.pop() * curr)
#                 elif sign == "/":
#                     # 除法要另外处理，-3//2 == -2
#                     tmp = stack.pop()
#                     if tmp < 0:
#                         stack.append(-(-tmp // curr))
#                     else:
#                         stack.append(tmp // curr)
                    
#                 curr = 0
#                 sign = c
                
#         return sum(stack)


# # Without stack1
# class Solution:
#     def calculate(self, s: str) -> int:
#         sign = "+"
#         curr = 0
#         pre = 0     # 记录上一个数字加到 res 中的数字
#         res = 0
#         s = s + "+"
        
#         for c in s:
#             if c == " ": continue
            
#             if c.isdigit():
#                 curr = curr * 10 + int(c)
#             else:
#                 if sign == "+":
#                     res += curr
#                     pre = curr
#                 elif sign == "-":
#                     res -= curr
#                     pre = -curr
#                 elif sign == "*":
#                     res = res - pre + pre * curr
#                     pre = pre * curr
#                 elif sign == "/":
#                     tmp = 0
#                     if pre < 0:
#                         tmp = -(-pre // curr)
#                     else:
#                         tmp = pre // curr
                        
#                     res = res - pre + tmp
#                     pre = tmp
                    
#                 curr = 0
#                 sign = c
                
#         return res
        
# Without stack2
class Solution:
    def calculate(self, s: str) -> int:
        sign = "+"
        curr = 0    # 当前的数字
        lastNum = 0 # 上一个数字
        res = 0
        s = s + "+"
        
        for c in s:
            if c == " ": continue
            
            if c.isdigit():
                curr = curr * 10 + int(c)
            else:
                if sign == "+":
                    res += lastNum
                    lastNum = curr
                elif sign == "-":
                    res += lastNum
                    lastNum = -curr
                elif sign == "*":
                    lastNum = lastNum * curr
                elif sign == "/":
                    if lastNum < 0:
                        lastNum = -(-lastNum // curr)
                    else:
                        lastNum = lastNum // curr
                    
                curr = 0
                sign = c
                
        return res + lastNum

        
