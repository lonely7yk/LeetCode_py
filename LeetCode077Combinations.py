"""
Given two integers n and k, return all possible combinations of k numbers 
out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

from typing import List

class Solution:
    # DFS: O(n^2) 540ms 55%
    def combine(self, n: int, k: int) -> List[List[int]]:
        def findCombinationsDFS(curr, res, idx, n, k):
            if len(curr) == k:
                res.append(list(curr))
                return

            for i in range(idx, n + 1):
                curr.append(i)
                findCombinationsDFS(curr, res, i + 1, n, k)
                curr.pop()

        if n == 0 or k == 0: return []

        curr = []
        res = []
        findCombinationsDFS(curr, res, 1, n, k)

        return res

if __name__ == '__main__':
    n = 4
    k = 2

    res = Solution().combine(n, k)
    print(res)