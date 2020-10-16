"""
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, 
you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of 
difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a 
job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is 
jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs 
return -1.

Example 1:

Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 

Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.

Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.

Example 4:

Input: jobDifficulty = [7,1,7,1,7,1], d = 3
Output: 15

Example 5:

Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
Output: 843
 

Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10
"""

from typing import List


# # 2D-DP: O(n^2 * d) O(nd)
# class Solution:
#     def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
#         if d > len(jobDifficulty): return -1
        
#         n = len(jobDifficulty)
#         # dp[i][j] 表示对 i~n-1 的 job 进行分配，剩下 j 天的情况，最小的 difficulty
#         # dp[i][j] = min_k{dp[k+1][j-1] + max(nums[i:k+1])}   i<=k<n-j+1
#         dp = [[float('inf') for j in range(d + 1)] for i in range(n + 1)]
#         dp[n][0] = 0
        
#         for j in range(1, d + 1):
#             for i in range(n - j + 1):
#                 maxd = 0
#                 # i <= k < n - j + 1
#                 for k in range(i, n - j + 1):
#                     maxd = max(maxd, jobDifficulty[k])
#                     dp[i][j] = min(dp[i][j], dp[k + 1][j-1] + maxd)

#         return dp[0][d]

# 上面代码的改进版 1D-DP: O(n^2 * d) O(n)
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty): return -1
        
        n = len(jobDifficulty)
        # dp[i][j] 表示对 i~n-1 的 job 进行分配，剩下 j 天的情况，最小的 difficulty
        # dp[i][j] = min_k{dp[k+1][j-1] + max(nums[i:k+1])}   i<=k<n-j+1
        dp = [float('inf')for i in range(n + 1)]
        dp[n] = 0
        
        for j in range(1, d + 1):
            for i in range(n - j + 1):
                maxd = 0
                dp[i] = inf
                # i <= k < n - j + 1
                for k in range(i, n - j + 1):
                    maxd = max(maxd, jobDifficulty[k])
                    dp[i] = min(dp[i], dp[k + 1] + maxd)

        return dp[0]

        
# # DFS + memo
# class Solution:
#     def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
#         n = len(jobDifficulty)
        
#         @functools.lru_cache(None)
#         def dfs(i, d):
#             if d == 1: return max(jobDifficulty[i:])
            
#             maxd = 0
#             res = float('inf')
#             for j in range(i, n - d + 1):
#                 maxd = max(maxd, jobDifficulty[j])
#                 res = min(res, maxd + dfs(j + 1, d - 1))
                
#             return res
                
#         if n < d: return -1
#         return dfs(0, d)
