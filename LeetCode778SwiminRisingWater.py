"""
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 
4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can 
swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].
"""

from typing import List


# Heap: O(n^2 * logn)   100ms
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        res = 0
        
        while heap:
            h, x, y = heapq.heappop(heap)
            res = max(res, h)
            if x == n - 1 and y == n - 1: return res
            
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    heapq.heappush(heap, (grid[nx][ny], nx, ny))
        
        return -1


# # DFS + Binary Search: O(n^2 * logn)   248ms
# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         def dfs(x, y, h, seen):
#             if x < 0 or x >= n or y < 0 or y >= n: return False
#             if (x, y) in seen: return False
#             if grid[x][y] > h: return False
#             if x == n - 1 and y == n - 1: return True
            
#             seen.add((x, y))
#             for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
#                 if dfs(nx, ny, h, seen): return True

#             # 这里不要 remove
#             # seen.remove((x, y))
                
#             return False
            
        
#         n = len(grid)
#         left = 0
#         right = n * n
        
#         while left < right:
#             mid = (left + right) // 2
#             if dfs(0, 0, mid, set()):
#                 right = mid
#             else:
#                 left = mid + 1
                
#         return left
        
        


