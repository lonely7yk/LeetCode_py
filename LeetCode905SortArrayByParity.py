"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 
Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""

from typing import List

# In-place
# class Solution:
#     def sortArrayByParity(self, A: List[int]) -> List[int]:
#         idx1 = 0
#         n = len(A)
        
#         for idx2 in range(n):
#             if A[idx2] % 2 == 0:
#                 A[idx1], A[idx2] = A[idx2], A[idx1]
#                 idx1 += 1
                
#         return A
        

# not in-place
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        res = [0 for i in range(n)]
        start = 0
        end = n - 1
        
        for i in range(n):
            if A[i] % 2 == 0:
                res[start] = A[i]
                start += 1
            else:
                res[end] = A[i]
                end -= 1
                
        return res
        