"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime , endTime and profit arrays, you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Example 1:

Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:

Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.

Example 3:

Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""

from typing import List
import bisect

# DP + Binary Search: O(nlogn)
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = [(t1, t2, p) for t1,t2,p in zip(startTime, endTime, profit)]
        # 按照 endtime 排序
        intervals.sort(key=lambda x: x[1])
        
        n = len(intervals)
        dp = [(0,0)]    # (t,p) 表示在t时间前最多能拿到多少 profit
        
        for t1, t2, p in intervals:
            # 找到 t1 时间前最大利润的索引
            idx = bisect.bisect(dp, (t1, float('inf'))) - 1
            currProfit = dp[idx][1] + p     # 当前索引
            if currProfit > dp[-1][1]:
                dp.append((t2, currProfit))
            
        return dp[-1][1]
        
