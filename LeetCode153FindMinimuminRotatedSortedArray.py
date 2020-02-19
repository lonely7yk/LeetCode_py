"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""

from typing import List

class Solution:
    # # Binary Search: 32ms 96%
    # # 直观想法
    # def findMin(self, nums: List[int]) -> int:
    #     if len(nums) == 1: return nums[0]
    #     if nums[0] < nums[-1]: return nums[0]

    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         mid = (left + right) // 2

    #         if nums[mid] > nums[mid + 1]: return nums[mid + 1]

    #         if nums[mid] > nums[left]:
    #             left = mid + 1
    #         else:
    #             right = mid

    #     return -1

    # Binary Search
    # 感觉像是技巧了。必须比较 nums[mid] < nums[right] 不能比较 nums[left]
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


if __name__ == '__main__':
    # nums = [3,4,5,1,2] 
    nums = [4,5,6,7,0,1,2]

    res = Solution().findMin(nums)
    print(res)
