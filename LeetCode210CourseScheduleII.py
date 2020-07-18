"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""

from typing import List
import collections

# Topo Sort -- BFS
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         graph = collections.defaultdict(list)
#         indegree = [0 for i in range(numCourses)]
#         visited = set()
#         res = []
        
#         for a, b in prerequisites:
#             graph[b].append(a)
#             indegree[a] += 1
        
#         dq = collections.deque()
#         for i in range(numCourses):
#             if indegree[i] == 0:
#                 dq.append(i)
        
#         while dq:
#             node = dq.popleft()
#             res.append(node)
            
#             for nxt in graph[node]:
#                 indegree[nxt] -= 1
#                 if indegree[nxt] == 0:
#                     dq.append(nxt)
                    
#         return res if len(res) == numCourses else []

# Topo Sort -- DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(curr, graph, visited, stack):
            if visited[curr] == -1: return False
            if visited[curr] == 1: return True

            visited[curr] = -1

            for nxt in graph[curr]:
                if not dfs(nxt, graph, visited, stack): return False

            visited[curr] = 1
            # 会优先把没有出度的节点放入 stack，所以 stack 的逆序输出就是最终结果
            stack.append(curr)
            return True

        graph = collections.defaultdict(list)
        visited = [0 for i in range(numCourses)]
        stack = []

        for course, pre in prerequisites:
            graph[pre].append(course)

        for i in range(numCourses):
            if not dfs(i, graph, visited, stack): return None

        return list(reversed(stack))

        
