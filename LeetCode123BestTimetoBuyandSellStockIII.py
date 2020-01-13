"""
Say you have an array for which the ith element is the price of a given 
stock on day i.

Design an algorithm to find the maximum profit. You may complete at most 
two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., 
you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), 
             profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), 
             profit = 4-1 = 3.

Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), 
             profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them 
             later, as you are engaging multiple transactions at the same 
             time. You must sell before buying again.

Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

from typing import List

class Solution:
    # # O(n^2) TLE
    # def maxProfit(self, prices: List[int]) -> int:
    #     def findMax(prices, left, right):
    #         """ [left, right) 的最大 profit """
    #         currMin = float('inf')
    #         maxP = 0

    #         for i in range(left, right):
    #             price = prices[i]
    #             if price < currMin:
    #                 currMin = price
    #             else:
    #                 maxP = max(maxP, price - currMin)

    #         return maxP

    #     res = 0
    #     n = len(prices)
    #     for i in range(n + 1):
    #         res = max(res, findMax(prices, 0, i) + findMax(prices, i, n))

    #     return res

    # # DP: O(n) - O(n) 84ms 48.36%
    # def maxProfit(self, prices: List[int]) -> int:
    #     if len(prices) == 0 or len(prices) == 1: return 0

    #     n = len(prices)
    #     # 表示 [0,i] 一次交易最多能赚的钱
    #     leftProfits = [0 for i in range(n)]
    #     # 表示 [i,n-1] 一次交易最多能赚的钱
    #     rightProfits = [0 for i in range(n)]

    #     currMin = prices[0]
    #     for i in range(1, n):
    #         price = prices[i]
    #         leftProfits[i] = max(leftProfits[i - 1], price - currMin)
    #         currMin = min(currMin, price)

    #     currMax = prices[-1]
    #     for i in reversed(range(n - 1)):
    #         price = prices[i]
    #         rightProfits[i] = max(rightProfits[i + 1], currMax - price)
    #         currMax = max(currMax, price)

    #     res = 0
    #     for i in range(n):
    #         res = max(res, leftProfits[i] + rightProfits[i])

    #     return res

    # # DP: O(n) - O(1) 72ms 90%
    # # 参考：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
    # def maxProfit(self, prices: List[int]) -> int:
    #     buy1, buy2 = float('inf'), float('inf')
    #     sell1, sell2 = 0, 0
    #     n = len(prices)

    #     for i in range(n):
    #         buy1 = min(buy1, prices[i])
    #         sell1 = max(sell1, prices[i] - buy1)
    #         buy2 = min(buy2, prices[i] - sell1)
    #         sell2 = max(sell2, prices[i] - buy2)

    #     return sell2

    # DP: O(n) - O(n) 84ms 48.36%
    # dp[k,i] 表示第 i 天进行第 k 次交易得到的最大收益
    # dp[k,i] = max(dp[k,i-1], max(prices[i] - prices[j] + dp[k-1,j-1]){0<=j<=i-1})
    # j = i 也可以，就是相当于少了一次交易，结果是一样的
    # 上面的版本是由这个版本推来的
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0

        n = len(prices)
        transNum = 2
        dp = [[0 for i in range(n)] for i in range(transNum + 1)]

        for k in range(1, transNum + 1):
            min_ = prices[0]
            for i in range(1, n):
                # min_ = prices[0]
                # for j in range(1, i):
                #     min_ = min(min_, prices[j] - dp[k - 1][j - 1])
                min_ = min(min_, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - min_)

        return dp[transNum][n - 1]


if __name__ == '__main__':
    # prices = [7,6,4,3,1]
    # prices = [3,3,5,0,0,3,1,4]
    prices = [1,2,3,4,5]

    res = Solution().maxProfit(prices)
    print(res)

