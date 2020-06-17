"""
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, 
empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of 
the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent 
battleships.

Example:
X..X
...X
...X
In the above board there are 2 battleships.

Invalid Example:
...X
XXXX
...X

This is an invalid board that you will not receive - as battleships will always have a cell separating between them.

Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
"""

from typing import List

# DFS: 每遇到一个 X 就用 DFS 把他连通的都变成 #，然后依次遍历找 X 的个数即可。
# class Solution:
#     def countBattleships(self, board: List[List[str]]) -> int:
#         def dfs(i, j, m, n):
#             if i < 0 or j < 0 or i >= m or j >= n: return 

#             if board[i][j] == 'X':
#                 board[i][j] = '#'
#                 dfs(i - 1, j, m, n)
#                 dfs(i + 1, j, m, n)
#                 dfs(i, j - 1, m, n)
#                 dfs(i, j + 1, m, n)

#         m, n = len(board), len(board[0])
#         res = 0
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == 'X':
#                     dfs(i, j, m, n)
#                     res += 1

#         return res

# 对于每一个 X 如果他左边和上面都不是 X 则进行一次计数，因为遍历是从左往右从上往下的，
# 所以如果左边或上面是 X 说明当前的 X 已经被计数过了
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] == '.': continue
                if j > 0 and board[i][j - 1] == 'X': continue
                if i > 0 and board[i - 1][j] == 'X': continue
                res += 1

        return res

