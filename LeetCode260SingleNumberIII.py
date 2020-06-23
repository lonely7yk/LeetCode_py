"""
Given an array of numbers nums, in which exactly two elements appear only once and all the 
other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only 
constant space complexity?
"""

from typing import List

# Bit Operation: O(n) O(1)
# 如果把所有数进行异或，那么结果 diff 就等价于两个只出现一次的数进行异或，因为其他出现两次的异或后的结果为 0
# 因为这两个数是不同的，所以他们肯定有一位是不同的，我们随机找一位可以通过 diff & -diff 找到最后一位为 1 的数
# 然后通过这个 1 把所有数分成两堆，在该位上为 1 的和在该位上为 0 的，把两堆数都进行异或可得到两个结果。
# 可以确定的是那两个数肯定在不同堆，而在同一堆的其他数一定成对出现，所以这样可以两堆的异或值就是两个结果。
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff ^= num

        diff &= -diff   # 得到 diff 中最后一位 1 对应的数

        first, second = 0, 0
        for num in nums:
            if num & diff != 0:
                first ^= num
            else:
                second ^= num

        return [first, second]

