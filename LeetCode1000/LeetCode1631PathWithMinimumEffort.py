"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where
heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you
hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right,
and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:

Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
"""

from typing import List


# # Binary Search + DFS: O(mn)
# # Binary Search + BFS 做法是一样的
# class Solution:
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:
#         # 最大 effort 的条件下是否能到达 (m-1,n-1)
#         def dfs(x, y, visited, effort, last):
#             if x < 0 or x >= m or y < 0 or y >= n: return False
#             if abs(last - heights[x][y]) > effort: return False
#             if x == m - 1 and y == n - 1: return True
#             if (x, y) in visited: return False
#
#             visited.add((x, y))
#             flag = False
#             for dx, dy in directs:
#                 if dfs(x + dx, y + dy, visited, effort, heights[x][y]): flag = True
#
#             return flag
#
#         m, n = len(heights), len(heights[0])
#         directs = [(-1,0),(1,0),(0,1),(0,-1)]
#
#         # 找到高度的最大最小值
#         maxH, minH = float('-inf'), float('inf')
#         for i in range(m):
#             for j in range(n):
#                 cur = heights[i][j]
#                 maxH = max(maxH, cur)
#                 minH = min(minH, cur)
#
#         # effort 范围为 [0, maxEffort]
#         maxEffort = maxH - minH
#         left, right = 0, maxEffort + 1
#
#         while left < right:
#             mid = (left + right) // 2
#
#             if dfs(0, 0, set(), mid, heights[0][0]):
#                 right = mid
#             else:
#                 left = mid + 1
#
#         return left


# Union Find: O(mn*log(mn))
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def find(roots, x):
            if x != roots[x]:
                roots[x] = find(roots, roots[x])
            return roots[x]

        edges = []
        m, n = len(heights), len(heights[0])
        roots = [i for i in range(m * n)]

        # 先把所有边保存起来
        for i in range(m):
            for j in range(n):
                cur = i * n + j
                if i < m - 1:
                    below = (i + 1) * n + j
                    edges.append((cur, below, abs(heights[i][j] - heights[i + 1][j])))
                if j < n - 1:
                    right = i * n + j + 1
                    edges.append((cur, right, abs(heights[i][j] - heights[i][j + 1])))

        # 根据边长排序
        edges.sort(key=lambda x: x[2])
        for x, y, e in edges:
            r1 = find(roots, x)
            r2 = find(roots, y)
            if r1 != r2: roots[r2] = r1

            # 如果 (0,0) 和 (m-1,n-1) 连起来就返回当前的 effort
            if find(roots, 0) == find(roots, m * n - 1): return e

        return 0


heights = [[1,2,2],[3,8,2],[5,3,5]]
res = Solution().minimumEffortPath(heights)
print(res)
