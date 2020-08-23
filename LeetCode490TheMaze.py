"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by 
rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball 
stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could 
stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You 
may assume that the borders of the maze are all walls. The start and destination coordinates are 
represented by row and column indexes.

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""

from typing import List

# DFS
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def dfs(x, y, visited, target):
            if visited[x][y]: return False
            if x == target[0] and y == target[1]: return True
            
            # 只要走过这个点，以后就不重复走了，因为结果都是一样的
            visited[x][y] = True
            m, n = len(maze), len(maze[0])
            # 分别表示向左、右、上、下各自最远能走到哪里（受限于边界和 wall）
            l, r, u, d = y, y, x, x
            
            while l - 1 >= 0 and maze[x][l - 1] == 0: l -= 1
            while r + 1 < n and maze[x][r + 1] == 0: r += 1
            while u - 1 >= 0 and maze[u - 1][y] == 0: u -= 1
            while d + 1 < m and maze[d + 1][y] == 0: d += 1
                
            for nxtX, nxtY in ((x, l), (x, r), (u, y), (d, y)):
                if dfs(nxtX, nxtY, visited, target): return True
                
            return False
                
        m, n = len(maze), len(maze[0])
        visited = [[False for j in range(n)] for i in range(m)]
        return dfs(start[0], start[1], visited, destination)
                
        
