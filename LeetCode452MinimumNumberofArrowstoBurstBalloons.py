"""
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is 
the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter 
and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. 
There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and 
xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be 
shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows 
that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""

from typing import List

# Greedy
# 和 435 Non-overlapping Intervals 非常相似，本质是找最多有多少个非重叠区间
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        
        n = len(points)
        points.sort(key=lambda x: x[1])
        cnt = 1
        
        currEnd = points[0][1]
        for i in range(1, n):
            if points[i][0] > currEnd:
                cnt += 1
                currEnd = points[i][1]
                
        return cnt
        
