"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, 
then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]

Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 
Constraints:

|x| + |y| <= 300
"""

import collections


# # BFS: unidirection 32%
# class Solution:
#     def minKnightMoves(self, x: int, y: int) -> int:
#         dq = collections.deque([(0,0,0)])
#         visited = set([(0,0)])
#         moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        
#         while dq:
#             cx, cy, step = dq.popleft()
#             if cx == x and cy == y: return step
            
#             for dx, dy in moves:
#                 nx, ny = cx + dx, cy + dy
                
#                 if (nx, ny) not in visited:
#                     visited.add((nx, ny))
#                     dq.append((nx, ny, step + 1))
                    
#         return -1
        

# # BFS: unidirection improved    72%
# class Solution:
#     def minKnightMoves(self, x: int, y: int) -> int:
#         x, y = abs(x), abs(y)   # make x and y positive
#         dq = collections.deque([(0,0,0)])
#         visited = set([(0,0)])
#         moves = [(1,2),(1,-2),(-1,2),(2,1),(2,-1),(-2,1)]  # no need (-1,-2) and (-2,-1)
        
#         while dq:
#             cx, cy, step = dq.popleft()
#             if cx == x and cy == y: return step
            
#             for dx, dy in moves:
#                 nx, ny = cx + dx, cy + dy
                
#                 if (nx, ny) not in visited and -1 <= nx <= x + 2 and -1 <= ny <= y + 2:
#                     visited.add((nx, ny))
#                     dq.append((nx, ny, step + 1))
                    
#         return -1

# BFS: bidirection  74%
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)   # make x and y positive
        dq1 = collections.deque([(0,0,0)])
        dq2 = collections.deque([(x,y,0)])
        do = {(0,0): 0}
        dt = {(x,y): 0}
        moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        
        while dq1 and dq2:
            ocx, ocy, ostep = dq1.popleft()
            if (ocx, ocy) in dt: return ostep + dt[(ocx, ocy)]
            tcx, tcy, tstep = dq2.popleft()
            if (tcx, tcy) in do: return tstep + do[(tcx, tcy)]
            
            for dx, dy in [(1,2),(1,-2),(-1,2),(2,1),(2,-1),(-2,1)]:      # no need (-1,-2) and (-2,-1)
                onx, ony = ocx + dx, ocy + dy
                
                if (onx, ony) not in do and -1 <= onx <= x + 2 and -1 <= ony <= y + 2:
                    do[(onx, ony)] = ostep + 1
                    dq1.append((onx, ony, ostep + 1))

            for dx, dy in [(1,-2),(-1,2),(-1,-2),(2,-1),(-2,1),(-2,-1)]:      # no need (1,2) and (2,1)
                tnx, tny = tcx + dx, tcy + dy

                if (tnx, tny) not in dt and -1 <= tnx <= x + 2 and -1 <= tny <= y + 2:
                    dt[(tnx, tny)] = tstep + 1
                    dq2.append((tnx, tny, tstep + 1))

        return -1

