"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to 
one connecting line.

Return the maximum number of connecting lines we can draw in this way.

Example 1:

1 4 2
|  \
1 2 4

Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line 
from A[2]=2 to B[1]=2.

Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3

Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
 

Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000
"""

from typing import List

# # DFS+memo
# class Solution:
#     def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
#         memo = dict()

#         def dfs(A, B, idx1, idx2):
#             if idx1 == len(A) or idx2 == len(B): return 0
#             if (idx1,idx2) in memo: return memo[(idx1,idx2)]

#             res = 0
#             for i in range(idx1, len(A)):
#                 for j in range(idx2, len(B)):
#                     if A[i] == B[j]:
#                         res = max(res, 1 + dfs(A, B, i + 1, j + 1))

#             memo[(idx1,idx2)] = res
#             return res

#         return dfs(A, B, 0, 0)

# # DP: O(n^2)
# # A[i] == B[j] : dp[i][j] = dp[i - 1][j - 1] + 1
# # otherwise    : dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
# class Solution:
#     def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
#         m,n = len(A),len(B)
#         # dp[i][j] 表示 A 中 [0,i] 和 B 中 [0,j] 中的最多 uncrossedline 数量
#         dp = [[0 for j in range(n)] for i in range(m)]

#         # 边界条件
#         for i in range(m):
#             if A[i] == B[0]:
#                 for x in range(i, m):
#                     dp[x][0] = 1
#                 break

#         for j in range(n):
#             if A[0] == B[j]: 
#                 for y in range(j, n):
#                     dp[0][y] = 1
#                 break

#         for i in range(1, m):
#             for j in range(1, n):
#                 if A[i] == B[j]:
#                     dp[i][j] = dp[i - 1][j - 1] + 1
#                 else:
#                     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

#         return dp[-1][-1]

# DP improved: 不需要额外考虑边界条件
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m,n = len(A),len(B)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)] 

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


A = [1,4,2]
B = [1,2,4]

# A = [2,5,1,2,5]
# B = [10,5,2,1,5,2]

# A = [1,3,7,1,7,5]
# B = [1,9,2,5,1]
res = Solution().maxUncrossedLines(A, B)
print(res)
