"""
Given a set of distinct integers, nums, return all possible subsets (the 
power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

from typing import List

class Solution:
    # # DFS backtracking: 28ms 86.81%
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     def findSubsetsDFS(curr, res, idx, nums):
    #         res.append(list(curr))      # curr 不可能已经在 list 中

    #         for i in range(idx, len(nums)):
    #             curr.append(nums[i])
    #             findSubsetsDFS(curr, res, i + 1, nums)
    #             curr.pop()

    #     curr = []
    #     res = []
    #     findSubsetsDFS(curr, res, 0, nums)

    #     return res

    # iterative: 20ms 99.54%
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]]
        for i in range(n):
            size = len(res)
            for j in range(size):
                tmp = res[j]
                newSet = tmp + [nums[i]]
                res.append(newSet)

        return res


if __name__ == '__main__':
    nums = [1,2,3]
    # nums = []

    res = Solution().subsets(nums)
    print(res)

