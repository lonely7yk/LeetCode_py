"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""

from typing import List
import collections

# PreSum + HashMap: O(n)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)
        tmp = [0 for i in range(n)]

        # 把 nums 转换为正负值，0 为 -1，1 为 1
        # 这样，如果一段区间的求和为 0，说明 0 和 1 的数量一样多
        for i in range(n):
            tmp[i] = 1 if nums[i] == 1 else -1

        # 求出所有累加和，累积和相同，说明中间部分的和为 0
        cumsum = [0 for i in range(n + 1)]
        for i in range(n):
            cumsum[i + 1] = cumsum[i] + tmp[i]

        # 把累积和对应的 idx 放入 list 中
        cumsumMap = collections.defaultdict(list)
        for i in range(n + 1):
            cumsumMap[cumsum[i]].append(i)

        # 对于每个累积和计算最大索引和最小索引差值
        res = 0
        for cumsum, idxs in cumsumMap.items():
            res = max(res, idxs[-1] - idxs[0])

        return res


nums = [0,1]
res = Solution().findMaxLength(nums)
print(res)
