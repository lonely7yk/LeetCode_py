"""
Return all non-negative integers of length N such that the absolute difference between every two 
consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. 
For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.
 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Note:

1 <= N <= 9
0 <= K <= 9
"""


from typing import List

# # DFS
# class Solution:
#     def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
#         def dfs(res, curr, last, leftNum, K):
#             # last: 上一个数
#             # leftNum: 剩下还有几个数字
#             # K: 连续数字的差
#             if leftNum == 0:
#                 res.append(curr)
#                 return 
            
#             if 0 <= last - K <= 9:
#                 dfs(res, curr * 10 + last - K, last - K, leftNum - 1, K)
                
#             # K == 0 的话 last - K 和 last + K 情况是一样的
#             if K != 0 and 0 <= last + K <= 9:
#                 dfs(res, curr * 10 + last + K, last + K, leftNum - 1, K)
                
#         # N == 1 单独考虑，因为有一个 0
#         if N == 1: return list(range(10))
                
#         res = []
#         for i in range(1, 10):
#             dfs(res, i, i, N - 1, K)
            
#         return res

# Iterative
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        curr = list(range(10))

        for i in range(1, N):
            tmp = []
            for num in curr:
                last = num % 10

                if num > 0 and last + K < 10:
                    tmp.append(num * 10 + last + K)

                if num > 0 and K > 0 and last - K >= 0:
                    tmp.append(num * 10 + last - K)

            curr = tmp

        return curr

