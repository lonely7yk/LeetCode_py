"""
Given an unsorted array of integers, find the length of longest increasing 
subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore 
the length is 4. 

Note:

- There may be more than one LIS combination, it is only necessary for you to 
return the length.
- Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""

from typing import List

class Solution:
    # # DP O(n^2): 1200ms 31.46%
    # # dp[i] = max(dp[j]+1) if nums[j] < nums[i]
    # # dp[i] 表示以 nums[j] 结尾的最长递增序列
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     if not nums: return 0

    #     n = len(nums)
    #     res = 1
    #     dp = [1 for i in range(n)]
        
    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[j] < nums[i]:
    #                 dp[i] = max(dp[i], dp[j] + 1)

    #         res = max(res, dp[i])

    #     return res

    # Binary Search: O(nlogn) 32ms 98.73%
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)
        list_ = [nums[0]]

        for i in range(1, n):
            num = nums[i]
            if num > list_[-1]:
                list_.append(num)
            else:
                # 找到 list_ 中第一个比 num 大的数，然后用 num 替换它
                left = 0
                right = len(list_)
                while left < right:
                    mid = int((right - left) / 2 + left)
                    if list_[mid] < num:
                        left = mid + 1
                    else:
                        right = mid

                list_[left] = num

        return len(list_)


if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]

    res = Solution().lengthOfLIS(nums)
    print(res)
