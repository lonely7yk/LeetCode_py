"""
Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination 
should be a unique set of numbers.

Note:

- All numbers will be positive integers.
- The solution set must not contain duplicate combinations.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(curr, res, idx, k, target):
            if k < 0: return 

            if target == 0 and k == 0:
                res.append(curr)
                return

            # 因为还剩 k 个数，所以该数最大为 10 - k
            for i in range(idx, 11 - k):
                if i > target: break
                dfs(curr + [i], res, i + 1, k - 1, target - i)

        if n <= 0 or k <= 0: return []
        if k > 9 or n > 45: return []   # k最大为9，n最大为45

        curr = []
        res = []
        dfs(curr, res, 1, k, n)

        return res

if __name__ == '__main__':
    k = 3
    n = 9

    res = Solution().combinationSum3(k, n)
    print(res)