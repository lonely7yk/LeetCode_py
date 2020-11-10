"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


# # Binary Search: O(nlogn)
# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if not matrix or not matrix[0]: return False
        
#         for line in matrix:
#             if line[0] > target: return False
            
#             idx = bisect.bisect_left(line, target)
#             if idx < len(line) and line[idx] == target: return True
            
#         return False


# 从右下向左上遍历，或从左上向右下遍历
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0

        while i >= 0 and j < n:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                return True

        return False

# class Solution:
#     def searchMatrix(self, matrix, target):
#         if not matrix or not matrix[0]: return False
        
#         m, n = len(matrix), len(matrix[0])
#         i, j = 0, n - 1

#         while i < m and j >= 0:
#             if matrix[i][j] < target:
#                 i += 1
#             elif matrix[i][j] > target:
#                 j -= 1
#             else:
#                 return True

#         return False

