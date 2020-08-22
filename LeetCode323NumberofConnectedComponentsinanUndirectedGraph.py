"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] 
is the same as [1, 0] and thus will not appear together in edges.
"""

from typing import List

# # DFS
# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         def dfs(visited, curr, graph):
#             if curr in visited: return
            
#             visited.add(curr)
#             for nxt in graph[curr]:
#                 dfs(visited, nxt, graph)
        
#         graph = collections.defaultdict(list)
#         for x, y in edges:
#             graph[x].append(y)
#             graph[y].append(x)
            
#         visited = set()
#         cnt = 0
#         for i in range(n):
#             if i not in visited:
#                 dfs(visited, i, graph)
#                 cnt += 1
            
#         return cnt
        

# Union Find
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 找到根节点
        def find(roots, id):
            while roots[id] != id:
                roots[id] = roots[roots[id]]    # compressed
                id = roots[id]
                
            return id
        
        roots = list(range(n))
        
        for x, y in edges:
            root1 = find(roots, x)
            root2 = find(roots, y)
        
            # union
            if root1 != root2:
                roots[root1] = root2
                n -= 1  # 每次连接 n 都自减 1
                
        return n


