"""
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""

from typing import List

# # DP: O(n^2) 4264ms 5%
# class Solution:
#     def numberOfArithmeticSlices(self, A: List[int]) -> int:
#         n = len(A)
#         cnt = 0
#         dp = [[False for j in range(n)] for i in range(n)]
        
#         for i in range(n):
#             dp[i][i] = True
#             if i <= n - 2:
#                 dp[i][i + 1] = True
                
#         for l in range(3, n + 1):
#             for i in range(n - l + 1):
#                 j = i + l - 1
#                 dp[i][j] = (dp[i][j - 1] and A[j] - A[j - 1] == A[j - 1] - A[j - 2]) \
#                     or (dp[i + 1][j] and A[i + 2] - A[i + 1] == A[i + 1] - A[i])
#                 if dp[i][j]:
#                     cnt += 1
                    
#         return cnt
                
# Greedy: O(n) 32ms 86%
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A or len(A) < 3: return 0
        
        n = len(A)
        cnt = 0
        diff = A[1] - A[0]
        size = 2
        
        for i in range(2, n):
            if A[i] - A[i - 1] == diff:
                size += 1
            else:
                if size >= 3:
                    cnt += (size - 1) * (size - 2) // 2
                diff = A[i] - A[i - 1]
                size = 2
                
        if size >= 3:
            cnt += (size - 1) * (size - 2) // 2
            
        return cnt

A = [1,2,3,4]
res = Solution().numberOfArithmeticSlices(A)
print(res)

