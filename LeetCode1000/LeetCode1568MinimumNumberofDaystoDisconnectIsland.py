"""
Given a 2D grid consisting of 1s (land) and 0s (water).  An island is a maximal 4-directionally 
(horizontal or vertical) connected group of 1s.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

Example 1:

Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.

Example 2:

Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.

Example 3:

Input: grid = [[1,0,1,0]]
Output: 0

Example 4:

Input: grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,0,1,1]]
Output: 1

Example 5:

Input: grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,1,1,1]]
Output: 2

Constraints:

1 <= grid.length, grid[i].length <= 30
grid[i][j] is 0 or 1.
"""

from typing import List


# 这题的关键在于要把一个岛分成两个的最大天数为 2，所以我们只要依次考虑 0 和 1 的情况即可，其他情况都返回 2
# reference: https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/discuss/819303/Python-you-need-at-most-2-days
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        diffs = [(-1,0),(1,0),(0,-1),(0,1)]

        # 把一个 island 中的所有位置都访问一遍
        def visit(grid, i, j, visited):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]): return
            if grid[i][j] == 0: return
            if visited[i][j]: return

            visited[i][j] = True
            for di, dj in diffs:
                visit(grid, i + di, j + dj, visited)

        # 计算 grid 中有多少个 islands
        def numIslands(grid, visited):
            cnt = 0
            m, n = len(grid), len(grid[0])

            for i in range(m):
                for j in range(n):
                    if visited[i][j]: continue
                    if grid[i][j]: 
                        cnt += 1
                        visit(grid, i, j, visited)

            return cnt

        # 如果初始的 island 数就不等于 1，直接返回 0
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        if numIslands(grid, visited) != 1:
            return 0

        # 如果只修改一个位置，island 不等于 1，返回 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    visited = [[False for j in range(n)] for i in range(m)]
                    if numIslands(grid, visited) != 1:
                        return 1

                    grid[i][j] = 1

        # 否则都返回 2
        return 2

