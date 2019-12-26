"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.

Note:

- The given board contain only digits 1-9 and the character '.'.
- You may assume that the given Sudoku puzzle will have a single unique solution.
- The given board size is always 9x9.
"""

from typing import List

class Solution:

    # DFS: 684ms 23.3%
    def __init__(self):
        self.flag = False
        self.vals = "123456789"

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for val in self.vals:
                        if not self.checkRow(val, i, j, board) and not self.checkCol(val, i, j, board) \
                            and not self.checkGrid(val, i, j, board):
                            board[i][j] = val
                            self.solveSudoku(board)
                            if self.flag: return    # 如果赋值后，flag 为 true，则直接返回
                            board[i][j] = '.'
                    else:
                        return
        self.flag = True    # 如果跑完一遍说明全部赋值，不需要继续赋值

    def checkRow(self, val, x, y, board):
            for i in range(9):
                if val == board[x][i]: return True
            return False

    def checkCol(self, val, x, y, board):
        for i in range(9):
            if val == board[i][y]: return True
        return False

    def checkGrid(self, val, x, y, board):
        rowNum = x // 3
        colNum = y // 3
        for i in range(rowNum * 3, (rowNum + 1) * 3):
            for j in range(colNum * 3, (colNum + 1) * 3):
                if val == board[i][j]: return True
        return False

if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Solution().solveSudoku(board)
    print()