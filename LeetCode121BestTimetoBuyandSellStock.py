"""
Say you have an array for which the ith element is the price of a given 
stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy 
one and sell one share of the stock), design an algorithm to find the 
maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), 
             profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying 
             price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

from typing import List

class Solution:
    # Greedy: O(n) 60ms 82%
    def maxProfit(self, prices: List[int]) -> int:
        lastMin = float('inf')  # 表示到目前位置，前面最小的价格
        res = 0

        # 如果价格小于 lastMin，更新 lastMin
        # 否则，更新 res
        for price in prices:
            if price < lastMin:
                lastMin = price
            else:
                res = max(res, price - lastMin)

        return res

if __name__ == '__main__':
    # prices = [7,1,5,3,6,4]
    prices = [7,6,5,4,3,2,1]

    res = Solution().maxProfit(prices)
    print(res)
