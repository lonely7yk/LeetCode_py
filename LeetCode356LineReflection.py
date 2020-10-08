"""
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the 
given points symmetrically, in other words, answer whether or not if there exists a line that 
after reflecting all points over the given line the set of the original points is the same that 
the reflected ones.

Note that there can be repeated points.

Follow up:
Could you do better than O(n^2) ?

Example 1:

Input: points = [[1,1],[-1,1]]
Output: true
Explanation: We can choose the line x = 0.

Example 2:

Input: points = [[1,1],[-1,-1]]
Output: false
Explanation: We can't choose a line.
 

Constraints:

n == points.length
1 <= n <= 10^4
-10^8 <= points[i][j] <= 10^8
"""

from typing import List


# HashSet: O(n)
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        pointSet = set()
        minX = float('inf')
        maxX = float('-inf')
        
        for x, y in points:
            minX = min(minX, x)
            maxX = max(maxX, x)
            pointSet.add((x, y))
            
        twoMidX = minX + maxX
        for x, y in points:
            if (twoMidX - x, y) not in pointSet:
                return False
        
        return True
        
