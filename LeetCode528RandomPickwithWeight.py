"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a 
function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.

Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor 
has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with 
a list, even if there aren't any.
"""

from typing import List
import random

# Binary Search: 先生成一个累积和数组（第一个元素为0）
# 然后每次 pick 就生成一个 1~所有数和 的随机数，然后用
# 二分搜索判断在哪个累积和区间中
class Solution:

    # O(n)
    def __init__(self, w: List[int]):
        self.n = len(w)
        self.cumsum = [0 for i in range(self.n + 1)]

        for i in range(1, self.n + 1):
            self.cumsum[i] = self.cumsum[i - 1] + w[i - 1]

    # O(logn)
    def pickIndex(self) -> int:
        target = random.randrange(1, self.cumsum[-1] + 1)
        return self.binarySearch(target)

    def binarySearch(self, target):
        left = 1
        right = self.n + 1

        while left < right:
            mid = (left + right) // 2
            if self.cumsum[mid - 1] < target <= self.cumsum[mid]:
                return mid - 1
            elif target > self.cumsum[mid]:
                left = mid + 1
            else:
                right = mid

        return -1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
