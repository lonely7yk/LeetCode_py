"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

from typing import List
import collections


# DFS + HashMap
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         def dfs(res, curr, counter):
#             if len(curr) == len(nums):
#                 res.append(curr)
#                 return
            
#             for c in counter:
#                 if counter[c] > 0:
#                     counter[c] -= 1
#                     dfs(res, curr + [c], counter)
#                     counter[c] += 1
                    
#         counter = collections.Counter(nums)
#         res = []
#         dfs(res, [], counter)
#         return res


# DFS + Set
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(res, first):
            if first == len(nums):
                res.append(list(nums))
                return

            seen = set()
            for i in range(first, len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    nums[first], nums[i] = nums[i], nums[first]
                    dfs(res, first + 1)
                    nums[first], nums[i] = nums[i], nums[first]

        nums.sort()
        res = []
        dfs(res, 0)
        return res

