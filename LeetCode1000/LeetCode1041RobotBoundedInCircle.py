"""
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:

Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:

Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.

Example 3:

Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

Note:

1 <= instructions.length <= 100
instructions[i] is in {'G', 'L', 'R'}
"""

# 满足两个条件之一可确认 robot 轨迹在一个圈内
# 1. robot 进行指令后仍保存在原来的坐标
# 2. robot 进行指令后方向与原方向不同
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        directIdx = 0
        
        for c in instructions:
            if c == "G":
                x += directions[directIdx][0]
                y += directions[directIdx][1]
            elif c == "L":
                directIdx = (directIdx - 1 + 4) % 4
            elif c == "R":
                directIdx = (directIdx + 1) % 4
                
        print(directIdx)
        return (x == 0 and y == 0) or directIdx != 0
        
        
