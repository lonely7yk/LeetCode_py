"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Example 2:

Input: nums = [1,10,2,9]
Output: 16

Constraints:

n == nums.length
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List


# # sort: O(nlogn)
# # 如果中位数是一个数，那所有数最后都会落到中位数，如果中位数是两个数，所有数会落到两中位数之间的一个数
# # 对于最两侧的数，他们到最终的数的距离和一定等于他们的差
# class Solution:
#     def minMoves2(self, nums: List[int]) -> int:
#         nums.sort()
#         i, j = 0, len(nums) - 1
#         res = 0

#         while i < j:
#             res += nums[j] - nums[i]
#             i += 1
#             j -= 1

#         return res
        
# sort + median: O(nlogn)  和上面的思路是一样的
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n // 2]
        res = 0

        for num in nums:
            res += abs(median - num)

        return res


# # Quick select 来选 median，时间复杂度低，但实际测试时间较长
# class Solution:
#     def minMoves2(self, nums: List[int]) -> int:
#         def quickSelect(nums, start, end, k):
#             pivot = nums[start]

#             left, right = start, end
#             while left < right:
#                 while nums[right] >= pivot and left < right: right -= 1
#                 while nums[left] <= pivot and left < right: left += 1

#                 if left < right:
#                     nums[left], nums[right] = nums[right], nums[left]
#                 else:
#                     nums[right], nums[start] = nums[start], nums[right]

#             if right == k: 
#                 return nums[right]
#             elif right < k:
#                 return quickSelect(nums, right + 1, end, k)
#             else:
#                 return quickSelect(nums, start, right - 1, k)

#         median = quickSelect(nums, 0, len(nums) - 1, len(nums) // 2)
#         res = 0

#         for num in nums:
#             res += abs(median - num)

#         return res

