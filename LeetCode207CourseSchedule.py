"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have 
to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it 
possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is 
             possible.

Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to 
             take course 0 you should also have finished course 1. So it 
             is impossible.

Note:

1. The input prerequisites is a graph represented by a list of edges, not 
adjacency matrices. Read more about how a graph is represented.
2. You may assume that there are no duplicate edges in the input prerequisites.
"""

from typing import List
import collections

class Solution:
    # Topo Sort(DFS): 92ms 96%
    # DAG 问题
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, graph, visited):
            # 如果访问过了，又进入该结点说明从该结点进入无环
            if visited[i] == 1: return True
            # 如果访问过中，又进入该结点说明从该结点进入有环
            if visited[i] == -1: return False

            visited[i] = -1     # -1 表示访问中

            for k in graph[i]:
                if not dfs(k, graph, visited): return False

            visited[i] = 1      # 1 表示已经访问过
            return True

        if numCourses == 0 or numCourses == 1: return True

        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        for prerequisite in prerequisites:
            course, pre = prerequisite[0], prerequisite[1]
            graph[course].append(pre)

        for i in range(numCourses):
            if not dfs(i, graph, visited): return False

        return True

    # # Topo Sort(BFS): 132ms 27%
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     graph = [[] for _ in range(numCourses)]
    #     indegree = [0 for _ in range(numCourses)]

    #     for prerequisite in prerequisites:
    #         course, pre = prerequisite[0], prerequisite[1]
    #         graph[course].append(pre)
    #         indegree[pre] += 1

    #     queue = collections.deque()
    #     for i in range(len(indegree)):
    #         if indegree[i] == 0:
    #             queue.append(i)

    #     res = 0

    #     while queue:
    #         idx = queue.popleft()   # 入度为 1 的节点
    #         res += 1

    #         for node in graph[idx]:
    #             indegree[node] -= 1
    #             if indegree[node] == 0:
    #                 queue.append(node)

    #     return res == numCourses





