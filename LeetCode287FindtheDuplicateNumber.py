"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, 
find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:

Input: [3,1,3,4,2]
Output: 3

Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

from typing import List

# slow-fast points: O(n)
# 把所有 num 当成索引，则 num 的下一个数为 nums[num]，如果 num 第二次出现，那 num 就是环中的第一个节点，
# 因为 nums[num] 就是之前 num 的下一个节点，构成了环
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: break

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# # Binary Search: O(nlogn)
# # left, right 表示重复的数的范围
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         left, right = 1, len(nums)

#         while left < right:
#             mid = (left + right) // 2

#             # 计算所有小于等于 mid 的个数
#             cnt = 0
#             for num in nums:
#                 if num <= mid: cnt += 1

#             # 个数多于 mid，说明重复数一定小于 mid
#             if cnt <= mid: left = mid + 1
#             else: right = mid

#         return left


nums = [2,2,2,2,2]
res = Solution().findDuplicate(nums)
print(res)

