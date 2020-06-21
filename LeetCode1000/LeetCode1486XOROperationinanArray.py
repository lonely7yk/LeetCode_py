"""
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

 

Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
Example 2:

Input: n = 4, start = 3
Output: 8
Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
Example 3:

Input: n = 1, start = 7
Output: 7
Example 4:

Input: n = 10, start = 5
Output: 2
 

Constraints:

1 <= n <= 1000
0 <= start <= 1000
n == nums.length
"""

import functools

# # Brute Force: O(n) 直接全部异或
# class Solution:
#     def xorOperation(self, n: int, start: int) -> int:
#         nums = [start + 2 * i for i in range(n)]
#         return functools.reduce(lambda x, y: x ^ y, nums, 0)


# O(1) 
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        if n == 1: return start

        last = start + 2 * (n - 1)
        # 如果 start % 4 == 0 or 1，那么从右往左的第二位一定为 0，这样 start ^ (start+2) == 2（就是每两个数的结果为 2）
        # 如果 n % 4 == 0，那么所有的 2 互相异或，结果为 0。
        # 如果 n % 4 == 1，那么除了最后一个数 last，其他所有 2 互相异或得 0，结果为 last
        # 如果 n % 4 == 2，那么除了最后两个数，其他所有 2 互相异或得 0，最后两个数异或结果为 2
        # 如果 n % 4 == 3，那么除了最后三个数，其他所有 2 互相异或得 0，最后三个数异或结果为 2 ^ last
        # start % 4 == 2 or 3 的情景只要把第一个数排除，因为 (start + 2) % 4 == 0 or 1，所以从 start + 2 开始的情景和之前是一样的
        if start % 4 <= 1:
            if n % 4 == 0:
                return 0
            elif n % 4 == 1:
                return last
            elif n % 4 == 2:
                return 2
            else:
                return 2 ^ last
        else:
            if (n - 1) % 4 == 0:
                return start
            elif (n - 1) % 4 == 1:
                return start ^ last
            elif (n - 1) % 4 == 2:
                return start ^ 2
            else:
                return start ^ 2 ^ last

n = 10
start = 5
res = Solution().xorOperation(n, start)
print(res)
