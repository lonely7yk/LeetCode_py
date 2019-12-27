"""
Given n non-negative integers representing the histogram's bar height 
where the width of each bar is 1, find the area of largest rectangle 
in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""

from typing import List

class Solution:
    # # brute force: O(n^2): TLE
    # # 对于每一个高度 height，其最大面积为 (rightFlag - leftFlag + 1) * height
    # # leftFlag 是在 height 左侧不小于 height 的最远位置
    # # rightFlag 是在 height 右侧不小于 height 的最远位置
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     n = len(heights)
    #     maxArea = 0

    #     for i in range(n):
    #         leftFlag = i
    #         rightFlag = i
    #         height = heights[i]

    #         while leftFlag > 0:
    #             if heights[leftFlag - 1] < height:
    #                 break
    #             leftFlag -= 1

    #         while rightFlag < n - 1:
    #             if heights[rightFlag + 1] < height:
    #                 break
    #             rightFlag += 1

    #         maxArea = max(maxArea, (rightFlag - leftFlag + 1) * height)

    #     return maxArea

    # # DP: 116ms 66.75%
    # # 参考：https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28902/5ms-O(n)-Java-solution-explained-(beats-96)
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     if not heights or len(heights) == 0: return 0

    #     n = len(heights)
    #     lessFromLeft = [0] * n      # 在 height[i] 左侧，比height[i]小的第一个索引
    #     lessFromRight = [0] * n     # 在 height[i] 右侧，比height[i]小的第一个索引
    #     maxArea = 0
    #     lessFromLeft[0] = -1
    #     lessFromRight[n - 1] = n

    #     for i in range(1, n):
    #         p = i - 1
    #         while p >= 0 and heights[p] >= heights[i]:
    #             p = lessFromLeft[p]
    #         lessFromLeft[i] = p

    #     for i in reversed(range(n - 1)):
    #         p = i + 1
    #         while p < n and  heights[p] >= heights[i]:
    #             p = lessFromRight[p]
    #         lessFromRight[i] = p

    #     for i in range(n):
    #         maxArea = max(maxArea, (lessFromRight[i] - lessFromLeft[i] - 1) * heights[i])

    #     return maxArea

    # stack: O(n) 116ms 66%
    # stack 保存索引，在 stack 加入新索引前判断最后一个高度是否大于新加入的高度，如果是则先 pop 计算最后一个高度的最大面积后 append
    # stack 中保存的为升序高度的索引
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights or len(heights) == 0: return 0

        heights.append(0)
        stack = [-1]
        maxArea = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                h = heights[idx]
                # i - 1 表示最后一个大于 h 的索引，stack[-1] 表示第一个大于 h 的索引的前面一个索引
                maxArea = max(maxArea, (i - 1 - stack[-1]) * h)
            stack.append(i)

        return maxArea


if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    res = Solution().largestRectangleArea(heights)
    print(res)
