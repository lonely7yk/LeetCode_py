"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.

Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
"""

from typing import List
import math

# bucket sorting: O(n) - O(n)
# 因为结果一定大于等于 (maxVal - minVal) / (n - 1)，所以我们可以把桶长设为 ceil((maxVal - minVal) / (n - 1))，
# 这样桶中的差值最大为 ceil((maxVal - minVal) / (n - 1)) - 1 < (maxVal - minVal) / (n - 1)，因此我们只要求所有桶的最大最小值，然后计算桶间的最大差值即可
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0

        n = len(nums)
        minVal, maxVal = min(nums), max(nums)
        if minVal == maxVal: return 0   # 如果最大最小值相等，那么可以直接返回 0

        # 桶里的最大差值为 (maxVal - minVal) / (n - 1) - 1
        # 但是总体的最大差值一定大于等于 (maxVal - minVal) / (n - 1)
        bucketLen = math.ceil((maxVal - minVal) / (n - 1))
        bucketNum = (maxVal - minVal) // bucketLen + 1  # 第 k 个 bucket --> [minVal + k * bucketLen, minVal + (k + 1) * bucketLen)
        bucket = [None for i in range(bucketNum)]

        # 对每个桶的最大最小值赋值
        for num in nums:
            k = (num - minVal) // bucketLen
            if not bucket[k]:
                bucket[k] = [num, num]
            else:
                bucket[k][0] = min(bucket[k][0], num)
                bucket[k][1] = max(bucket[k][1], num)

        # 找出桶间的最大差值
        pre = 0
        res = 0
        for i in range(bucketNum):
            if not bucket[i]: continue
            res = max(res, bucket[i][0] - bucket[pre][1])
            pre = i

        return res


nums = [3,6,9,1]
res = Solution().maximumGap(nums)
print(res)