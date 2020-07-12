"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:

Input: nums = [1,2,3]
Output: 0
 
Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

from typing import List
import collections

# O(n^2)-O(1) 67%
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         res = 0
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] == nums[j]: res += 1

#         return res

# O(n)-O(n) 67%
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = dict()
        res = 0

        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                res += seen[num]
                seen[num] += 1

        return res

nums = [1,2,3]
res = Solution().numIdenticalPairs(nums)
print(res)
