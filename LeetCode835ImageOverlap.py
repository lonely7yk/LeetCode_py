"""
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.
After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes:

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
"""

from typing import List
import collections


# O(n^2)
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        # A 中所有值为 1 的位置
        LA = [(i, j) for i in range(n) for j in range(n) if A[i][j]]
        # B 中所有值为 1 的位置
        LB = [(i, j) for i in range(n) for j in range(n) if B[i][j]]

        # 统计所有值为 1 的位置的差值的个数，如果差值的个数表示shift差值的位置可以重合的个数
        counter = collections.Counter([(ax - bx, ay - by) for ax, ay in LA for bx, by in LB])
        return max(counter.values()) if counter else 0
