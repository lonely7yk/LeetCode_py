"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add 
binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
"""

from typing import List

class Solution:
    # DFS: 728ms 80%
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(curr, res, num, target, currTotal, lastNum):
            if not num:
                if currTotal == target:
                    res.append(curr)
                    return

            for i in range(1, len(num) + 1):
                pre = num[:i]
                left = num[i:]
                val = int(pre)

                if not curr:
                    dfs(pre, res, left, target, val, val)
                else:
                    dfs(curr + "+" + pre, res, left, target, currTotal + val, val)
                    dfs(curr + "-" + pre, res, left, target, currTotal - val, -val)
                    dfs(curr + "*" + pre, res, left, target, currTotal - lastNum + lastNum * val, lastNum * val)

                if num[0] == '0': break # 第一个是 0 只遍历一次

        if not num: return []

        res = []
        dfs("", res, num, target, 0, 0)

        return res

if __name__ == '__main__':
    num = "123"
    target = 6
    res = Solution().addOperators(num, target)
    print(res)



