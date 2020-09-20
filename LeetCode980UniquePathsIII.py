"""
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square,
that walk over every non-obstacle square exactly once.

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation:
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

Note:

1 <= grid.length * grid[0].length <= 20
"""

from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res = 0
        diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(curr, visited, emptyNum, m, n):
            x, y = curr[0], curr[1]
            if x < 0 or x >= m or y < 0 or y >= n: return
            if grid[x][y] == -1: return

            # 如果到了终点，且已经访问了所有空位置，res += 1
            # 因为 visited 中包含起点，所以我们要保证 len(visited) == emptyNum + 1
            if grid[x][y] == 2:
                if len(visited) == emptyNum + 1:
                    self.res += 1
                return

            if curr in visited: return
            visited.add(curr)

            for dx, dy in diffs:
                dfs((x + dx, y + dy), visited, emptyNum, m, n)

            visited.remove(curr)

        visited = set() # 访问过的空位置
        m, n = len(grid), len(grid[0])
        start = None    # 开始的位置
        emptyNum = 0    # 空的位置的数量
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 0:
                    emptyNum += 1

        dfs(start, visited, emptyNum, m, n)
        return self.res