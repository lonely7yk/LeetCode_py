"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens 
puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as 
shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution:
    # # DFS: 68ms 53.40%
    # # 和 51 题一样的做法
    # def totalNQueens(self, n: int) -> int:
    #     def findSolutionsDFS(curr, res, n):
    #         if len(curr) == n:
    #             res.append(curr)
    #             return

    #         canStay = [True for i in range(n)]
    #         row = len(curr)
    #         line = '.' * n
    #         for i in range(row):
    #             idx = curr[i].find('Q')
    #             canStay[idx] = False

    #             leftIdx = idx - (row - i)
    #             rightIdx = idx + (row - i)
    #             if leftIdx >= 0: canStay[leftIdx] = False
    #             if rightIdx < n: canStay[rightIdx] = False

    #         for i in range(n):
    #             if canStay[i]:
    #                 curr.append(line[:i] + 'Q' + line[i + 1:])
    #                 findSolutionsDFS(curr, res, n)
    #                 curr.pop()


    #     res = []
    #     curr = []
    #     findSolutionsDFS(curr, res, n)
    #     return len(res)

    # DFS: 44ms 87.62%
    # 参考：https://leetcode.wang/leetCode-52-N-QueensII.html
    def totalNQueens(self, n: int) -> int:
        def countSolutionsDFS(colSet, d1Set, d2Set, currRow, n, count):
            if currRow == n:
                count += 1
            else:
                for currCol in range(n):
                    if currCol in colSet: continue

                    d1 = currRow - currCol  # 相同右斜对角线的 currRow - currCol 相同
                    d2 = currRow + currCol  # 相同左斜对角线的 currRow + currCol 相同

                    if d1 in d1Set or d2 in d2Set: continue

                    colSet.add(currCol)
                    d1Set.add(d1)
                    d2Set.add(d2)
                    count = countSolutionsDFS(colSet, d1Set, d2Set, currRow + 1, n, count)
                    colSet.remove(currCol)
                    d1Set.remove(d1)
                    d2Set.remove(d2)

            return count

        d1Set = set()
        d2Set = set()
        colSet = set()
        count = countSolutionsDFS(colSet, d1Set, d2Set, 0, n, 0)
        return count


if __name__ == '__main__':
    n = 4

    res = Solution().totalNQueens(n)
    print(res)

