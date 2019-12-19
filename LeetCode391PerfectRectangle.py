'''
Given N axis-aligned rectangles where N > 0, determine if they all together 
form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. 
For example, a unit square is represented as [1,1,2,2]. (coordinate of 
bottom-left point is (1, 1) and top-right point is (2, 2)).

Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
'''

from typing import List

class Solution:
    # # brute force: TLE
    # # 用方块的最左下坐标表示每个最小方块的，算出整个图形的最左下坐标和最右上坐标，如果其中的方块和allRectSet中的一致则返回True
    # def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
    #     mostLeftBottom = [float('inf'), float('inf')]
    #     mostRightTop = [float('-inf'), float('-inf')]
    #     allRectSet = set()

    #     for rect in rectangles:
    #         for i in range(rect[0], rect[2]):
    #             for j in range(rect[1], rect[3]):
    #                 if (i, j) in allRectSet:
    #                     return False
                    
    #                 allRectSet.add((i, j))
    #                 if i < mostLeftBottom[0]:
    #                     mostLeftBottom = (i, j)
    #                 elif i == mostLeftBottom[0] and j < mostLeftBottom[1]:
    #                     mostLeftBottom = (i, j)

    #                 if i > mostRightTop[0]:
    #                     mostRightTop = (i, j)
    #                 elif i == mostRightTop[0] and j > mostRightTop[1]:
    #                     mostRightTop = (i, j)

    #     for i in range(mostLeftBottom[0], mostRightTop[0] + 1):
    #         for j in range(mostLeftBottom[1], mostRightTop[1] + 1):
    #             if (i, j) not in allRectSet:
    #                 return False

    #             allRectSet.remove((i, j))

    #     return len(allRectSet) == 0

    # 404ms 62%
    # 参考：https://leetcode.com/problems/perfect-rectangle/discuss/87181/Really-Easy-Understanding-Solution(O(n)-Java)
    # 三种情况会返回 False
    # 1. 最外围节点不在cornersSet，或最外围节点出现1次以上
    # 2. 最外围交点组成矩形面积 != 所有rectangles加起来的面积
    # 3. 有任意两个rect有重叠部分
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 表示最左下坐标和最右上坐标
        x1, y1, x2, y2 = float('inf'), float('inf'), float('-inf'), float('-inf')
        area = 0    # 表示所有 rectangles 的总面积
        cornersSet = set()  

        for rect in rectangles:
            x1 = min(x1, rect[0])
            y1 = min(y1, rect[1])
            x2 = max(x2, rect[2])
            y2 = max(y2, rect[3])

            area += (rect[2] - rect[0]) * (rect[3] - rect[1])

            corners = [(rect[0], rect[1]), (rect[0], rect[3]), (rect[2], rect[3]), (rect[2], rect[1])]
            # 这一步的目的是去除偶数个的相同交点
            for corner in corners:  
                if corner in cornersSet:
                    cornersSet.remove(corner)
                else:
                    cornersSet.add(corner)

        # len(cornersSet) != 4 是为了防止一个rect出现在另一个rect的内部的情况，或者两个rect有重叠部分
        if (x1, y1) not in cornersSet or (x1, y2) not in cornersSet or (x2, y1) not in cornersSet \
            or (x2, y2) not in cornersSet or len(cornersSet) != 4:
            return False

        return area == (x2 - x1) * (y2 - y1)

if __name__ == '__main__':
    solution = Solution()
    # rectangles = [
    #   [1,1,3,3],
    #   [3,1,4,2],
    #   [3,2,4,4],
    #   [1,3,2,4],
    #   [2,3,3,4]
    # ]

    rectangles = [
      [1,1,2,3],
      [1,3,2,4],
      [3,1,4,2],
      [3,2,4,4]
    ]
    print(solution.isRectangleCover(rectangles))
