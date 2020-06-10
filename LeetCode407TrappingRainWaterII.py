"""
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D 
elevation map, compute the volume of water it is able to trap after raining.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before 
the rain.

After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

Constraints:

1 <= m, n <= 110
0 <= heightMap[i][j] <= 20000
"""

from typing import List
import heapq

# heap: 93%
# reference: https://www.youtube.com/watch?time_continue=345&v=cJayBq38VYw&feature=emb_logo
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False for j in range(n)] for i in range(m)]
        heap = []

        # 先把边缘一圈加入到 heap 中
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][0] = True
            visited[i][n - 1] = True
        # 先把边缘一圈加入到 heap 中
        for j in range(1, n - 1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
            visited[0][j] = True
            visited[m - 1][j] = True

        # 相当于在一直不停地缩圈，直到所有节点都被访问
        # 每次缩圈都是通过 bottleneck 向内部缩小
        res = 0
        while heap:
            # 找到高度最小的位置
            height, x, y = heapq.heappop(heap)

            # 将该位置的四周加入到 heap（未访问）
            for x,y in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                # 排除走出边缘的情况
                if x < 0 or x >= m or y < 0 or y >= n: continue

                if not visited[x][y]:
                    # 注意这里加入的高度是 max(heightMap[x][y], height)
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))
                    visited[x][y] = True
                    if heightMap[x][y] < height:
                        res += height - heightMap[x][y]

        return res


heightMap = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
res = Solution().trapRainWater(heightMap)
print(res)
