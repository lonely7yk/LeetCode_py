"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""

from typing import List
import heapq


# # max heap: O(nlogk)
# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         heap = []
#
#         for point in points:
#             dis = point[0] * point[0] + point[1] * point[1]
#             heapq.heappush(heap, (-dis, point[0], point[1]))
#             if len(heap) > K:
#                 heapq.heappop(heap)
#
#         res = [[x[1], x[2]] for x in heap]
#         return res

# quick sort: O(nlogn)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def compare(p1, p2):
            return p1[0] * p1[0] + p1[1] * p1[1] - p2[0] * p2[0] - p2[1] * p2[1]

        def partition(points, left, right):
            pivot = points[left]
            pl = left
            pr = right

            while pl < pr:
                while compare(pivot, points[pr]) <= 0 and pl < pr: pr -= 1
                while compare(pivot, points[pl]) >= 0 and pl < pr: pl += 1

                if pl < pr:
                    points[pl], points[pr] = points[pr], points[pl]
                else:
                    points[left], points[pr] = points[pr], points[left]

            return pr

        left = 0
        right = len(points) - 1

        while left < right:
            mid = partition(points, left, right)
            if mid < K:
                left = mid + 1
            elif mid > K:
                right = mid - 1
            else:
                break

        return points[:K]


points = [[3,3],[5,-1],[-2,4]]
K = 2
res = Solution().kClosest(points, K)
print(res)
