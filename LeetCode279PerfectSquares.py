"""
Given a positive integer n, find the least number of perfect square numbers 
(for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

import math
import collections

# # DP: O(nlogn) 40%
# # dp[i] = min(dp[i], dp[i - j * j] + 1)   for j * j < i
# # dp[i] = 1 if j * j == i
# class Solution:
#     def numSquares(self, n: int) -> int:
#         dp = [float('inf') for i in range(n + 1)]
#         dp[1] = 1

#         for i in range(2, n + 1):
#             if math.sqrt(i) == int(math.sqrt(i)):
#                 dp[i] = 1
#                 continue

#             for j in range(1, int(math.sqrt(i)) + 1):
#                 dp[i] = min(dp[i], dp[i - j * j] + 1)

#         return dp[n]

# BFS 66%
# https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS
class Solution:
    def numSquares(self, n: int) -> int:
        deque = collections.deque([n])
        # 存储所有小于 n 的平方数
        lst = [i * i for i in range(1, int(n ** 0.5) + 1)]
        cnt = 0

        # 每到一层，cnt += 1
        while deque:
            cnt += 1
            size = len(deque)

            for i in range(size):
                curr = deque.popleft()
                for num in lst:
                    if curr - num == 0: return cnt
                    if curr - num < 0: break

                    deque.append(curr - num)

        return -1


n = 13
res = Solution().numSquares(n)
print(res)
