'''
Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions 
clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
'''
from typing import List


class Solution:
    # 88ms 82%
    # 多列几个就会发现 F(i+1) = F(i) + sum - n * A[n - 1 - i]
    def maxRotateFunction(self, A: List[int]) -> int:
        sum_ = sum(A)
        n = len(A)
        last = 0
        for i in range(n):
            last += i * A[i]

        max_ = last
        for i in range(n):
            fi = last + sum_ - n * A[n - 1 - i]
            last = fi
            max_ = max(max_, fi)

        return max_

if __name__ == '__main__':
    A = [4,3,2,6]
    solution = Solution()
    print(solution.maxRotateFunction(A))