"""
Given an array of non-negative integers, you are initially positioned 
at the first index of the array.

Each element in the array represents your maximum jump length at that 
position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last 
index.

Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

from typing import List

class Solution:
    # Greedy: O(n) 104ms 46.23%
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True
        if nums[0] == 0: return False

        l, r = 1, nums[0]

        while r < len(nums) - 1:
            nxt = max(i + nums[i] for i in range(l, r + 1))
            if nxt <= r: return False
            l, r = r + 1, nxt
        return True

    # # Greedy: 100ms 53%
    # def canJump(self, nums: List[int]) -> bool:
    #     if len(nums) <= 1: return True

    #     maxReach = nums[0]

    #     for i in range(1, len(nums)):
    #         if maxReach < i: return False
    #         maxReach = max(maxReach, i + nums[i])
    #         if maxReach >= len(nums) - 1: return True

    #     return False
