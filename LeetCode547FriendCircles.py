"""
There are N students in a class. Some of them are friends, while some are not. Their friendship 
is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, 
then A is an indirect friend of C. And we defined a friend circle is a group of students who are 
direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. 
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
 

Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

Constraints:

1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]
"""

from typing import List


# # Union Find: O(n^2)
# class Solution:
#     def findCircleNum(self, M: List[List[int]]) -> int:
#         def find(roots, x):
#             if x == roots[x]:
#                 return x
#             else:
#                 roots[x] = find(roots, roots[x])
#                 return roots[x]
        
#         n = len(M)
#         cnt = n
#         roots = list(range(n))
#         size = [1 for i in range(n)]
        
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if M[i][j] == 1:
#                     root1 = find(roots, i)
#                     root2 = find(roots, j)
                    
#                     if root1 != root2:
#                         if size[root1] > size[root2]:
#                             roots[root2] = root1
#                             size[root1] += size[root2]
#                         else:
#                             roots[root1] = root2
#                             size[root2] += size[root1]
                            
#                         cnt -= 1
                            
#         return cnt
        
# DFS: O(n^2)
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(visited, M, i):
            for j in range(len(M)):
                # 如果 i 和 j 有关系，且 j 没被访问过，用 dfs 访问所有关联节点
                if M[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(visited, M, j)
                
        
        n = len(M)
        visited = [False for i in range(n)]
        cnt = 0
        
        for i in range(n):
            if visited[i] == False:
                dfs(visited, M, i)
                cnt += 1
                
        return cnt