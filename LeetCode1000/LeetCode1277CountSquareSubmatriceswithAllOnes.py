"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""

from typing import List

# DP: O(m * n)  dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
# dp[i][j] means the size of biggest square with A[i][j] as bottom-right corner.
# dp[i][j] also means the number of squares with A[i][j] as bottom-right corner.
# class Solution:
#     def countSquares(self, matrix: List[List[int]]) -> int:
#         m, n = len(matrix), len(matrix[0])
#         dp = [[0 for j in range(n)] for i in range(m)]

#         res = 0
#         # 计算第一行的值
#         for i in range(m):
#             dp[i][0] = matrix[i][0]
#             res += dp[i][0]

#         # 计算第一列的值（排除 (0,0)，因为已经算过了）
#         for j in range(1, n):
#             dp[0][j] = matrix[0][j]
#             res += dp[0][j]

#         for i in range(1, m):
#             for j in range(1, n):
#                 # 只有在 matrix[i][j] 值为 1 时，dp[i][j] 才大于 0
#                 if matrix[i][j] == 1:
#                     dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
#                     res += dp[i][j]

#         return res

# improved: in-place method
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1

        return sum(map(sum, matrix))


matrix = [[1,0,1],[1,1,0],[1,1,0]]
res = Solution().countSquares(matrix)
print(res)


