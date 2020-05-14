"""
Given a m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])

Notice that there could be some invalid signs on the cells of the grid which points outside the grid.

You will initially start at the upper left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path doesn't have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

Example 1:

Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.

Example 2:

Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).

Example 3:

Input: grid = [[1,2],[4,3]]
Output: 1

Example 4:

Input: grid = [[2,2,2],[2,2,2]]
Output: 3

Example 5:

Input: grid = [[4]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
"""

from typing import List
import collections

class Solution:
    # DFS+BFS: O(MN) O(MN) 376ms 78.5%
    # 先用 DFS 遍历一遍找到从(0,0)不用修改就能遍历的所有点保存在一个 queue 中（用list其实也可以），把对应位置 dp[i][j] = 0
    # 然后在遍历 queue 中所有点，修改他的方向，然后 DFS，结果还是保存在 queue 中，对应位置 dp[i][j] = 1
    # 以此类推，直到 queue 为空或 dp[-1][-1] != -1，退出循环，结果为 dp[-1][-1
    def minCost(self, grid: List[List[int]]) -> int:
        def dfs(grid, x, y, queue, direct, dp, k):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]): return
            if dp[x][y] != -1: return   # 说明该点已经走过了

            dp[x][y] = k        # k 表示至少修改 k 次才能走到 (x, y)
            queue.append([x, y])
            dfs(grid, x + direct[grid[x][y] - 1][0], y + direct[grid[x][y] - 1][1], queue, direct, dp, k)

        k = 0
        queue = collections.deque()
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        dp = [[-1 for j in range(len(grid[0]))] for i in range(len(grid))]
        dfs(grid, 0, 0, queue, direct, dp, k)

        # BFS
        while queue and dp[-1][-1] == -1:
            k += 1
            queue, queue2 = [], queue
            [dfs(grid, x + i, y + j, queue, direct, dp, k) for x, y in queue2 for i, j in direct]

        return dp[-1][-1]


grid = [[1,1,3],[2,2,2],[4,4,1]]
res = Solution().minCost(grid)
print(res)
