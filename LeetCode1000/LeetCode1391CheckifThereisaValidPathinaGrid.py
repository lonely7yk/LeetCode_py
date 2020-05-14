"""
Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.

You will initially start at the street of the upper-left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

Example 1:

Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:

Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
Example 4:

Input: grid = [[1,1,1,1,1,1,3]]
Output: true
Example 5:

Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
Output: true

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
"""

from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # d 为过来的方向，s 为 grid 中的值（street 的类型）
        # 1 上 2 左 3 下 4 右
        def direct(d, s):
            if d == 1:
                if s == 2:
                    return 1
                elif s == 3:
                    return 2
                elif s == 4:
                    return 4
                else:
                    return 0
            elif d == 2:
                if s == 1:
                    return 2
                elif s == 4:
                    return 3
                elif s == 6:
                    return 1
                else:
                    return 0
            elif d == 3:
                if s == 2:
                    return 3
                elif s == 5:
                    return 2
                elif s == 6:
                    return 4
                else:
                    return 0
            elif d == 4:
                if s == 1:
                    return 4
                elif s == 3:
                    return 3
                elif s == 5:
                    return 1
                else:
                    return 0

        def dfs(x, y, come, grid, visited):
            m, n = len(grid), len(grid[0])
            if x < 0 or x >= m or y < 0 or y >= n: return False
            if visited[x][y]: return False

            # d 要提前判断，因为可能来的方向和当前道路不匹配
            d = direct(come, grid[x][y])
            if d == 0: return False

            if x == m - 1 and y == n - 1: return True

            visited[x][y] = True
            if d == 1:
                return dfs(x - 1, y, 1, grid, visited)
            elif d == 2:
                return dfs(x, y - 1, 2, grid, visited)
            elif d == 3:
                return dfs(x + 1, y, 3, grid, visited)
            else:
                return dfs(x, y + 1, 4, grid, visited)

        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1: return True
        visited = [[False for j in range(n)] for i in range(m)]

        a = grid[0][0]
        visited[0][0] = True
        if a == 1 or a == 6:
            return dfs(0, 1, 4, grid, visited)
        elif a == 2 or a == 3:
            return dfs(1, 0, 3, grid, visited)
        elif a == 4:
            return dfs(0, 1, 4, grid, visited) or dfs(1, 0, 3, grid, visited)
        else:
            return False


# grid = [[2,4,3],[6,5,2]]
# grid = [[1,2,1],[1,2,1]]
# grid = [[1,1,2]]
# grid = [[1,1,1,1,1,1,3]]
grid = [[2], [2], [2], [2], [2], [2], [6]]
res = Solution().hasValidPath(grid)
print(res)
