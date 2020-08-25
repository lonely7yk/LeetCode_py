"""
In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.

Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
 

Note:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""

from typing import List
import bisect
import collections

# # DP: O(maxDay) - O(maxDay) dp[i] = min(dp[max(0, i - 1)] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
# class Solution:
#     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
#         daySet = set(days)
#         maxDay = days[-1]
#         dp = [0 for i in range(maxDay + 1)]
        
#         for i in range(1, maxDay + 1):
#             if i not in daySet:
#                 dp[i] = dp[i - 1]
#             else:
#                 dp[i] = min(dp[max(0, i - 1)] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
                
#         return dp[-1]
        

# # 上面 DP 改进，只保存 30 天的前   O(maxDay) - O(30)
# class Solution:
#     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
#         daySet = set(days)
#         minDay = days[0]
#         maxDay = days[-1]
#         dp = [0 for i in range(30)]

#         for i in range(minDay, maxDay + 1):
#             if i not in daySet:
#                 dp[i % 30] = dp[(i - 1) % 30]
#             else:
#                 dp[i % 30] = min(dp[max(0, i - 1) % 30] + costs[0], \
#                     dp[max(0, i - 7) % 30] + costs[1], dp[max(0, i - 30) % 30] + costs[2])

#         return dp[maxDay % 30]


# DP + Queue: O(n) - O(30)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost = 0
        # (day, cost)   cost 表示在 day 这天购买 7 pass 车票后的最小累积价格
        last7 = collections.deque()
        # (day, cost)   cost 表示在 day 这天购买 30 pass 车票后的最小累积价格
        last30 = collections.deque()

        for day in days:
            # last7[0][0] + 7 <= day 表示 7 天车票已经过期了
            while last7 and last7[0][0] + 7 <= day: last7.popleft()
            while last30 and last30[0][0] + 30 <= day: last30.popleft()

            last7.append((day, cost + costs[1]))
            last30.append((day, cost + costs[2]))

            cost = min(cost + costs[0], last7[0][1], last30[0][1])

        return cost



days = [1,5,8,9,10,12,13,16,17,18,19,20,23,24,29]
costs = [3,12,54]
res = Solution().mincostTickets(days, costs)
print(res)