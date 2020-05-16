"""
Given a circular array C of integers represented by A, find the maximum possible sum of a 
non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  
(Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  
(Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, 
k2 <= j with k1 % A.length = k2 % A.length.)

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1

Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000
"""

from typing import List

# 先理解 53 题，求最大子序列和
# 这题的 max subarray 可能在中间部分，也可能是结尾部分加开头部分
# 前一种情况就是直接用 53 题的解法求 max subarray 的 maxSum
# 后一种情况就是用同样解法求 min subarray 的 minSum，然后 total - minSum 就是 maxSum
# O(n) : maxSubarray
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        currMax = 0
        currMin = 0
        maxSum = float('-inf')
        minSum = float('inf')
        total = 0

        for a in A:
            currMax = max(currMax + a, a)
            currMin = min(currMin + a, a)
            maxSum = max(maxSum, currMax)
            minSum = min(minSum, currMin)
            total += a

        # 如果 maxSum <= 0 说明 A 中没有正数，这是 maxSum 为 A 中最大值，minSum 等于 total
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum 



# A = [1,-2,3,-2]
# A= [5,-3,5]
# A = [-2,-3,-1]
# A = [3,1,3,2,6]
A = [-2,4,-5,4,-5,9,4]
res = Solution().maxSubarraySumCircular(A)
print(res)

