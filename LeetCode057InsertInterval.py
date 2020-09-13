"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

from typing import List

# O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        idx = 0
        n = len(intervals)
        
        while idx < n:
            interval = intervals[idx]

            if newInterval[0] <= interval[1] and newInterval[1] >= interval[0]:
                # 如果 interval 和 newInterval 有交集，就更新 newInterval
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                # 如果没有交集
                if newInterval[0] > interval[1]:
                    # 如果 newInterval 在 interval 后面，就直接添加 interval（因为后面可能有交集）
                    res.append(interval)
                else:
                    # 如果 newInterval 在 interval 前面，那 newInterval 在后面都不会有交集了，直接添加 newInterval
                    res.append(newInterval)
                    break
            idx += 1
        
        if idx != n:
            # 如果 idx 没有遍历完，说明提前添加了 newInterval，只要把剩下的 interval 添加进 res 即可
            res.extend(intervals[idx:])
        else:
            # 如果 idx 遍历完了，那么 newInterval 还没有加入到 res 中，添加 newInterval
            res.append(newInterval)
        return res
            
        
