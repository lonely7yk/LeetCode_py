"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""

from typing import List
import heapq

# heap
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        heap = []
      
        # 把第一列所有的数先塞进 heap  
        for i in range(m):
            heapq.heappush(heap, (matrix[i][0], i, 0))
            
        cnt = 0
        while heap:
            num, x, y = heapq.heappop(heap)
            cnt += 1
            
            if cnt == k: return num
            # 每排出一个数，把那个数后面一个数塞进 heap
            if y + 1 < n: heapq.heappush(heap, (matrix[x][y + 1], x, y + 1))
                
        return -1
        
