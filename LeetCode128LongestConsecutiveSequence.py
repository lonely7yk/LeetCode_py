"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

from typing import List


# HashMap: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cntMap = dict()
        res = 0

        for num in nums:
            # num 不在 cntMap 中才处理
            if num not in cntMap:
                left = right = 0
                # 左侧一共有多少个连续的数
                if num - 1 in cntMap: left = cntMap[num - 1]
                # 右侧一共有多少个连续的数
                if num + 1 in cntMap: right = cntMap[num + 1]

                cntMap[num] = left + right + 1
                # 更新左侧和右侧的数
                cntMap[num - left] = left + right + 1
                cntMap[num + right] = left + right + 1
                res = max(res, cntMap[num])

        return res

