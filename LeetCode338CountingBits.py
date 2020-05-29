"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num 
calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]

Example 2:

Input: 5
Output: [0,1,1,2,1,2]

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But 
can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).

Can you do it like a boss? Do it without using any builtin function like 
__builtin_popcount in c++ or in any other language.
"""

from typing import List

# # O(n)
# # 找规律 
# # res[1] = res[0] + 1

# # res[2] = res[0] + 1
# # res[3] = res[1] + 1

# # res[4] = res[0] + 1
# # res[5] = res[1] + 1
# # res[6] = res[2] + 1
# # res[7] = res[3] + 1
# # 每经过 2^n 个周期，下一个 2^n 个周期的数就是从 0 到 2^n 对应的数加上 1
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         idx = 0
#         bound = 1   # 当前 2^n 的边界值
#         res = [0]

#         for i in range(1, num + 1):
#             curr = 1 + res[idx]
#             res.append(curr)

#             idx += 1
#             if idx == bound:
#                 # idx 达到边界时，idx 归零，bound 变两倍
#                 idx = 0
#                 bound *= 2

#         return res

# DP: O(n) 
# dp[i] = dp[i >> 1] + (i & 1)
# 真的是很神奇的方法，i >> 1 相当于去掉最右边的一位后的值，因为这个值是小于 i 的所以已经算过了，然后只要判断 i 的最右边的位是否为 1 即可
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0 for i in range(num + 1)]
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


num = 5
res = Solution().countBits(num)
print(res)
