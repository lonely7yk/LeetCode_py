"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
[0,1] is the same as [1,0] and thus will not appear together in edges.
"""

from typing import List

# Union Find: O(klogn)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(roots, x):
            if x == roots[x]:
                return x
            else:
                roots[x] = find(roots, roots[x])    # path compression
                return roots[x]
        
        roots = list(range(n))
        size = [1 for i in range(n)]
        
        for x, y in edges:
            root1 = find(roots, x)
            root2 = find(roots, y)
            
            # x 和 y 的 root 相同，你又要连 x 和 y 那一定会出现环
            if root1 == root2: return False
        
            # union by rank
            if size[root1] > size[root2]:
                roots[root2] = root1
                size[root1] += size[root2]
            else:
                roots[root1] = root2
                size[root2] += size[root1]
                
            n -= 1
            
        return n == 1


# # DFS
# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         # DFS 判断是否有环，因为是无向图，所以需要加一个 prev 参数
#         def hasCycle(graph, visited, curr, prev):
#             if visited[curr]: return True
            
#             visited[curr] = True
#             for nxt in graph[curr]:
#                 if nxt == prev: continue
#                 if hasCycle(graph, visited, nxt, curr): return True
                
#             return False
        
#         graph = collections.defaultdict(list)
        
#         for x, y in edges:
#             graph[x].append(y)
#             graph[y].append(x)
        
#         visited = [False for i in range(n)]
#         # 只从 0 开始进行 DFS 遍历
#         if hasCycle(graph, visited, 0, -1): 
#             return False
        
#         # 判断是否所有节点都访问到了，用于判断是否是同一棵树
#         for i in range(n):
#             if not visited[i]: return False
            
#         return True
        
