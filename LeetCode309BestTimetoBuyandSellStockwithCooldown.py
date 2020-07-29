"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""

from typing import List

# # DP: O(n) - O(n)
# # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices: return 0

#         n = len(prices)
#         # 以下表示三个状态下的最大利润
#         s0 = [0 for i in range(n)]  # idle 状态，表示没有购买的状态
#         s1 = [0 for i in range(n)]  # hold 状态，表示已经购买的状态
#         s2 = [0 for i in range(n)]  # sold 状态，表示刚卖的状态

#         s0[0] = 0
#         s1[0] = -prices[0]
#         s2[0] = 0

#         for i in range(1, n):
#             s0[i] = max(s0[i - 1], s2[i - 1])
#             s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
#             s2[i] = s1[i - 1] + prices[i]

#         return max(s0[-1], s2[-1])  # 在最后一天是不会 hold 状态的，所以不考虑 s1

# DP improved: O(n) - O(1)
# 上面的改进，因为只需要保存上一个状态的信息，所以直接用三个变量保存即可，注意使用上个状态的信息前需要进行一次保存，如 preIdle = idle
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        idle = 0
        hold = float('-inf')
        sold = 0

        for price in prices:
            preIdle = idle  # 保存上一个状态的 idle
            preHold = hold  # 保存上一个状态的 hold

            idle = max(idle, sold)
            hold = max(hold, preIdle - price)
            sold = preHold + price

        return max(idle, sold)
