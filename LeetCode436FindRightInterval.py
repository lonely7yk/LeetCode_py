"""
Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point 
is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the 
minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 
for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
 

Example 1:

Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
 

Example 2:

Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
 

Example 3:

Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new 
method signature.
"""

from typing import List
import bisect

# sort + binary search: O(nlogn) 55%
# 将 interval 的 (start, idx) 保存成一个 list，然后对 start 进行排序
# 然后对于每一个 interval，通过二分搜索找到比 interval[1]（即 end）大的第一个索引的位置，通过该索引可以找到 l 中 start 对应的原来的索引
# 如果索引等于 len(intervals) 说明找不到右侧区间，加入 -1
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = []
        l = sorted((interval[0], i) for i, interval in enumerate(intervals))

        for interval in intervals:
            idx = bisect.bisect_left(l, (interval[1], -1))
            res.append(l[idx][1] if idx < len(intervals) else -1)

        return res


intervals = [[3,4],[2,3],[1,2]]
res = Solution().findRightInterval(intervals)
print(res)
