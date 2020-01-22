"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are 
not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border 
will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""

from typing import List

class Solution:
    # # DFS: O(n^2) 148ms 55%
    # def solve(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     def dfs(board, i, j):
    #         row, col = len(board), len(board[0])
    #         if i < 0 or j < 0 or i >= row or j >= col: return
    #         if board[i][j] == 'X' or board[i][j] == '#': return

    #         board[i][j] = '#'
    #         ds = [[-1,0], [1,0], [0,-1], [0,1]]
    #         for d in ds:
    #             dfs(board, i + d[0], j + d[1])

    #     if not board: return
    #     row, col = len(board), len(board[0])
    #     if row <= 2 or col <= 2: return

    #     # 把左右边界的O的变成#
    #     for i in range(row):
    #         dfs(board, i, 0)
    #         dfs(board, i, col - 1)

    #     # 把上下边界的O的变成#
    #     for j in range(col):
    #         dfs(board, 0, j)
    #         dfs(board, row - 1, j)

    #     # 把剩下的O变成X
    #     for i in range(row):
    #         for j in range(col):
    #             if board[i][j] == 'O':
    #                 board[i][j] = 'X'

    #     # 还原变成#的O
    #     for i in range(row):
    #         for j in range(col):
    #             if board[i][j] == '#':
    #                 board[i][j] = 'O'


    # DFS: 144ms 71%
    # 本质和上面的一致，只是用 visited 数组记录了与边界连通的 O
    def solve(self, board: List[List[str]]) -> None:
        def dfs(board, i, j, visited):
            row, col = len(board), len(board[0])
            if i < 0 or j < 0 or i >= row or j >= col: return
            if board[i][j] == 'X' or visited[i][j]: return
            visited[i][j] = True
            ds = [[-1,0], [1,0], [0,-1], [0,1]]
            for d in ds:
                dfs(board, i + d[0], j + d[1], visited)

        if not board: return
        row, col = len(board), len(board[0])
        if row <= 2 or col <= 2: return

        visited = [[False for j in range(col)] for i in range(row)]

        for i in range(row):
            dfs(board, i, 0, visited)
            dfs(board, i, col - 1, visited)

        for j in range(col):
            dfs(board, 0, j, visited)
            dfs(board, row - 1, j, visited)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'


if __name__ == '__main__':
    # board = [
    #     ['X', 'X', 'X', 'X'],
    #     ['X', 'O', 'O', 'X'],
    #     ['X', 'X', 'O', 'X'],
    #     ['X', 'O', 'X', 'X']
    # ]

    board = [
        ["O", "X", "X", "O", "X"],
        ["X", "O", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"]
    ]

    Solution().solve(board)
    print(board)


