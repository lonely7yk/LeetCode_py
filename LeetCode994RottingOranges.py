"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""

from typing import List
import collections

# BFS
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = collections.deque()
        leftNum = 0     # 还剩多少橘子没有腐烂
        m, n = len(grid), len(grid[0])
        res = 0
        diffs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    leftNum += 1
                elif grid[i][j] == 2:
                    dq.append((i, j))
                    
        while dq and leftNum:
            res += 1
            size = len(dq)
            
            for i in range(size):
                x, y = dq.popleft()
                
                for dx, dy in diffs:
                    newX = x + dx
                    newY = y + dy
                    
                    if newX < 0 or newX >= m or newY < 0 or newY >= n: continue
                    if grid[newX][newY] == 1:
                        leftNum -= 1
                        grid[newX][newY] = 2
                        dq.append((newX, newY))
                        
        return res if leftNum == 0 else -1
