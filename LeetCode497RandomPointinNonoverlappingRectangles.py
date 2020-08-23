"""
Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which 
randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:

An integer point is a point that has integer coordinates. 
A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the 
bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
length and width of each rectangle does not exceed 2000.
1 <= rects.length <= 100
pick return a point as an array of integer coordinates [p_x, p_y]
pick is called at most 10000 times.

Example 1:

Input: 
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output: 
[null,[4,1],[4,1],[3,3]]

Example 2:

Input: 
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output: 
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one 
argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with 
a list, even if there aren't any.
"""

from typing import List

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.tot = 0
        self.preSum = []
        
        for x in rects:
            area = (x[2] - x[0] + 1) * (x[3] - x[1] + 1)
            self.tot += area
            self.preSum.append(self.tot)

    def pick(self) -> List[int]:
        target = random.randrange(0, self.tot)
        left = 0
        right = len(self.preSum) - 1
        
        while left < right:
            mid = (left + right) // 2
            if self.preSum[mid] > target:
                right = mid
            else:
                left = mid + 1
                
        x = self.rects[left]
        width = x[2] - x[0] + 1
        height = x[3] - x[1] + 1
        leftArea = target - (self.preSum[left] - width * height)
        return [x[0] + leftArea % width, x[1] + leftArea // width]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()