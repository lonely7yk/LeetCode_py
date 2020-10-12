"""
There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] 
represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of 
cities. In other words, the cities form a tree.

A subtree is a subset of cities where every city is reachable from every other city in the subset, where the 
path between each pair passes through only the cities from the subset. Two subtrees are different if there is 
a city in one subtree that is not present in the other.

For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities 
in the subtree is equal to d.

Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum 
distance between any two cities is equal to d.

Notice that the distance between the two cities is the number of edges in the path between them.

Example 1:

Input: n = 4, edges = [[1,2],[2,3],[2,4]]
Output: [3,4,0]
Explanation:
The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
No subtree has two nodes where the max distance between them is 3.

Example 2:

Input: n = 2, edges = [[1,2]]
Output: [1]

Example 3:

Input: n = 3, edges = [[1,2],[2,3]]
Output: [2,1]

Constraints:

2 <= n <= 15
edges.length == n-1
edges[i].length == 2
1 <= ui, vi <= n
All pairs (ui, vi) are distinct.
"""

from typing import List
import collections


# Bitmask: O(2^n * n^2)
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # 通过 bfs 求最大距离，并返回访问的所有节点
        def bfs(start, graph):
            dq = collections.deque([(start, 0)])
            visited = {start}
            maxDist = 0

            while dq:
                node, dist = dq.popleft()
                maxDist = max(maxDist, dist)

                for nxt in graph[node]:
                    if nxt not in visited:
                        dq.append((nxt, dist + 1))
                        visited.add(nxt)

            return maxDist, visited


        def calMaxDistance(bitmask):
            cities = set()
            # bitmask 找出所有城市
            for i in range(n):
                if (bitmask >> i) & 1 == 1:
                    cities.add(i + 1)

            # 只构建包含 cities 节点的 graph
            graph = collections.defaultdict(list)
            for x, y in edges:
                if x in cities and y in cities:
                    graph[x].append(y)
                    graph[y].append(x)

            ans = 0
            for i in cities:
                dist, visited = bfs(i, graph)
                # 如果有节点没访问到，直接返回 0
                if len(visited) < len(cities): return 0
                ans = max(ans, dist)

            return ans

        res = [0 for i in range(n - 1)]
        # 对所有可能性找所有最大距离
        for i in range(1, 2 ** n):
            d = calMaxDistance(i)
            if d > 0: res[d - 1] += 1

        return res


n = 4
edges = [[1,2],[2,3],[2,4]]
res = Solution().countSubgraphsForEachDiameter(n, edges)
print(res)
