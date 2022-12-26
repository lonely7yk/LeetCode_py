"""
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.


Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
 

Constraints:

1 <= events.length <= 10^5
events[i].length == 2
1 <= startDayi <= endDayi <= 10^5
"""

from typing import List
import heapq


# Sort + Heap: O(d + nlogn)
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: (x[0], x[1]))
        heap = []
        idx = 0
        n = len(events)
        res = 0

        for i in range(1, 100001):
            while heap and heap[0] < i:
                heapq.heappop(heap)

            while idx < n and events[idx][0] == i:
                heapq.heappush(heap, events[idx][1])
                idx += 1

            if heap:
                heapq.heappop(heap)
                res += 1

        return res


events = [[1,2],[2,3],[3,4]]
res = Solution().maxEvents(events)
print(res)

