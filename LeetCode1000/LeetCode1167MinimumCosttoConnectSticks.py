"""
You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  
You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

Example 1:

Input: sticks = [2,4,3]
Output: 14

Example 2:

Input: sticks = [1,8,3,5]
Output: 30
 

Constraints:

1 <= sticks.length <= 10^4
1 <= sticks[i] <= 10^4
"""

from typing import List
import heapq

# Heap: O(nlogn)
# 本质是哈夫曼编码
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = sticks
        heapq.heapify(heap)
        res = 0
        
        while len(heap) > 1:
            n1 = heapq.heappop(heap)
            n2 = heapq.heappop(heap)
            res += n1 + n2
            heapq.heappush(heap, n1 + n2)
            
        return res
        
