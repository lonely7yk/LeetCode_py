"""
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections 
forming a network where connections[i] = [a, b] represents a connection between servers a and b. 
Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach 
some other server.

Return all critical connections in the network in any order.

Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 
Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
"""

import collections
from typing import List

# 这个算法现在 TLE 了
# class Solution:
#     def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
#         graph = collections.defaultdict(list)
#         for x, y in connections:
#             graph[x].append(y)
#             graph[y].append(x)
        
#         connSet = set()
#         for conn in connections:
#             connSet.add(tuple(sorted(conn)))
            
#         rank = [-2 for i in range(n)]
        
#         def dfs(cur, depth, n):
#             if rank[cur] >= 0: return rank[cur]
        
#             rank[cur] = depth
#             minBackDepth = n
#             for nxt in graph[cur]:
#                 # 不往回走，所以 rank 初始值不能设为 -1
#                 if rank[nxt] == depth - 1: continue
                
#                 backDepth = dfs(nxt, depth + 1, n)
#                 if backDepth <= depth:
#                     connSet.discard(tuple(sorted([cur,nxt])))
                    
#                 minBackDepth = min(minBackDepth, backDepth)
                
#             rank[cur] = n
#             return minBackDepth
            
            
#         dfs(0, 0, n)    
#         return list(connSet)

# Tarjan Algorithm
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        g = defaultdict(list)
        for u,v in connections:
            g[u].append(v)
            g[v].append(u)
            
        dfn = [None for i in range(n)]  # 表示当前结点
        low = [None for i in range(n)]  # 表示当前结点连接的结点中的最小深度
        out = []
        self.depth = 0
        def dfs(u,parent):                
            dfn[u] = low[u] = self.depth
            self.depth+=1
            for v in g[u]:
                if dfn[v] == None:
                    dfs(v,u)
                    if dfn[u] < low[v]: 
                        '''
                        low[x] = essentially a strongly connected network defined by the earliest node...
                        
                        
                        dfn[u] < low[v]
                        if depth of recursion of u is earlier than the "network of v defined by the earliest node,"
                        then its guaranteed that v is not reachable without the existing connection.
                        
                        dfn[u] >= low[v]
                        if depth of recursion of u is later than or equal to the "network of v defined by the earliest node,"
                        we know that u comes later than the network, so it is reachable
                        ''' 
                        out.append([u,v])

                if v!=parent: # one full loop means that there is a low point that wasn't the parent
                    low[u] = min(low[u],low[v])
        dfs(0,None)
        return out
