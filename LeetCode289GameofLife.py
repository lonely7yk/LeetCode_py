"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular 
automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live 
(represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors 
(horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia 
article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current 
state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, 
return the next state.

Example 1:

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot 
update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which 
would cause problems when the active area encroaches upon the border of the array (i.e., live cells 
reach the border). How would you address these problems?
"""

from typing import List


# O(mn) - O(1)
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = 1 # cnt从1开始记，这样能判断正负
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0: continue
                        if 0 <= i + di < m and 0 <= j + dj < n:
                            if board[i + di][j + dj] > 0:
                                cnt += 1
                
                # 正数表示当前位置的数为 1，负数表示为 0。abs(cnt) - 1 表示周围 1 的个数
                if board[i][j] <= 0:
                    cnt = -cnt
                board[i][j] = cnt
                
        # 第二次遍历
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    if board[i][j] - 1 == 2 or board[i][j] - 1 == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                else:
                    if -board[i][j] - 1 == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                            
        
