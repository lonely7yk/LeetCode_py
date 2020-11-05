"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the 
two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all 
possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Example 1:

Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

Example 3:

Input: n = 1, edges = []
Output: [0]

Example 4:

Input: n = 2, edges = [[0,1]]
Output: [0,1]

Constraints:

1 <= n <= 2 * 10^4
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
"""

from typing import List
import collections


# # DFS + memo: O(m)
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         @functools.lru_cache(None)
#         def dfs(node, prev):
#             height = 1
            
#             for nxt in graph[node]:
#                 if nxt != prev:
#                     height = max(height, 1 + dfs(nxt, node))
                    
#             return height
        
#         graph = collections.defaultdict(list)
        
#         for x, y in edges:
#             graph[x].append(y)
#             graph[y].append(x)
        
#         heights = [dfs(i, None) for i in range(n)]  # 记录每个节点作为根的高度
#         minHeight = min(heights)                    # 找到最小高度
#         res = [i for i,h in enumerate(heights) if h == minHeight]
        
#         return res


# Topo sort: O(m)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: return [0]
        
        graph = collections.defaultdict(list)
        degree = [0 for i in range(n)]

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            degree[x] += 1
            degree[y] += 1

        dq = collections.deque()
        for i in range(n):
            if degree[i] == 1:
                dq.append(i)

        res = None
        while dq:
            size = len(dq)
            res = list(dq)

            for i in range(size):
                node = dq.popleft()
                for nxt in graph[node]:
                    degree[nxt] -= 1
                    if degree[nxt] == 1:
                        dq.append(nxt)

        return res


        
        