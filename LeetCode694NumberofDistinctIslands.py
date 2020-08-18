"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid 
are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and 
only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.

Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""

from typing import List

# DFS
# 该题的难点在于如何判断两个岛是 distinct。
# 其实可以通过 dfs 过程中把所有相对位置 i,j 索引依次放入一个 arr，然后用 join 组合成字符串。如果两个字符串一致，那就不是 distinct
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        diffs = [(-1,0), (1,0), (0,1), (0,-1)]
        
        def dfs(grid, x, y, i, j, arr):
            # x,y 是绝对位置
            # i,j 是相对位置（判断 distinct 是用相对位置的）
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]): return
            if grid[x][y] != 1: return
            grid[x][y] = -1 # 记得把 grid 设成不是 1 的数，避免重复访问
            
            arr.append(str(i))
            arr.append(str(j))
            
            for dx, dy in diffs:
                dfs(grid, x + dx, y + dy, i + dx, j + dy, arr)
            
        
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    arr = []
                    dfs(grid, i, j, 0, 0, arr)
                    res.add("#".join(arr))
                    
        return len(res)
        
        
