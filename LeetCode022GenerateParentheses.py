"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

from typing import List

class Solution:
    # DFS backtracking: 32ms 72%
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(curr, res, leftNotMatch, leftNotUse, n):
            """ 
            leftNotMatch: 在 curr 中未匹配的左括号 
            leftNotUse: 还可以使用多少个左括号
            n: 2 * n 为括号总数
            """
            if len(curr) == 2 * n:
                res.append(curr)
                return

            if leftNotMatch > 0:
                dfs(curr + ')', res, leftNotMatch - 1, leftNotUse, n)

            if leftNotUse > 0:
                dfs(curr + '(', res, leftNotMatch + 1, leftNotUse - 1, n)

        res = []
        curr = ''
        dfs(curr, res, 0, n, n)
        return res

if __name__ == '__main__':
    n = 3

    res = Solution().generateParenthesis(n)
    print(res)