"""
You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
"""

from typing import List

# 全部异或，最终结果就是唯一的数 O(n)
# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         res = 0
#         for num in nums:
#             res = res ^ num

#         return res

# 二分法 O(logn)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 边界条件
        if len(nums) == 1: return nums[0]
        if nums[0] != nums[1]: return nums[0]
        if nums[-1] != nums[-2]: return nums[-1]

        left, right = 1, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # 首先明确唯一的数只有可能在偶数索引出现
            # 如果 mid 为偶数，nums[mid] == nums[mid - 1] 说明唯一数在 mid 左侧
            # nums[mid] == nums[mid + 1] 说明唯一数在 mid 右侧
            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    right = mid - 1
                elif nums[mid] == nums[mid + 1]:
                    left = mid + 2
                else:
                    return nums[mid]
            # 如果 mid 为奇数，nums[mid] == nums[mid - 1] 说明唯一数在 mid 右侧
            # nums[mid] == nums[mid + 1] 说明唯一数在 mid 左侧
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    right = mid

        return -1



nums = [1,1,2,3,3,4,4,8,8]
# nums = [3,3,7,7,10,11,11]
res = Solution().singleNonDuplicate(nums)
print(res)
