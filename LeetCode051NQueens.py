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
    # # DFS: 60 ms 80%
    # def solveNQueens(self, n: int) -> List[List[str]]:

    #     def findSolutionsDFS(colIdx, curr, res, n):
    #         if len(curr) == n:
    #             res.append(list(curr))
    #             return

    #         line = '.' * n
    #         canLocate = [True for i in range(n)]    # 判断第 i 个位置是否可以放 Q

    #         # 对于每一行，根据其 Q 的位置确定现在这行有哪些位置不能放 Q
    #         row = len(curr)     # 现在有多少行
    #         for i in range(row):
    #             # qIdx = curr[i].find('Q')    # 找到改行 Q 的位置
    #             qIdx = colIdx[i]            # 第 i 行的 Q 的位置
    #             canLocate[qIdx] = False     # 正下方
    #             if qIdx - (row - i) >= 0:   # 左斜对角线
    #                 canLocate[qIdx - (row - i)] = False
    #             if qIdx + (row - i) < n:    # 右斜对角线
    #                 canLocate[qIdx + (row - i)] = False

    #         for i in range(n):
    #             if canLocate[i]:
    #                 colIdx[row] = i
    #                 curr.append(line[:i] + 'Q' + line[i+1:])
    #                 findSolutionsDFS(colIdx, curr, res, n)
    #                 curr.pop()
    #                 colIdx[row] = -1

    #     if n == 0: return []

    #     colIdx = [-1 for i in range(n)]     # 表示第 i 个皇后在第几列
    #     curr = []
    #     res = []
    #     findSolutionsDFS(colIdx, curr, res, n)

    #     return res

    # DFS: 52ms 91.7%
    def solveNQueens(self, n: int) -> List[List[str]]:

        def findSolutionsDFS(colSet, d1Set, d2Set, curr, res, n):
            if len(curr) == n:
                res.append(list(curr))
                return

            line = '.' * n
            currRow = len(curr)

            for currCol in range(n):
                d1 = currRow - currCol  # 相同右斜对角线的 currRow - currCol 相同
                d2 = currRow + currCol  # 相同左斜对角线的 currRow + currCol 相同
                if currCol not in colSet and d1 not in d1Set and d2 not in d2Set:
                    colSet.add(currCol)
                    d1Set.add(d1)
                    d2Set.add(d2)
                    curr.append(line[:currCol] + 'Q' + line[currCol+1:])
                    findSolutionsDFS(colSet, d1Set, d2Set, curr, res, n)
                    curr.pop()
                    colSet.remove(currCol)
                    d1Set.remove(d1)
                    d2Set.remove(d2)

        if n == 0: return []

        colSet = set()  # 表示已经占有的列
        d1Set = set()   # 表示已占有的右斜对角线
        d2Set = set()   # 表示已占有的左斜对角线
        curr = []
        res = []
        findSolutionsDFS(colSet, d1Set, d2Set, curr, res, n)

        return res

if __name__ == '__main__':
    n = 4

    res = Solution().solveNQueens(n)
    print(res)