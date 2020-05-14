"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""

from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(res, start):
            for i in range(10):
                if start + i == 0: continue # exclude 0
                if start + i > n: break
                res.append(start + i)
                dfs(res, (start + i) * 10)

        res = []
        dfs(res, 0)
        return res

res = Solution().lexicalOrder(13)
print(res)
