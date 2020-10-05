"""
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays 
(each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute 
difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4

Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
"""

from typing import List
import heapq


# # Heap: O(n)
# class Solution:
#     def maxDistance(self, arrays: List[List[int]]) -> int:
#         minHeap = []
#         maxHeap = []
        
#         for i, array in enumerate(arrays):
#             minHeap.append((array[0], i))
#             maxHeap.append((-array[-1], i))
            
#         heapq.heapify(minHeap)
#         heapq.heapify(maxHeap)
        
#         min1, i = minHeap[0]
#         max1, j = maxHeap[0]
        
#         if i != j:
#             # 如果 max1 和 min1 来自于不同 array，直接返回 max - min
#             return -max1 - min1
#         else:
#             # 否则，分别找另一个 min2 和 max2，计算 max(max2-min1, max1-min2)
#             heapq.heappop(minHeap)
#             heapq.heappop(maxHeap)
            
#             min2, _ = minHeap[0]
#             max2, _ = maxHeap[0]
            
#             return max(-max2 - min1, -max1 - min2)


# One pass: O(n)
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        curMin = float('inf')
        curMax = float('-inf')

        for array in arrays:
            res = max(res, curMax - array[0], array[-1] - curMin)

            curMin = min(curMin, array[0])
            curMax = max(curMax, array[-1])

        return res
  
        
