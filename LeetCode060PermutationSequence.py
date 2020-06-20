"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""

import math

# 对于数组 [1,2,...,n]，放置第一个数后，有 (n-1)! 中排列可能，所以可以通过  k / (n-1)! 求出当前数的索引
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i + 1 for i in range(n)]

        k -= 1  # 这个比较重要，因为数组是基于0的，所以要把 k 也变成基于0
        res = ""
        while nums:
            division = math.factorial(len(nums) - 1)
            idx = k // division
            res += str(nums[idx])

            k -= division * idx
            nums.pop(idx)

        return res


n = 4
k = 9
res = Solution().getPermutation(n, k)
print(res)
