"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: 
|xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly 
one simple path between any two points.


Example 1:

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Example 3:

Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4

Example 4:

Input: points = [[-1000000,-1000000],[1000000,1000000]]
Output: 4000000

Example 5:

Input: points = [[0,0]]
Output: 0
 

Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.

"""

from typing import List
import heapq

# 最小代价生成树问题
# Prime
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n = len(points)
#         dists = [float('inf') for i in range(n)]   # 当前到所有节点的最小距离
#         visited = {0}           # 访问过的节点
#         minIdx = 0              # 当前最小距离的索引
#         minDist = float('inf')  # 当前最小距离
#         res = 0

#         # 直到把所有节点加到树中才停止遍历
#         while len(visited) != n:
#             point = points[minIdx]  # 上一个被添加到树上的节点

#             minDist = float('inf')
#             minIdx = -1

#             # 根据新加入的节点，更新 dists 数组，并找到当前 minDist 和 minIdx
#             for i, (x, y) in enumerate(points):
#                 if i in visited: continue   # 只遍历没有添加到树上的节点

#                 tmp = abs(x - point[0]) + abs(y - point[1])
#                 dists[i] = min(dists[i], tmp)

#                 if dists[i] < minDist:
#                     minDist = dists[i]
#                     minIdx = i

#             res += minDist
#             visited.add(minIdx)

#         return res


# Kruskal
# 要用并查集来保证图无环，并记录添加到树上的节点数
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(roots, x):
            if x != roots[x]:
                roots[x] = find(roots, roots[x])    # compress
            return roots[x]

        n = len(points)
        manhattan = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
        heap = []
        roots = list(range(n))
        size = [1 for i in range(n)]
        res = 0

        # 先把所有节点按照距离存放到 heap 中
        for i in range(n):
            for j in range(i + 1, n):
                d = manhattan(points[i], points[j])
                heap.append((d, (i, j)))

        # 堆化
        heapq.heapify(heap)

        while heap:
            d, (i, j) = heapq.heappop(heap)
            root1 = find(roots, i)
            root2 = find(roots, j)

            # 感觉 union by rank 提升性能不大
            # if root1 != root2:
            #     res += d
            #     # union by rank
            #     if size[root1] < size[root2]:
            #         roots[root1] = root2
            #         size[root2] += size[root1]
            #         if size[root2] == n: break
            #     else:
            #         roots[root2] = root1
            #         size[root1] += size[root2]
            #         if size[root1] == n: break

            if root1 != root2:
                res += d
                
                roots[root2] = root1
                size[root1] += size[root2]
                if size[root1] == n: break

        return res


points = [[2,-3],[-17,-8],[13,8],[-17,-15]]
res = Solution().minCostConnectPoints(points)
print(res)

