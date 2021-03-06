"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""

from typing import List

# O(n) : use cross product instead of division
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2: return True

        dy = coordinates[1][1] - coordinates[0][1]
        dx = coordinates[1][0] - coordinates[0][0]

        for i in range(2, len(coordinates)):
            dy2 = coordinates[i][1] - coordinates[i - 1][1]
            dx2 = coordinates[i][0] - coordinates[i - 1][0]

            if (dy2 * dx) != (dx2 * dy): return False

        return True

# coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
res = Solution().checkStraightLine(coordinates)
print(res)
