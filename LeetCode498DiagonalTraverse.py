"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal 
order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

Note:

The total number of elements of the given matrix will not exceed 10,000.
"""

from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        
        m, n = len(matrix), len(matrix[0])
        res = []
        x, y = 0, 0
        dx, dy = -1, 1
        
        while len(res) < m * n:
            res.append(matrix[x][y])
            
            if y == n - 1 and dx == -1:
                x += 1
                dx, dy = 1, -1
            elif x == 0 and dx == -1:
                y += 1
                dx, dy = 1, -1
            elif x == m - 1 and dx == 1:
                y += 1
                dx, dy = -1, 1
            elif y == 0 and dx == 1:
                x += 1
                dx, dy = -1, 1
            else:
                x += dx
                y += dy
                
        return res
