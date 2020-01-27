"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of 
islands. An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. You may assume all four edges 
of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

from typing import List

class Solution:
    # DFS: 144ms 72%
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            row, col = len(grid), len(grid[0])
            if i < 0 or i >= row or j < 0 or j >= col: return

            # 如果是小岛，则把小岛部分都变成 2，相当于访问过了
            if grid[i][j] == '1':
                grid[i][j] = '2'
                dfs(grid, i - 1, j)
                dfs(grid, i + 1, j)
                dfs(grid, i, j - 1)
                dfs(grid, i, j + 1)

        if not grid or not grid[0]: return 0

        res = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    res += 1

        return res



