"""
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3

Example 3:

Input: stones = [[0,0]]
Output: 0
 

Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000
"""

from typing import List


# 首先明确一点，move 的次数 = 总 stone 数 - island 的个数
# 这里的 island 表示相互连在一起的 stones（两个石头有相同的 x 或 y 表示连在一起）

# # DFS: O(n^2)
# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         # 将遍历过的节点都放入 seen 中
#         def dfs(graph, cur, seen):
#             if cur in seen: return
            
#             seen.add(cur)
#             for nxt in graph[cur]:
#                 dfs(graph, nxt, seen)
        
#         graph = collections.defaultdict(list)
#         n = len(stones)
        
#         # 构建图需要 O(n^2) 注意这里使用索引来构建图
#         for i in range(1, n):
#             x = stones[i]
#             for j in range(i):
#                 y = stones[j]
#                 if x[0] == y[0] or x[1] == y[1]:
#                     graph[i].append(j)
#                     graph[j].append(i)
            
#         seen = set()    # 访问过的节点
#         numIsland = 0
#         for i in range(n):
#             if i in seen: continue
#             # i 不在 seen 中说明这是一个新的 island
#             dfs(graph, i, seen)
#             numIsland += 1
            
#         return n - numIsland


# Union Find: O(nlogn)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            if x not in UF: UF[x] = x
            if y not in UF: UF[y] = y
            UF[find(x)] = find(y)
        
        for x, y in stones:
            # 用 -y - 1 代替 y，用于区分 x
            union(x, ~y)
            
        return len(stones) - len({find(x) for x in UF})
            
        
        
