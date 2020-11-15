"""
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or
the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for
future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements
(5 operations in total) to reduce x to zero.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9
"""

from typing import List


# 把数组分成 left + middle + right，由题可知 sum(left) + sum(right) = x
# 那么中间部分就是 target = sum(nums) - x。我们需要找到中间部分和为 target 的最长序列，可以使用 hashmap 来实现
# O(n)
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/935935/Java-Detailed-Explanation-O(N)-Prefix-SumMap-Longest-Target-Sub-Array
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        totSum = sum(nums)
        if totSum == x: return len(nums)
        if totSum < x: return -1

        preSumIdxMap = dict()
        preSumIdxMap[0] = -1
        # 中间部分的和
        target = totSum - x

        curSum = 0
        res = -1    # 表示中间部分的最大长度
        for i, num in enumerate(nums):
            curSum += num

            # 如果 curSum - target 曾经出现过，那么 (preSumIdxMap[curSum - target], i] 区间内的和一定为 target
            if curSum - target in preSumIdxMap:
                res = max(res, i - preSumIdxMap[curSum - target])

            if curSum not in preSumIdxMap:
                preSumIdxMap[curSum] = i

        return len(nums) - res if res != -1 else -1

