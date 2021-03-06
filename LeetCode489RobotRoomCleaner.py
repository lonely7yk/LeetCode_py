"""
Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made 
is 90 degrees.

When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays 
on the current cell.

Design an algorithm to clean the entire room using only the 4 given APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Example:

Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3

Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.

Notes:

- The input is only given to initialize the room and the robot's position internally. You must 
solve this problem "blindfolded". In other words, you must control the robot using only the 
mentioned 4 APIs, without knowing the room layout and the initial robot's position.
- The robot's initial position will always be in an accessible cell.
- The initial direction of the robot will be facing up.
- All accessible cells are connected, which means the all cells marked as 1 will be accessible 
by the robot.
- Assume all four edges of the grid are all surrounded by wall.
"""


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

# DFS
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # visited 表示走过的位置
        visited = set()

        # 表示从 x, y 开始往四个方向进行 clean，并且清理完后最后停留在原来的地方和原来的方向        
        # 0: up, 90: right, 180: down, 270: left
        def dfs(robot, x, y, curDir):
            if (x, y) in visited: return
            
            robot.clean()
            visited.add((x,y))
            
            # 转四个方向
            for i in range(4):
                if robot.move():
                    nxtX, nxtY = x, y
                    if curDir == 0:
                        nxtY += 1
                    elif curDir == 90:
                        nxtX += 1
                    elif curDir == 180:
                        nxtY -= 1
                    else:
                        nxtX -= 1
                        
                    dfs(robot, nxtX, nxtY, curDir)
                    # 把 robot 放回原来的位置，原来的方向
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                    
                # robot 转一个方向
                robot.turnRight()
                curDir += 90
                curDir %= 360
                
        dfs(robot, 0, 0, 0)
