"""
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time 
is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:

Input: [1,2,3,4]
Output: "23:41"

Example 2:

Input: [5,5,5,5]
Output: ""
 
Note:

A.length == 4
0 <= A[i] <= 9
"""

from typing import List
import itertools

# # DFS: 用 DFS 找出 A 的所有排列组合结果，前两个为时，后两个为分。过滤掉不合理的，然后对剩下的结果排序。
# class Solution:
#     def largestTimeFromDigits(self, A: List[int]) -> str:
#         def dfs(res, curr, A):
#             if not A:
#                 first = curr[0] * 10 + curr[1]
#                 second = curr[2] * 10 + curr[3]
#                 if first >= 24 or second >=60: return

#                 res.append((first, second))

#             for i in range(len(A)):
#                 tmp = list(A)
#                 tmp.pop(i)
#                 dfs(res, curr + [A[i]], tmp)

#         res = []
#         dfs(res, [], A)

#         res.sort(key=lambda x: (x[0], x[1]))

#         if not res: return ""

#         return str(res[-1][0]).zfill(2) + ":" + str(res[-1][1]).zfill(2)

# 使用 itertools 直接找出所有的排列可能，然后在字符串中取最大
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        res = ""
        for tmp in itertools.permutations(A, 4):
            if tmp[0] * 10 + tmp[1] < 24 and tmp[2] < 6:
                res = max(res, "%d%d:%d%d" % tmp)

        return res


A = [1,2,3,4]
res = Solution().largestTimeFromDigits(A)
print(res)
