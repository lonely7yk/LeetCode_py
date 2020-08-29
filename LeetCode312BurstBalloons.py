"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""

from typing import List

# 2D DP: O(n^3) - O(n^2)
# dp[i][j]: 打碎 i~j 气球获得的最大 coin
# dp[i][j] = max(left + right + leftVal * rightVal * nums[k])    表示打碎第 i~k-1 气球和 k+1~j 气球后获得的 coin再加上打碎第 k 个气球的 coin
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums: return 0
        
        n = len(nums)
        dp = [[0 for j in range(n)] for i in range(n)]
        
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                
                for k in range(i, j + 1):
                    left = 0 if k == i else dp[i][k - 1]
                    right = 0 if k == j else dp[k + 1][j]
                    leftVal = 1 if i == 0 else nums[i - 1]
                    rightVal = 1 if j == n - 1 else nums[j + 1]
                    
                    dp[i][j] = max(dp[i][j], \
                                  left + right + leftVal * rightVal * nums[k])
                    
        return dp[0][n - 1]
        
