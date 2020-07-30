"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed 
from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape 
photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri 
are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is 
guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect 
rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] 
that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last 
key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has 
zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

- The number of buildings in any input list is guaranteed to be in the range [0, 10000].
- The input list is already sorted in ascending order by the left x position Li.
- The output list must be sorted by the x position.
- There must be no consecutive horizontal lines of equal height in the output skyline. For instance, 
[...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be 
merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
"""

from typing import List
import heapq

# heap: O(nlogn)
# 用 heap 来存储每个矩形的高度和其右边界。堆顶元素表示到当前 x 坐标的最大高度
# 从左到右扫描，每当有一条边扫描到
    # 如果这是左边界，判断对应的高度和 heap 中的最高高度谁高
        # 如果当前高度比 heap 堆顶高度更高，那么添加 (左边界，高度)到 res，并把 （高度，右边界）添加到 heap 中
        # 否则，不添加，并把 （高度，右边界）添加到 heap 中
        # 对上面进行总结，可以直接把 （高度，右边界）添加到 heap 中，然后判断 res[-1] 的高度是否等于 heap[0] 中的高度，如果不等于则更新
    # 如果这是右边界，不添加到 heap，判断 heap 最高高度是否
        # 如果变化，添加（左边界，heap 当前最高高度）到 res 中
        # 否则，不添加
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(L, -H, R) for L, R, H in buildings]  # 左侧的边，高度以 H 从大到小排序
        events += list({(R, 0, 0) for _, R, _ in buildings})  # 右侧的边（只存储边的位置），为了防止重复，使用 set
        events.sort()

        res = [[0,0]]               # [x, h]
        heap = [(0, float('inf'))]  # [height, endingPoint]

        for pos, negH, R in events:
            while pos >= heap[0][1]: heapq.heappop(heap)    # pos >= heap[0][1] 说明，已经横坐标已经过了这个点了。确保堆顶的一定是当前坐标有效的高度
            if negH: heapq.heappush(heap, (negH, R))    # 如果 negH 不为 0，说明这是左侧边，加入到 heap 中
            if res[-1][1] != -heap[0][0]:               # heap 最高高度和 res 上一个添加的高度不一致，说明这一定是一个轮廓点
                res += [[pos, -heap[0][0]]]

        return res[1:]

# # 5% 这种方法太慢了，主要右边界从堆中删除以后还要进行堆化
# class Solution:
#     def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
#         events = []
#         events += [(L, -H) for L, _, H in buildings]
#         events += [(R, H) for _, R, H in buildings]

#         events.sort()
#         heap = [0]
#         res = [[0, 0]]

#         # print(events)

#         for pos, H in events:
#             if H < 0:
#                 # 左边界直接 push
#                 heapq.heappush(heap, H)
#             else:
#                 # 右边界 remove 以后堆化
#                 heap.remove(-H)
#                 heapq.heapify(heap)

#             # 如果 heap 最大高度和之前添加的不同，则把 (pos,-heap[0]) 加入 res
#             if -heap[0] != res[-1][1]:
#                 res.append([pos, -heap[0]])

#         return res[1:]


buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
res = Solution().getSkyline(buildings)
print(res)

