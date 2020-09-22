"""
You are driving a vehicle that has capacity empty seats initially available for passengers.  
The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains 
information about the i-th trip: the number of passengers that must be picked up, and the 
locations to pick them up and drop them off.  The locations are given as the number of 
kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all 
the given trips. 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true

Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true

Constraints:

trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000
"""

from typing import List
import heapq


# # Sort + Heap: O(nlogn)
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         # trip 按照 start 位置排序
#         trips.sort(key=lambda x: x[1])
#         heap = []
#         currCap = capacity  # 当前还剩下多少空位
        
#         for trip in trips:
#             # 如果 heap 不为空，heappop 直到所有已经路过的位置都空出来
#             if heap:
#                 while heap and heap[0][0] <= trip[1]:
#                     _, cap = heapq.heappop(heap)
#                     currCap += cap
                
#                 # 如果当前空位不够直接返回 False    
#                 if trip[0] > currCap: return False
                
#             heapq.heappush(heap, (trip[2], trip[0]))
#             currCap -= trip[0]
            
#         return True


# # Sort: O(nlogn)
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         timestamps = []
#         for trip in trips:
#             timestamps.append([trip[1], trip[0]])   # 表示上车
#             timestamps.append([trip[2], -trip[0]])  # 表示下车

#         currCap = capacity
#         timestamps.sort()   # 注意下车排在上车前面
#         for timestamp in timestamps:
#             currCap -= timestamp[1]
#             if currCap < 0: return False

#         return True


# Bucket Sort: O(max(n, 1001))
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamps = [0 for i in range(1001)]
        
        for cap, start, end in trips:
            timestamps[start] += cap
            timestamps[end] -= cap
            
        currCap = capacity
        for changeCap in timestamps:
            currCap -= changeCap
            if currCap < 0: return False
            
        return True
