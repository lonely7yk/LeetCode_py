"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""

from typing import List


# 按照 (x,y) 进行排序后，四个点的顺序为 (0,1,3,2) 直接验证四条边相当且对角线相等且不等于0即可
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(point1, point2):
            return (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2
        
        def check(p):
            return dist(p[0], p[1]) > 0 and dist(p[0], p[1]) == dist(p[1], p[3]) and dist(p[1], p[3]) == dist(p[3], p[2]) and dist(p[3], p[2]) == dist(p[2], p[0]) and dist(p[0], p[3]) == dist(p[1], p[2])
        
        p = [p1, p2, p3, p4]
        p.sort(key=lambda x: (x[0], x[1]))
        
        return check(p)
        
        
