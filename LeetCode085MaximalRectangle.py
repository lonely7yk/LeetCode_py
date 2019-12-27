"""
Given a 2D binary matrix filled with 0's and 1's, find the largest 
rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

from typing import List

class Solution:
    # # DP: O(n^2) 220ms 64%
    # # 完全参考 LeetCode084，把矩阵的每一行都看成是一个 Largest Rectanglein Histogram 问题
    # def maximalRectangle(self, matrix: List[List[str]]) -> int:
    #     if not matrix or len(matrix) == 0 or len(matrix[0]) == 0: return 0

    #     row = len(matrix)
    #     col = len(matrix[0])
    #     maxArea = 0
    #     heights = [0] * col

    #     for i in range(row):
    #         # 计算该行作为底座的高度
    #         for j in range(col):
    #             if matrix[i][j] == '1': heights[j] += 1
    #             else: heights[j] = 0

    #         lessFromLeft = [-1] * col   # 表示从 i 左边，第一个小于 heights[j] 的索引
    #         for j in range(1, col):
    #             p = j - 1
    #             while p >= 0 and heights[p] >= heights[j]:
    #                 p = lessFromLeft[p]
    #             lessFromLeft[j] = p

    #         lessFromRight = [col] * col # 表示从 i 右边，第一个小于 heights[j] 的索引
    #         for j in reversed(range(col - 1)):
    #             p = j + 1
    #             while p < col and heights[p] >= heights[j]:
    #                 p = lessFromRight[p]
    #             lessFromRight[j] = p

    #         # 计算这行的所有面积
    #         for j in range(col):
    #             maxArea = max(maxArea, heights[j] * (lessFromRight[j] - lessFromLeft[j] - 1))

    #     return maxArea

    # stack: 200ms 92.71%
    # 同上，完全参考084
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0: return 0

        row = len(matrix)
        col = len(matrix[0])
        heights = [0] * (col + 1)
        maxArea = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1': heights[j] += 1
                else: heights[j] = 0

            stack = [-1]
            for j in range(col + 1):
                while heights[j] < heights[stack[-1]]:
                    idx = stack.pop()
                    h = heights[idx]
                    maxArea = max(maxArea, h * (j - 1 - stack[-1]))
                stack.append(j)

        return maxArea

if __name__ == '__main__':
    matrix = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]

    res = Solution().maximalRectangle(matrix)
    print(res)

