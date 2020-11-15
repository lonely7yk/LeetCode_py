"""
Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.

We remove the intersections between any interval in intervals and the interval toBeRemoved.

Return a sorted list of intervals after all such removals.

Example 1:

Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]

Example 2:

Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]

Example 3:

Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
Output: [[-5,-4],[-3,-2],[4,5],[8,9]]

Constraints:

1 <= intervals.length <= 10^4
-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9
"""

from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        r1, r2 = toBeRemoved
        res = []
        
        for x1, x2 in intervals:
            # removeInterval 和 interval 没有交集
            if x2 <= r1 or x1 >= r2:
                res.append([x1, x2])
            # interval 在 removeInterval 内部
            elif x1 >= r1 and x2 <= r2:
                continue
            # removeInterval 在 interval 内部
            elif x1 < r1 and x2 > r2:
                res.append([x1, r1])
                res.append([r2, x2])
            elif x1 < r1 and r1 < x2 <= r2:
                res.append([x1, r1])
            elif x2 > r2 and r1 <= x1 < r2:
                res.append([r2, x2])
                
        return res
        
