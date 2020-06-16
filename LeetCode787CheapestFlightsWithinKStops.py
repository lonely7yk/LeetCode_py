"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is 
to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
 
Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""

from typing import List
import collections
import heapq

# # DFS + memo: 16%
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

#         graph = collections.defaultdict(list)
#         memo = [[[-1 for k in range(K + 1)] for j in range(n)] for i in range(n)]

#         for from_,to_,price in flights:
#             graph[from_].append((to_, price))
       
#        # 返回 src 到 dst 最多停留 K 次的最小价格
#         def dfs(src, dst, K):
#             if src == dst: return 0
#             if K < 0: return float('inf')   # K < 0 说明不能转机了
#             # -1 表示未记录，如果不是 -1，表示已经记录过了
#             if memo[src][dst][K] != -1: return memo[src][dst][K]

#             minPrice = float('inf')
#             # 对于 src 连接的每个节点，计算每个节点的最小价格，然后取最小值
#             for to_,price in graph[src]:
#                 minPrice = min(minPrice, price + dfs(to_, dst, K - 1))

#             memo[src][dst][K] = minPrice
#             return minPrice

#         res = dfs(src, dst, K)

#         return res if res != float('inf') else -1

# Dijkstra + Heap: 81%
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)

        for a, b, p in flights:
            graph[a][b] = p

        heap = [(0, src, K + 1)]    # 三个元素分别表示 (当前价格, 当前结点, 剩余可转飞次数)

        while heap:
            p, a, k = heapq.heappop(heap)
            if a == dst: return p

            if k > 0:
                for b in graph[a]:
                    heapq.heappush(heap, (p + graph[a][b], b, k - 1))

        return -1



# n = 3
# edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 1

# n = 5
# edges = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
# src = 2
# dst = 1
# k = 1

n = 10
edges = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
src = 6
dst = 0
k = 7

res = Solution().findCheapestPrice(n, edges, src, dst, k)
print(res)



