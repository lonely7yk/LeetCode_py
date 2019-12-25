"""
Given an array of non-negative integers, you are initially positioned 
at the first index of the array.

Each element in the array represents your maximum jump length at that 
position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:

You can assume that you can always reach the last index.
"""

from typing import List

class Solution:
    # # DP: O(n^2) TLE
    # def jump(self, nums: List[int]) -> int:
    #     dp = [0] + [float('inf')] * (len(nums) - 1)
    #     for i in range(1, len(nums)):
    #         for j in range(0, len(dp)):
    #             if nums[j] >= i - j:
    #                 dp[i] = min(dp[i], dp[j] + 1)
    #     return dp[len(nums) - 1]

    # Greedy: O(n) 116ms 32%
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        # 第一次跳跃后，最近落地点为 1，最远落地点为 nums[0]
        l, r = 1, nums[0]   # l 表示第 i 次跳跃最近的落地点，r 表示第 i 次跳跃最远的落地点
        times = 1
        while r < len(nums) - 1:
            nxt = max(i + nums[i] for i in range(l, r + 1)) # 下一次跳跃的最远落地点
            l, r = r + 1, nxt
            times += 1
        return times

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    res = Solution().jump(nums)
    print(res)
