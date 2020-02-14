"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation 
of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in 
ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the 
right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

from typing import List

class Solution:
    # nextPermutation: O(n) 35% 44ms
    # reference: https://leetcode.com/problems/next-permutation/discuss/13867/C%2B%2B-from-Wikipedia
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, end):
            for i in range(start, (start + end) // 2):
                nums[i], nums[end - (i - start) - 1] = nums[end - (i - start) - 1], nums[i]

        idx1 = 0    # first idx from right that leads to nums[idx1 - 1] < nums[idx1]
        for i in reversed(range(1, len(nums))):
            if nums[i - 1] < nums[i]: 
                idx1 = i
                break

        if idx1 == 0:
            reverse(nums, 0, len(nums))
            return

        idx2 = 0    # first idx from right that leads to nums[idx2] > nums[idx1 - 1]
        for i in reversed(range(idx1, len(nums))):
            if nums[i] > nums[idx1 - 1]:
                idx2 = i
                break

        nums[idx1 - 1], nums[idx2] = nums[idx2], nums[idx1 - 1]
        reverse(nums, idx1, len(nums))

