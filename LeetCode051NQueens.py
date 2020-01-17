"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack 
each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both 
indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""

from typing import List

class Solution:
    # DFS: 72 ms 65.18%
    def solveNQueens(self, n: int) -> List[List[str]]:

        def findSolutionsDFS(curr, res, n):
            if len(curr) == n:
                res.append(list(curr))
                return

            line = '.' * n
            canLocate = [True for i in range(n)]    # 判断第 i 个位置是否可以放 Q

            row = len(curr)
            for i in range(row):
                qIdx = curr[i].find('Q')    # 找到改行 Q 的位置
                canLocate[qIdx] = False     # 正下方
                if qIdx - (row - i) >= 0:   # 左斜对角线
                    canLocate[qIdx - (row - i)] = False
                if qIdx + (row - i) < n:    # 右斜对角线
                    canLocate[qIdx + (row - i)] = False

            for i in range(n):
                if canLocate[i]:
                    curr.append(line[:i] + 'Q' + line[i+1:])
                    findSolutionsDFS(curr, res, n)
                    curr.pop()

        if n == 0: return []

        curr = []
        res = []
        findSolutionsDFS(curr, res, n)

        return res

if __name__ == '__main__':
    n = 4

    res = Solution().solveNQueens(n)
    print(res)