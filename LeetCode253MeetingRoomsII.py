"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
(si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""

from typing import List
import heapq

# # O(nlogn) - O(n)
# # 不关注 start 和 end 的对应关系，只关注每个 end 前有多少个 start，每多一个 start 就会多一个 room，
# # 如果 start 大于当前 end，表示当前 end 对应的 room 已经空出来了，只需要更新 end 即可，不用添加 room
# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         if not intervals: return 0

#         n = len(intervals)
        
#         # 所有 interval 开始时间的排序
#         startTimings = sorted([interval[0] for interval in intervals])
#         # 所有 interval 结束时间的排序
#         endTimings = sorted([interval[1] for interval in intervals])

#         startPoint = 0
#         endPoint = 0
#         res = 0     # 表示使用 room 的数量

#         while startPoint < n:
#             if startTimings[startPoint] < endTimings[endPoint]:
#                 res += 1        # 表示在房间空出来前又来了一节课，这课时候要添加房间
#             else:
#                 endPoint += 1   # 表示有一间房间空了出来，不需要新加 room 了

#             startPoint += 1

#         return res

# Heap: O(nlogn) - O(n)
# 这个就好理解好多了。interval 先按照 start 排序。然后定义一个 min heap，存的是 interval 的 end。
# 对于每一个 interval，如果 start 大于等于 heap 堆顶的 end，说明这个 start 可以用当前的 room，直接替换堆顶的 end 为当前 interval 的 end
# 否则，说明没有空的 room，需要再添加一个 room。最后只要看 heap 的长度就可以知道教室的数量
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = []

        for interval in intervals:
            if heap and interval[1] >= heap[0]:
                heapq.heapreplace(heap, interval[1])
            else:
                heapq.heappush(heap, interval[1])

        return len(heap)


intervals = [[2,15],[36,45],[9,29],[16,23],[4,9]]
res = Solution().minMeetingRooms(intervals)
print(res)
