"""
Given an integer array nums, return the number of longest increasing subsequences.

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 
subsequences' length is 1, so output 5.

Constraints:

0 <= nums.length <= 2000
-10^6 <= nums[i] <= 10^6
"""

from typing import List
import bisect
import collections

# DP: O(n^2)
# class Solution:
#     def findNumberOfLIS(self, nums: List[int]) -> int:
#         if not nums: return 0
#         n = len(nums)
#         dp = [1 for i in range(n)]
#         cnt = [1 for i in range(n)]
        
#         for i in range(1, n):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     if dp[j] + 1 == dp[i]:
#                         cnt[i] += cnt[j]
#                     elif dp[j] + 1 > dp[i]:
#                         dp[i] = dp[j] + 1
#                         cnt[i] = cnt[j]
                        
#         maxLen = max(dp)
#         res = 0
#         for i in range(n):
#             if dp[i] == maxLen: res += cnt[i]
                
#         return res


# Binary Search: O(nlogn)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        cur = []
        n = len(nums)
        dp = collections.defaultdict(collections.Counter)
        dp[-1][-10 ** 9] = 1

        for num in nums:
            idx = bisect.bisect_left(cur, num)
            if idx == len(cur):
                cur.append(num)
            else:
                cur[idx] = num

            dp[idx][num] += sum(dp[idx - 1][n] for n in dp[idx - 1] if n < num)

        return sum(dp[max(0, len(cur) - 1)].values())


nums = [1,2,4,3,5,4,7,2]
res = Solution().findNumberOfLIS(nums)
print(res)
