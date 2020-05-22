"""
Given a positive integer num, output its complement number. The complement strategy is to flip the 
bits of its binary representation.

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. 
So you need to output 2.

Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. 
So you need to output 0.

Constraints:

The given integer num is guaranteed to fit within the range of a 32-bit signed integer.
num >= 1
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
"""

# O(n) 对于 num 的每一位取反，然后加起来
# class Solution:
#     def findComplement(self, num: int) -> int:
#         res = 0
#         cnt = 0

#         while num != 0:
#             curBit = (num & 1) ^ 1  # 先取出当前位的值，然后取反（可以直接和 1 异或得到）
#             res += (curBit << cnt)

#             cnt += 1
#             num = num >> 1

#         return res

# 找到大于 num 的最小 2 的 n 次方，比如 11001 对应的数是 100000，减1为 11111，位数和 11001 一样
# 两个数异或即可得到结果。或者可以用 11111 - 11001 也可以得到对应结果
class Solution:
    def findComplement(self, num: int) -> int:
        tmp = 1
        while tmp <= num:
            tmp = tmp << 1

        return (tmp - 1) ^ num
        # return (tmp - 1) - num

num = 5
res = Solution().findComplement(num)
print(res)
