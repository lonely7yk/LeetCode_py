"""
You are given a rows x cols matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step,
you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner
(rows - 1, cols - 1), find the path with the maximum non-negative product. The product of a path is the
product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative return -1.

Notice that the modulo is performed after getting the maximum product.

Example 1:

Input: grid = [[-1,-2,-3],
               [-2,-3,-3],
               [-3,-3,-2]]
Output: -1

Explanation: It's not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.

Example 2:

Input: grid = [[1,-2,1],
               [1,-2,1],
               [3,-4,1]]
Output: 8

Explanation: Maximum non-negative product is in bold (1 * 1 * -2 * -4 * 1 = 8).

Example 3:

Input: grid = [[1, 3],
               [0,-4]]
Output: 0

Explanation: Maximum non-negative product is in bold (1 * 0 * -4 = 0).

Example 4:

Input: grid = [[ 1, 4,4,0],
               [-2, 0,0,1],
               [ 1,-1,1,1]]
Output: 2
Explanation: Maximum non-negative product is in bold (1 * -2 * 1 * -1 * 1 * 1 = 2).

Constraints:

1 <= rows, cols <= 15
-4 <= grid[i][j] <= 4
"""

from typing import List


# 2D DP: O(mn)
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxGrid = [[float('-inf') for j in range(n)] for i in range(m)]
        minGrid = [[float('inf') for j in range(n)] for i in range(m)]

        maxGrid[0][0] = grid[0][0]
        minGrid[0][0] = grid[0][0]

        for i in range(1, m):
            lastMax = maxGrid[i - 1][0]
            lastMin = minGrid[i - 1][0]

            maxGrid[i][0] = max(lastMax * grid[i][0], lastMin * grid[i][0])
            minGrid[i][0] = min(lastMax * grid[i][0], lastMin * grid[i][0])

        for j in range(1, n):
            lastMax = maxGrid[0][j - 1]
            lastMin = minGrid[0][j - 1]

            maxGrid[0][j] = max(lastMax * grid[0][j], lastMin * grid[0][j])
            minGrid[0][j] = min(lastMax * grid[0][j], lastMin * grid[0][j])

        for i in range(1, m):
            for j in range(1, n):
                lastLeftMax = maxGrid[i][j - 1]
                lastLeftMin = minGrid[i][j - 1]
                lastUpMax = maxGrid[i - 1][j]
                lastUpMin = minGrid[i - 1][j]

                maxGrid[i][j] = max(lastLeftMax * grid[i][j], lastLeftMin * grid[i][j], lastUpMax * grid[i][j],
                                    lastUpMin * grid[i][j])
                minGrid[i][j] = min(lastLeftMax * grid[i][j], lastLeftMin * grid[i][j], lastUpMax * grid[i][j],
                                    lastUpMin * grid[i][j])

        return maxGrid[-1][-1] % (10 ** 9 + 7) if maxGrid[-1][-1] >= 0 else -1
