"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

from typing import List

# class Solution:
#     # DFS: O(n!) 36ms 81%
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def findPermutationDFS(curr, res, nums):
#             if not nums:
#                 res.append(list(curr))
#                 return

#             for i in range(len(nums)):
#                 curr.append(nums[i])
#                 tmp = nums[:i] + nums[i+1:]     # 删除 nums[i]
#                 findPermutationDFS(curr, res, tmp)
#                 curr.pop()

#         if not nums: return []

#         curr = []
#         res = []
#         findPermutationDFS(curr, res, nums)

#         return res


# O(n!) without extra memory
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(first):
            if first == n:
                res.append(nums[:])
                return
            
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                dfs(first + 1)
                nums[i], nums[first] = nums[first], nums[i]
                
            
        n = len(nums)
        res = []
        dfs(0)
        return res



if __name__ == '__main__':
    nums = [1,2,3]

    res = Solution().permute(nums)
    print(res)

