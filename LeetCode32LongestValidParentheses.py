'''
Given a string containing just the characters '(' and ')', find 
the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

class Solution:
    # # stack: O(n) 36ms 97.4%
    # def longestValidParentheses(self, s: str) -> int:
    #     stack = [0]
    #     maxLen = 0
        
    #     for c in s:
    #         if c == '(':
    #             stack.append(0)
    #         else:
    #             if len(stack) > 1:
    #                 val = stack.pop()
    #                 stack[-1] += (val + 2)
    #                 maxLen = max(maxLen, stack[-1])
    #             else:
    #                 stack = [0]

    #     return maxLen

    # stack: O(n) 40ms 91.84%
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxLen = 0

        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i) # 没有'('配对的话把')'索引加入到stack中
                else:
                    maxLen = max(maxLen, i - stack[-1])

        return maxLen
        

if __name__ == '__main__':
    s = "(()"
    # s = ")()())"
    res = Solution().longestValidParentheses(s)
    print(res)
