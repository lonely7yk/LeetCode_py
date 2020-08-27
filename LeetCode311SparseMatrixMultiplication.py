"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
 

Constraints:

1 <= A.length, B.length <= 100
1 <= A[i].length, B[i].length <= 100
-100 <= A[i][j], B[i][j] <= 100
"""

from typing import List
import collections


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m1, n1 = len(A), len(A[0])
        m2, n2 = len(B), len(B[0])
        res = [[0 for j in range(n2)] for i in range(m1)]
        
        graphA = collections.defaultdict(list)
        graphB = collections.defaultdict(list)
        
        # 用邻接表来存储所有节点的值
        for i in range(m1):
            for j in range(n1):
                if A[i][j]:
                    graphA[i].append((j, A[i][j]))
        
        for i in range(m2):
            for j in range(n2):
                if B[i][j]:
                    graphB[i].append((j, B[i][j]))
                    
        # res[x][z] = sum(A[x][y] * B[y][z])    0<=y<n1
        for x in graphA:
            for y, val1 in graphA[x]:
                for z, val2 in graphB[y]:
                    res[x][z] += val1 * val2
                    
        return res
        
