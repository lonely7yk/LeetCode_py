"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

from typing import List

# Greedy
# No-overlapping Problem
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        # 当前合并区间的 start
        currStart = intervals[0][0]
        # 当前合并区间的 end
        currEnd = intervals[0][1]
        res = []
        
        for i in range(1, n):
            if intervals[i][0] <= currEnd:
                currEnd = max(currEnd, intervals[i][1])
            else:
                res.append([currStart, currEnd])
                currStart = intervals[i][0]
                currEnd = intervals[i][1]
                
        # 记得加上最后一个合并区间
        res.append([currStart, currEnd])
        return res
        
