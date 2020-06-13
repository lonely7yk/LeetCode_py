"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a 
continent, the "Pacific ocean" touches the left and top edges of the matrix and the 
"Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one 
with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above 
matrix).
"""

from typing import List

# DFS: 从边缘开始做 DFS，得到 pacific 和 atlantic 可以到达的位置
# 然后如果能同时到达 pacific 和 atlantic 的话就把坐标放进 res 中
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        def dfs(i, j, visited, last):
            m, n = len(visited), len(visited[0])
            if i < 0 or j < 0 or i >= m or j >= n: return
            if visited[i][j]: return
            if matrix[i][j] < last: return

            visited[i][j] = True
            dfs(i - 1, j, visited, matrix[i][j])
            dfs(i + 1, j, visited, matrix[i][j])
            dfs(i, j - 1, visited, matrix[i][j])
            dfs(i, j + 1, visited, matrix[i][j])

        if not matrix: return []

        m, n = len(matrix), len(matrix[0])
        pVisited = [[False for j in range(n)] for i in range(m)]
        aVisited = [[False for j in range(n)] for i in range(m)]

        for i in range(m):
            dfs(i, 0, pVisited, 0)
            dfs(i, n - 1, aVisited, 0)

        for j in range(n):
            dfs(0, j, pVisited, 0)
            dfs(m - 1, j, aVisited, 0)

        res = []
        for i in range(m):
            for j in range(n):
                if pVisited[i][j] and aVisited[i][j]:
                    res.append([i, j])

        return res


matrix = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]
res = Solution().pacificAtlantic(matrix)
print(res)

