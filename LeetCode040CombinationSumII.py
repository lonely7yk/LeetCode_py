"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique 
combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

from typing import List

class Solution:
    # DFS: 44 ms 85%
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def findCombinationDFS(curr, res, candidates, idx, target):
            if target == 0:
                res.append(list(curr))
                return

            for i in range(idx, len(candidates)):
                # 因为已经排序过了，如果当前值大于 target 则后面的值一定也大于 target
                if candidates[i] > target: break
                # 这句可以避免重复
                if i > idx and candidates[i] == candidates[i - 1]: continue

                curr.append(candidates[i])
                findCombinationDFS(curr, res, candidates, i + 1, target - candidates[i])
                curr.pop()

        if not candidates: return []

        curr = []
        res = []
        candidates.sort()
        findCombinationDFS(curr, res, candidates, 0, target)
        return res

if __name__ == '__main__':
    # candidates = [10,1,2,7,6,1,5]
    # target = 8

    candidates = [2,5,2,1,2]
    target = 5

    res = Solution().combinationSum2(candidates, target)
    print(res)

