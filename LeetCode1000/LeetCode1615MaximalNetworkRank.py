"""
There is an infrastructure of n cities with some number of roads connecting these cities. Each 
roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads 
to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

Example 1:

Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. 
The road between 0 and 1 is only counted once.

Example 2:

Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation: There are 5 roads that are connected to cities 1 or 2.

Example 3:

Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
Output: 5
Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
 

Constraints:

2 <= n <= 100
0 <= roads.length <= n * (n - 1) / 2
roads[i].length == 2
0 <= ai, bi <= n-1
ai != bi
Each pair of cities has at most one road connecting them.
"""

from typing import List
import collections


# # O(n^2)
# class Solution:
#     def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
#         # 记录一个点连接的节点数
#         cntMap = collections.defaultdict(lambda: 0)
#         # 记录直接相连的节点
#         connectSet = set()

#         for x, y in roads:
#             cntMap[x] += 1
#             cntMap[y] += 1
#             connectSet.add((x,y))
#             connectSet.add((y,x))

#         res = 0

#         for i in range(n):
#             for j in range(i + 1, n):
#                 rank = cntMap[i] + cntMap[j]
#                 # 如果 i,j 直接相连，那还要减 1
#                 if (i, j) in connectSet: rank -= 1
#                 res = max(res, rank)

#         return res

# imporove
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # 记录一个点连接的节点数
        cntMap = collections.defaultdict(lambda: 0)
        # 记录直接相连的节点
        connectSet = set()

        for x, y in roads:
            cntMap[x] += 1
            cntMap[y] += 1
            connectSet.add((x,y))
            connectSet.add((y,x))

        res = 0
        # 排序来提高效率
        cntItems = sorted(list(cntMap.items()), key=lambda x: -x[1])
        m = len(cntItems)

        for i in range(m):
            for j in range(i + 1, m):
                rank = cntItems[i][1] + cntItems[j][1]
                if res >= rank: break
                # 如果 i,j 直接相连，那还要减 1
                if (cntItems[i][0], cntItems[j][0]) in connectSet: rank -= 1
                res = max(res, rank)

        return res


n = 8
# roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
roads = []
res = Solution().maximalNetworkRank(n, roads)
print(res)
