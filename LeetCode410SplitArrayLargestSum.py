"""
Given an array which consists of non-negative integers and an integer m, you can split the array 
into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among 
these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)

Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""

from typing import List

# Binary Search: O(nlogn) 87%
# https://leetcode.com/problems/split-array-largest-sum/discuss/89817/Clear-Explanation%3A-8ms-Binary-Search-Java
# 首先，结果在 [max(nums), sum(nums)] 之间，所以 left = max(nums), right = sum(nums) + 1
# 对于 mid = (left + right) // 2
# 如果 nums 能够分出多于 m 个分组，使得每个分组的和小于等于 mid，那说明 mid 过小，mid 如果取大一点则分组数会变少
# 如果 nums 不能分出多于 m 个分组，那说明 mid 过大，mid 取小一点则分组数会变多
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 判断 nums 是否能分出小于等于 m 个分组（前提：每个分组和小于 mid）
        def valid(mid, nums, m):
            cnt = 1     # 分组数量
            curr = 0    # 当前分组的和

            for num in nums:
                curr += num
                if curr > mid:
                    curr = num
                    cnt += 1

                    if cnt > m: return False

            return True


        left, right = max(nums), sum(nums) + 1

        while left < right:
            mid = (left + right) // 2

            if valid(mid, nums, m):
                right = mid
            else:
                left = mid + 1

        return left

nums = [7,2,5,10,8]
m = 2
res = Solution().splitArray(nums, m)
print(res)

